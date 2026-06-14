from dotenv import load_dotenv
from groq import Groq
import groq
import time

load_dotenv()

client = Groq()

def call_with_retry(messages, max_retries=3):
    wait_time = 1
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages
            )
            return response.choices[0].message.content
        
        except groq.RateLimitError:
            if attempt < max_retries - 1:
                print(f"Rate limited! Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                wait_time *= 2
            else:
                print("Max retries reached. Giving up.")
                return None

result = call_with_retry([{"role": "user", "content": "Hello!"}])
print(result)