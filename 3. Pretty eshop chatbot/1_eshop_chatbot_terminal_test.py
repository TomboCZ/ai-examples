import config
from openai import OpenAI
from ai_core.chatbot import Chatbot
from ai_core.models import Model
from ai_core import prompts

def run_eshop_chat():
    """
    Runs an interactive terminal chat session.
    """
    # AI model configuration
    IS_OUTPUT_STREAMED = True
    AI_MODEL = Model.GPT_4O_MINI

    chatbot = Chatbot(model=AI_MODEL, system_prompt=prompts.ESHOP_CHATBOT_SYSTEM_PROMPT)

    print("=" * 50)
    print("Jak vám můžeme pomoci?")
    
    while True:
        user_input = input("Vy:  ")      
        ai_reply = ""

        if IS_OUTPUT_STREAMED:  
            print(f"Bot: ", end="")
            for token in chatbot.get_answer_streamed(user_input):
                print(f"{token}", end="")
                ai_reply += token
            print()
        else:       
            ai_reply = chatbot.get_answer(user_input)
            print(f"Bot: {ai_reply}")

# Example usage
if __name__ == "__main__":
    run_eshop_chat()