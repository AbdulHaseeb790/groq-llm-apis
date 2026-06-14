from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()

chat_history = []

questions = [
    "What is AI?",
    "What is machine learning?",
    "What is deep learning?"
]

for question in questions:
    chat_history.append({"role": "user", "content": question})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=chat_history
    )
    
    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})
    
    print(f"Q: {question}")
    print(f"Input tokens: {response.usage.prompt_tokens}")
    print(f"Output tokens: {response.usage.completion_tokens}")
    print(f"Total tokens: {response.usage.total_tokens}")
    print("---")