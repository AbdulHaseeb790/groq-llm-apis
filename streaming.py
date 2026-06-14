import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

stream = client.chat.completions.create(
    model='llama-3.3-70b-versatile',
    messages=[
        {"role": "user", "content": "explain machine learning in detail"}
    ],
    max_tokens=300,
    temperature=0.7,
    stream=True
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)

print()