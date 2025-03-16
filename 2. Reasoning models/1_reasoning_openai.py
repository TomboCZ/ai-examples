import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = None 

def solve_any_problem(problem, ai_model):
    SYSTEM_PROMPT = """
    Jsi expert na řešení logických a matematických problémů.
    """
    
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    conversation = [{"role": "system", "content": SYSTEM_PROMPT}]
    conversation.append({"role": "user", "content": problem})

    response = client.chat.completions.create(
        model=ai_model,
        messages=conversation
    )
    answer = response.choices[0].message.content
    return answer

if __name__ == "__main__":
    problem = "How many letters 'r' are there in the word 'strawberry'?."
    print(problem)
           
    print("\n4o-mini:")
    solution_classic = solve_any_problem(problem, "gpt-4o-mini")
    print(solution_classic)

    print("\no3-mini:")
    solution_reasoning = solve_any_problem(problem, "o3-mini")
    print(solution_reasoning)

