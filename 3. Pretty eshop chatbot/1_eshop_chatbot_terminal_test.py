"""
Terminal-based chat interface for the e-shop chatbot.
Provides interactive command-line interface for customer support interactions.
"""

from typing import NoReturn
from openai import OpenAIError
from ai_core.chatbot import Chatbot
from ai_core.models import Model
from ai_core import prompts

# Application constants
IS_OUTPUT_STREAMED = True
AI_MODEL = Model.GPT_4O_MINI

def run_eshop_chat() -> NoReturn:
    """
    Runs an interactive terminal chat session.
    
    The chat continues until the user types 'exit' or 'quit',
    or terminates the program with Ctrl+C.
    """
    chatbot = Chatbot(model=AI_MODEL, system_prompt=prompts.ESHOP_CHATBOT_SYSTEM_PROMPT)

    print("=" * 50)
    print("Jak vám můžeme pomoci? (Pro ukončení napište 'exit' nebo 'quit')")
    
    while True:
        try:
            user_input = input("Vy:  ").strip()
            
            if user_input.lower() in ('exit', 'quit'):
                print("Děkujeme za využití našeho chatbota. Na shledanou!")
                break
                
            if not user_input:
                print("Prosím zadejte zprávu.")
                continue

            print(f"Bot: ", end="", flush=True)
            try:
                if IS_OUTPUT_STREAMED:
                    ai_reply = ""
                    for token in chatbot.get_answer_streamed(user_input):
                        print(f"{token}", end="", flush=True)
                        ai_reply += token
                    print()
                else:
                    ai_reply = chatbot.get_answer(user_input)
                    print(ai_reply)
                    
            except OpenAIError as e:
                print(f"\nOmlouváme se, došlo k chybě při komunikaci: {str(e)}")
            except Exception as e:
                print(f"\nOmlouváme se, došlo k neočekávané chybě: {str(e)}")
                
        except KeyboardInterrupt:
            print("\nChat ukončen uživatelem.")
            break

if __name__ == "__main__":
    run_eshop_chat()