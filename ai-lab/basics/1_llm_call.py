import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Who is the greatest white ball captain of all time"
)
print("Response: ", response.text)
print("Metadata: ", response.usage_metadata)