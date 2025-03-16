from openai import OpenAI

API_KEY = "non_empty_string"
AI_MODEL = "llama-3.2-3b-instruct-q8_0"
BASE_URL = "http://127.0.0.1:1234/v1"

def get_answer(client, conversation):
    """Sends message to the model, gets response and returns it"""
    response = client.chat.completions.create(
        model=AI_MODEL,
        max_tokens=50,
        messages=conversation
    )
    answer = response.choices[0].message.content
    return answer

if __name__ == "__main__":
    SYSTEM_PROMPT = "You are a helpful assistant."
   
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