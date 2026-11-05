from fastembed import TextEmbedding
import chromadb

model = TextEmbedding("BAAI/bge-small-en-v1.5")
notes = chromadb.Client().create_collection("notes")

docs = [
    "Consumers in one group split the partitions",
    "A rebalance happens when a consumer joins or leaves",
    "MVCC lets Postgres readers avoid blocking writers",
    "VACUUM cleans up dead row versions in Postgres",
]
notes.add(
    ids=["1", "2", "3", "4"],
    documents=docs,
    embeddings=list(model.embed(docs)),
    metadatas=[{"topic": "kafka"}, {"topic": "kafka"}, {"topic": "postgres"}, {"topic": "postgres"}]
)

q = list(model.embed(["what if a consumer dies"]))
result = notes.query(query_embeddings=q, n_results=2, where={"topic": "kafka"})["documents"]
print("result:", result)
