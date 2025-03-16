import os
from llama_cpp import Llama

MODEL_PATH = "./local_models/llama-3.2-3b-instruct-q8_0.gguf"

if __name__ == "__main__":
    prompt = "Hello, how are you?"

    # Create client with local inference directly in application, no server needed
    llm = Llama(model_path=MODEL_PATH, verbose=False)
    
    try:
        # Create single shot: response to our prompt and end
        response = llm(prompt, max_tokens=50)
        
        # Extract clean text response from response object
        answer = response["choices"][0]["text"]
        print(answer)
    finally:
        # Ensure resources are properly released
        llm.close()
