from rag import generate_answer

while True:
    query = input("Ask: ")

    if query == "exit":
        break

    answer = generate_answer(query)
    print("\n💡 Answer:\n", answer)