from embedder import embed_texts
from retriever import search
from router import choose_model
from ollama_client import ask_ollama

def generate_answer(query):
    model = choose_model(query)

    query_vec = embed_texts([query])
    docs = search(query_vec, k=12)

    # separate code vs docs
    code_parts = [d for d in docs if "FILE:" in d]
    doc_parts = [d for d in docs if "FILE:" not in d]

    context = "\n\n".join(
        ["### DOCUMENTATION ###"] + doc_parts[:5] +
        ["\n### PROJECT CODE ###"] + code_parts[:5]
    )

    prompt = f"""
You are a senior DevOps + Software Engineer.

Use BOTH:
- Documentation (Docker/Kubernetes)
- Project code

Context:
{context}

Question:
{query}

Give:
- Explanation
- Code fix (if needed)
"""

    return ask_ollama(prompt, model=model)