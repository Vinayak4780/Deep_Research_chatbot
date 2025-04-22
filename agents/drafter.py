from langchain.prompts import PromptTemplate
from shared_llm import llm
def drafter_agent():
    prompt = PromptTemplate.from_template("""
  Research Question:
{input}

  You are a senior research analyst. Create a comprehensive, fact-based, and clear answer suitable for a university professor.

  Answer:
""")

    

    return prompt | llm
