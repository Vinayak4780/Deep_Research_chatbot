# shared_llm.py
from langchain.llms import LlamaCpp

llm = LlamaCpp(
    model_path="/home/ubuntu/ChatBot/project_dseu/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=8152,
    max_tokens=512,
    temperature=0.3,
    n_gpu_layers=33  # Adjust as per your GPU memory
)
