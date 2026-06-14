import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

try:
    response = client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {"role": "user", "content": "what is artificial intelligence?"}
        ],
        max_tokens=200
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")