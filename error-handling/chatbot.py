from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client=Groq()
chat_history=[]
print("chatbot ready! type 'quit' to exit")
print("---")
while True:
    user_input=input('you:')
    if user_input.lower()=='quit':
        print("bye!")
        break
    if len(chat_history) > 10:
        chat_history = chat_history[-10:]
    chat_history.append({'role':'user','content':user_input})

    try:
        response=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=chat_history
        )
        reply=response.choices[0].message.content
        chat_history.append({"role":'assistant','content':reply})
        print(f"bot:{reply}")
        print(f"[Tokens used: {response.usage.total_tokens}]")
        print("---")
    except groq.AuthenticationError:
        print("bad API key")
        break
    except groq.RateLimitError:
        print("too many request pls slow down ")
    except Exception as e:
        print(f"someelse type error:{e}")
           
