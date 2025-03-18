import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = None 
AI_MODEL = "gpt-4o-mini"

def solve_vision(ai_model, system_prompt, prompt, image_path):
    # Create client for API
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    
    # Load image and encode to Base64
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode("utf-8")
    
    # Construct messages with multimodal input: system message + user message containing text and image
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": "data:image/png;base64," + base64_image, "detail": "low"}}
            ]
        }
    ]
    
    # Send request to chat completions endpoint with GPT-4o mini model
    response = client.chat.completions.create(
        model=ai_model,
        messages=messages,
    )
    
    # Extract text description from response
    answer = response.choices[0].message.content
    return answer

def get_file_path(filename):
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

if __name__ == "__main__":
    SYSTEM_PROMPT = """
    You are a world-class film scene analyst and visual expert with decades of experience in cinematography and film history. 
    Your specialty is recognizing movie scenes, analyzing their composition, lighting, and identifying specific movies, actors, and directors.
    Focus on:
    - Identifying the movie if possible
    - Key visual elements and composition
    - Notable actors or characters
    - Distinctive cinematographic features
    Be concise and precise in your analysis.
    """
    
    PROMPT = """
    1. Provide a description of the entire scene.
    2. Present a table of characters with their descriptions.
    3. Briefly describe the relationships between the characters.
    4. Carefully reconsider all the gathered information and, based on that, determine the title of the film.
    """
    
    image_file = get_file_path("test-bar.png")
    scene_analysis = solve_vision(AI_MODEL, SYSTEM_PROMPT, PROMPT, image_file)
    print(scene_analysis)

