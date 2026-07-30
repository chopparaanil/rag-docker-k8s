import os
from chunker import chunk_text
from embedder import embed_texts
from retriever import save_index
from code_ingest import load_code_files

texts = []

# 📄 Load docs
for file in os.listdir("data/raw"):
    with open(f"data/raw/{file}", encoding="utf-8") as f:
        raw = f.read()
        chunks = chunk_text(raw)
        texts.extend(chunks)

# 💻 Load project code
code_data = load_code_files()
for code in code_data:
    chunks = chunk_text(code)
    texts.extend(chunks)

print(f"Total chunks (docs + code): {len(texts)}")

vectors = embed_texts(texts)
save_index(vectors, texts)

print("✅ Combined index built!")