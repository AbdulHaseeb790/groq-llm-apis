import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))
chat_history = [
    {"role":"system","content":"You are a Pakistani assistant who mixes Urdu and English"}
]
while True:
    user_input=input("you:")
    if user_input=='exit':
        exit()
   
    chat_history.append({"role":"user","content":user_input})
   
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        messages=chat_history
    )
    
    assistant_reply=response.choices[0].message.content
    chat_history.append({'role':'assistant','content':assistant_reply})
    print(f"Assistant: {assistant_reply}")