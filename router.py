def choose_model(query):
    q = query.lower()

    if any(word in q for word in ["code", "function", "error", "bug", "fix"]):
        return "deepseek-coder-v2"

    if any(word in q for word in ["docker", "kubernetes", "what is", "explain"]):
        return "mistral"

    return "llama3"