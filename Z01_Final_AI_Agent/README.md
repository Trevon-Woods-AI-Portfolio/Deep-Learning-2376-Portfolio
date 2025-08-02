
# 🧠 Research Assistant Agent – AI Capstone Project

## 🎯 Objective

This capstone project challenges student groups to design, implement, and demonstrate an AI agent system that applies key concepts from the course. The goal is to gain hands-on experience building and evaluating an AI-driven assistant that leverages language-based planning, reasoning, and decision-making.

## 🤖 Project Overview – Research Assistant Agent

The Research Assistant Agent is an intelligent system designed to help users research topics, gather credible information, and present findings in a clear, organized format. It integrates modern AI tools to deliver a streamlined research experience.

## ✨ Key Features

- 🔍 **Information Retrieval & Summarization**  
  Retrieves and condenses content from multiple online sources to provide concise overviews.

- 🧾 **Source Evaluation**  
  Assesses credibility and relevance of sources to ensure reliable results.

- 📂 **Structured Report Generation**  
  Organizes findings into coherent formats suitable for academic or professional use.

- 📚 **Citation Management**  
  Tracks and formats references for easy citation in MLA style.

## 🧱 Agent Architecture

The system follows a modular and extensible design to manage tasks effectively:

- **Input Processing**  
  Interprets user queries or environmental inputs to define clear research objectives.

- **Memory System**  
  Stores retrieved content, user preferences, and intermediate findings for context-aware responses.

- **Reasoning Component**  
  Utilizes Chain-of-Thought (CoT) reasoning to make step-by-step decisions and plan research actions.

- **Output Generation**  
  Formats and presents results in structured outputs, including summaries, reports, and citation lists.

## 🧩 Agent Pattern

- 🧠 **Chain-of-Thought (CoT) Reasoning**  
  The agent thinks step-by-step through complex tasks to ensure logical consistency and clarity in outcomes.

## 🛠️ External Tools & Integrations

- 🌐 **Web Search:**
  - [Firecrawl](https://firecrawl.dev): Enables live information retrieval from the web.

- 🧠 **LLM Interactions:**
  - [OpenAI GPT-4o](https://openai.com/gpt-4o): Powers natural language understanding, summarization, and reasoning.
  - **Firecrawl**: Also used to enhance LLM input with real-time web context.

---


---

## 🚀 Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/R2D2/research-assistant-agent.git
   cd research-assistant-agent
   
2. **Install Depedancies:**
    ```bash
    pip install -r requirements.txt

3. **Add environment variables:**
    ```bash
    OPENAI_API_KEY=your_openai_key
    FIRECRAWL_API_KEY=your_firecrawl_key

4. **Run the agent:**
    ```bash
    python src/main.py


