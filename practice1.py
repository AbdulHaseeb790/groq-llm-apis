import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))
try:
    response=client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {"role":"user","content":"what is a machine learning"}
        ],
        max_tokens=200,
        temperature=1.0
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"error{e}")


