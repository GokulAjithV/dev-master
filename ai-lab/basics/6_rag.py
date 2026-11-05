import chromadb
from google import genai
from fastembed import TextEmbedding
from dotenv import load_dotenv

load_dotenv()
model = TextEmbedding("BAAI/bge-small-en-v1.5")
db = chromadb.Client().create_collection("facts")

# Private facts the LLM cannot know from training
facts = [
    "The payments service on-call engineer this week is Priya, phone extension 4417.",
    "Payments database connection pool size is 5.",
    "Deploys are frozen every Friday after 4 PM.",
    "The notifications service sends receipts through SendGrid.",
]

db.add(
    ids=[str(i) for i in range(len(facts))],
    documents=facts,
    embeddings=list(model.embed(facts)),
)

question = "Payments is down, who do I call?"

# 1.Retrieve 
context = db.query(query_embeddings=list(model.embed([question])), n_results=2)["documents"][0]

# 2.Augment
prompt = (
    "Answer using ONLY the context. If the answer is not there, say 'I don't know'.\n\n"
    "Context:\n" + "\n".join(context) + f"\n\nQuestion: {question}"
)

print("--------prompt sent to LLM --------\n\n" + prompt + "\n")

# 3.Generate
llm_model="gemini-3.5-flash"
client = genai.Client()
print("WITH Context: ", client.models.generate_content(model=llm_model, contents=prompt).text)
print("WITHOUT Context: ", client.models.generate_content(model=llm_model, contents=question).text)
