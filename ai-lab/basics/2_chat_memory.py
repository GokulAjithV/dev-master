import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()
MODEL = "gemini-2.5-flash"
content_1 = "My name is Gokul Ajith, Say hi in five words"
content_2 = "What is my name"

first = client.models.generate_content(
    model=MODEL,
    contents=content_1
)
print("call 1: ", first.text)

second = client.models.generate_content(
    model=MODEL,
    contents=content_2
)
print("call 2: ", second.text)

history = [
    {"role": "user", "parts": [{"text": content_1}]},
    {"role": "model", "parts": [{"text": first.text}]},
    {"role": "user", "parts": [{"text": content_2}]}
]

third = client.models.generate_content(
    model=MODEL,
    contents=history
)
print("call 3: ", third.text)