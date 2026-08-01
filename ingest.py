import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

visited = set()

def crawl(url, base_url, depth=2):
    if depth == 0 or url in visited:
        return []

    print(f"Crawling: {url}")
    visited.add(url)

    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator="\n")

        docs = [text]

        # find links
        for link in soup.find_all("a", href=True):
            href = link["href"]

            if href.startswith("/"):
                full_url = urljoin(base_url, href)

                if base_url in full_url:
                    docs += crawl(full_url, base_url, depth-1)

        return docs

    except Exception as e:
        print("Error:", e)
        return []


def save_docs():
    os.makedirs("data/raw", exist_ok=True)

    docker_docs = crawl(
        "https://docs.docker.com/",
        "https://docs.docker.com",
        depth=2
    )

    k8s_docs = crawl(
        "https://kubernetes.io/docs/",
        "https://kubernetes.io",
        depth=2
    )

    all_docs = docker_docs + k8s_docs

    for i, doc in enumerate(all_docs):
        with open(f"data/raw/doc_{i}.txt", "w", encoding="utf-8") as f:
            f.write(doc)


if __name__ == "__main__":
    save_docs()x
e
j
t
y
f
k
p
u
