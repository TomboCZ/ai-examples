from openai import OpenAI

API_KEY = "non_empty_string"
BASE_URL = "http://127.0.0.1:1234/v1"

def solve_any_problem(problem, ai_model):
    SYSTEM_PROMPT = """
    You are an expert in solving logical and mathematical problems.
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
    problem = "How many letters 'r' are there in the word 'strawberry'?"
    print(problem)
           
    print("\nDeepSeek R1:")
    solution_reasoning = solve_any_problem(problem, "deepseek-r1-distill-llama-8b")
    print(solution_reasoning)

