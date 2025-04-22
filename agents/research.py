from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import Tool, initialize_agent, AgentType
from shared_llm import llm
import concurrent.futures

# ⛑️ Safe wrapper for Tavily
def safe_tavily_search(query, timeout=10):
    search = TavilySearchResults()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(search.run, query)
        try:
            return future.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            return "⚠️ Tavily search timed out."

def researcher_agent():
    tools = [
        Tool(
            name="TavilySearch",
            func=safe_tavily_search,
            description="Use this tool to search the web for current and factual information. Input should be a query string."
        )
    ]

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5,
        max_execution_time=60
    )
