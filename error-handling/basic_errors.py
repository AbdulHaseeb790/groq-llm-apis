from dotenv import load_dotenv
from groq import Groq
import groq

load_dotenv()

client = Groq()

try:
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":"hello"}
        ]
    )
    print(response.choices[0].message.content)


except groq.AuthenticationError as e:
    print(f"Bad API key: {e}")

except groq.RateLimitError as e:
    print(f"Too many requests, slow down: {e}")

except groq.BadRequestError as e:
    print(f"Bad request: {e}")

except groq.NotFoundError as e:
    print(f"Model not found: {e}")
except groq.APIConnectionError as e:
    print(f"Network error, check your internet: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
