from fastembed import TextEmbedding

model = TextEmbedding("BAAI/bge-small-en-v1.5")

sentences = [
    "the database ran our of connections",
    "connection pool exhausted",
    "my phone connection keeps dropping"
]


vectors = list(model.embed(sentences))

print("numbers per sentence: ", len(vectors[0]))
print("first 5 numbers: ", vectors[0][:5])

print("s0 vs s1: ", round(float(vectors[0] @ vectors[1]), 2))
print("s0 vs s1: ", round(float(vectors[0] @ vectors[2]), 2))
