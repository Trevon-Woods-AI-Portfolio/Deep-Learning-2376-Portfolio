from typing import Dict, Any
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.caches import InMemoryCache
from langchain_core.globals import set_llm_cache
from .models import ResearchState
from .firecrawl import FirecrawlAPI
from .prompts import ResearchPrompts


class Workflow:
    def __init__(self):
        self.firecrawl = FirecrawlAPI()
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.1)
        self.prompts = ResearchPrompts()
        self.workflow = self._build_workflow()
        self.cache = InMemoryCache()
        set_llm_cache(self.cache)

    def _build_workflow(self):
        graph = StateGraph(ResearchState)
        graph.add_node("extract_urls", self.find_academic_resources)
        graph.add_node("gather_analyze_report", self.gather_analyze_report)
        graph.set_entry_point("extract_urls")
        graph.add_edge("extract_urls", "gather_analyze_report")
        graph.add_edge("gather_analyze_report", END)
        return graph.compile()
    
    def find_academic_resources(self, state: ResearchState):
        print(f"Finding Academic Resources about {state.topic}")

        web_query = f"information about {state.topic}"
        search_results = self.firecrawl.search_topic(web_query, num_results=5)

        urls = []

        for result in search_results.data:
            urls.append(result.get("url", ""))

        return {"source_urls": urls}
        
    def gather_analyze_report(self, state: ResearchState):
        retrieved_urls = getattr(state, "source_urls", [])

        if not retrieved_urls:
            print("No urls found. Starting search for urls...")
            web_query = f"Academic articles or information about {state.topic}"
            search_results = self.firecrawl.search_topic(web_query, num_results=5)

            retrieved_urls = []

            for result in search_results.data:
                retrieved_urls.append(result.get("url", ""))
        
        research_content = ""
        scraped_data = []

        print("Extracting Markdown Info: \n")
        for i, url in enumerate(retrieved_urls):
            print(f"Scrapping {url}")
            scraped = self.firecrawl.scrape_websites(url)
            if scraped:
                research_content + scraped.markdown[:15000] + "\n\n"
                scraped_data.append(f"{scraped.markdown[:15000]}\n\n")

        print()

        messages = [
            SystemMessage(content=self.prompts.REPORT_CREATION_SYSTEM),
            HumanMessage(content=self.prompts.report_creation_user(state.topic, research_content))
        ]

        try:
            response = self.llm.invoke(messages)
            return {"report": response.content, "source_content": scraped_data}
        except Exception as e:
            print(e)
            return {"report": "", "source_content": []}


    def run(self, topic: str) -> ResearchState:
        starting_state = ResearchState(topic=topic)
        finished_state = self.workflow.invoke(starting_state)
        return ResearchState(**finished_state)