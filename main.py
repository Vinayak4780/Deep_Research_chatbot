import os
from dotenv import load_dotenv
from graph.research_graph import build_graph

load_dotenv()

def run_system():
    graph = build_graph()  # Build once
    cache = {}  # 🔁 Cache to store previously answered questions

    while True:
        raw_input = input("🔍 Enter your research question (or type 'exit' to quit): ")
        question = raw_input.strip()

        if question.lower() in {"exit", "quit"}:
            print("👋 Exiting the system. Goodbye!")
            break

        # ✅ Check cache first
        if question in cache:
            print("⚡ Cached Result:\n")
            print("📝 Final Answer:\n", cache[question])
            continue

        # ⏳ Time the operation
        import time
        start = time.time()

        result = graph.invoke({"question": question})
        answer = result["final_answer"]
        print("📝 Final Answer:\n", answer)

        # 💾 Save to cache
        cache[question] = answer



if __name__ == "__main__":
    run_system()
