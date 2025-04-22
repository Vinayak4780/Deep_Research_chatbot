from langgraph.graph import StateGraph, END
from agents.research import researcher_agent
from agents.drafter import drafter_agent
from pydantic import BaseModel

# Define the state schema
class ResearchState(BaseModel):
    question: str
    research: str = None
    final_answer: str = None

def build_graph():
    researcher = researcher_agent()
    drafter = drafter_agent()

    builder = StateGraph(ResearchState)

    # Rename node functions to avoid conflict with state keys
    def run_research(state: ResearchState) -> ResearchState:
        result = researcher.run(state.question)
        print("Research Output:\n", result)
        return state.copy(update={"research": result})


    def generate_draft(state: ResearchState) -> ResearchState:
        answer = drafter.invoke({"input": state.research})
        print("📝 Drafted Answer:\n", answer)
        return state.copy(update={"final_answer": answer})



    # Add nodes with non-conflicting names
    builder.add_node("run_research", run_research)
    builder.add_node("generate_draft", generate_draft)

    builder.set_entry_point("run_research")
    builder.add_edge("run_research", "generate_draft")
    builder.add_edge("generate_draft", END)

    return builder.compile()
