# AI Development Course

Modern AI integration course focused on practical implementation using both OpenAI and open-source models.

## Quick Start

### Clone Repository and Setup Virtual Environment
- git clone https://github.com/TomboCZ/ai-examples
- python -m venv .venv
- source .venv/bin/activate  # Mac/Linux
- .\.venv\Scripts\activate   # Windows

### Install Dependencies
- pip install -r requirements.txt

### Configure API Keys
- cp .env-example .env
- Edit .env with your API key

### LM Studio Setup
- Visit [LM Studio](https://lmstudio.ai) to download and install.
- Load these models:
  - llama-3.2-3b-instruct-q8_0
  - deepseek-r1-distill-llama-8b

### Download Model for Local llama.cpp Inference
Before testing local inference with llama.cpp, download the model "llama-3.2-3B-Instruct-Q8_0.gguf" file from 
[Hugging Face](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/blob/main/Llama-3.2-3B-Instruct-Q8_0.gguf)
and place it into the `local_models` folder.



