from fastembed import TextEmbedding

model = TextEmbedding("BAAI/bge-small-en-v1.5")

docs = [
    "Kafka consumers in the same group split the partitions between them",
    "Postgres uses MVCC so readers do not block writers",
    "A rebalance moves partitions when a consumer joins or leaves",
    "FastAPI runs sync endpoints in a threadpool",
    "An index speeds up reads but slows down writes",
]

doc_vectors = list(model.embed(docs))

question = "what happens when a kafka consumer crashes?"
q = list(model.embed(question))[0]

scores = [(q @ d, text) for d, text in zip(doc_vectors, docs)]

print("Question: ", question)
for score, text in sorted(scores, reverse=True):
    print(f"{score:.2f} - {text}")