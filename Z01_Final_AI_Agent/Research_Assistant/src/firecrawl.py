import os
from firecrawl import FirecrawlApp, ScrapeOptions
from dotenv import load_dotenv

load_dotenv()


class FirecrawlAPI:
    """
        Class created to use the FireCrawl API
    """
    def __init__(self):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("Missing FIRECRAWL_API_KEY environment variable")
        self.app = FirecrawlApp(api_key=api_key)

    def search_topic(self, topic: str, num_results: int = 10):
        """
        Find academic resources for the user's query and returns a 
        certain number of results.

        Args:
            topic: The agent's query to be looked up.
            num_results: Number of results that the API should look for.

        Returns:
            Markdown: Contains all of the scraped data found
        """
        try:
            result = self.app.search(
                query=f"{topic}",
                limit=num_results,
                scrape_options=ScrapeOptions(
                    formats=["markdown"]
                )
            )
            return result
        except Exception as e:
            print(e)
            return []

    def scrape_websites(self, url: str):
        """
        Scrape the website using the url and extract the data in markdown format

        Args:
            url: The website to be scraped.

        Returns:
            Markdown: Contains all of the scraped website data found
        """
        try:
            result = self.app.scrape_url(
                url,
                formats=["markdown"]
            )
            return result
        except Exception as e:
            print(e)
            return None