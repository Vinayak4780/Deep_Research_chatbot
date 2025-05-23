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
