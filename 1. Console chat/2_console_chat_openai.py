import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
AI_MODEL = "gpt-4o-mini" 
BASE_URL = None 

# FROM HERE IT'S THE SAME AS THE OPEN SOURCE VERSION

def get_answer(client, conversation):
    """Sends message to the model, gets response and returns it"""
    response = client.chat.completions.create(
        model=AI_MODEL,        
        messages=conversation
    )
    answer = response.choices[0].message.content
    return answer

if __name__ == "__main__":
    SYSTEM_PROMPT = "You are a digital assistant."
   
    # Create client - connection to server running AI model
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    # Initialize conversation with system message
    conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        # Get user input and add it to conversation queue
        user_input = input("User: ")
        conversation.append({"role": "user", "content": user_input})

        # Get response, print it and add it to conversation queue
        answer = get_answer(client, conversation)
        conversation.append({"role": "assistant", "content": answer})
        
        print(f"AI: {answer}")