import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GEMINI_API_KEY"))

# langchain is framework that is used to streamline the complex workflows 

# 1. plain call (same as script 1, through the wrapper) 
print("Plain Call: ", llm.invoke("what is kafka partition? One sentence").text)

# 2. prompt template + chain: '|' sends prompt's output to llm model
prompt = ChatPromptTemplate.from_template("Explain {topic} to a backend engineer in one sentence")
chain = prompt | llm 
print("Chain Call: ", chain.invoke({"topic": "MVCC"}).text)

# 3. structured output: get a python object back intead of plain text
class Concept(BaseModel):
    name: str
    one_line: str
    common_mistake: str

structured = llm.with_structured_output(Concept)
result = structured.invoke("Describe kafka consumer lag")
print("Structured Result: ", result)
print("Common Mistakes: ", result.common_mistake)