# Deep Research Chatbot

## Overview

The Deep Research Chatbot is an AI-powered assistant designed to streamline and automate in-depth research workflows. Leveraging a combination of LangChain agents and a graph-based state machine, this project orchestrates information gathering, question decomposition, and draft generation to deliver precise, context-aware responses.

## Key Features

- **Research Agent**: Uses web search tools to gather relevant information based on user queries.  
- **Drafter Agent**: Refines and synthesizes research findings into coherent draft answers.  
- **Graph-Based Workflow**: Defines a multi-step research process using `StateGraph` for orchestration and state management.  
- **Interactive CLI**: Runs as a command-line interface, prompting users for questions and displaying final answers.  

## Prerequisites

- **Python**: Version 3.8 or higher  
- **Model File**: Download the Mistral 7B Instruct GGUF model (`mistral-7b-instruct-v0.1.Q4_K_M.gguf`) and update the path in `shared_llm.py`.  
- **Optional GPU**: Recommended for faster inference when using LlamaCpp.  

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/Deep_Research_chatbot.git
   cd Deep_Research_chatbot
2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   Install dependencies

   ```bash

   pip install --upgrade pip
   pip install python-dotenv llama-cpp-python langchain langchain-community langgraph pydantic
Configuration
Environment Variables (optional):

Create a .env file at the project root to store API keys or other configuration values:

ini
Copy
Edit
# .env
TAVILY_API_KEY=your_tavily_api_key
Model Path:

Open shared_llm.py and update the model_path parameter to point to your downloaded GGUF model file.

Usage
Run the chatbot via the command line:

bash
Copy
Edit
python main.py
Enter your research question when prompted.

Type exit or quit to end the session.

Project Structure
text
Copy
Edit
Deep_Research_chatbot-main/
├── agents/
│   ├── drafter.py          # Prompt template for draft generation
│   └── research.py         # Research agent setup and tool integration
├── graph/
│   └── research_graph.py   # StateGraph definition for the research workflow
├── shared_llm.py           # LLM configuration using LlamaCpp
├── main.py                 # Entry point and CLI loop
└── README.md               # Project overview and instructions
Contributing
Contributions are welcome! Please open an issue or submit a pull request for:

Bug fixes and enhancements

New research tools or agents

Documentation improvements

License
This project is released under the MIT License.

Copy
Edit
