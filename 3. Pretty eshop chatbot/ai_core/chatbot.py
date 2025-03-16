import os
from openai import OpenAI
from ai_core import prompts
from ai_core.models import Model

class Chatbot:
    def __init__(self, model: Model, system_prompt: str = prompts.GENERIC_SYSTEM_PROMPT):
        """
        Initializes the Chatbot instance.
        Args:
            model (str): The name of the model to be used.
            is_opensource (bool): Flag indicating if the model is open-source.
            system_prompt (str, optional): The initial system prompt for the chatbot. Defaults to "You are a helpful assistant.".
            api_key (str): The API key for accessing the OpenAI service.
            base_url (str, optional): The base URL for the OpenAI service. Defaults to None.
        """
 
        self.model = model.exact_name
        self.is_opem_source = model.is_open_source
        self.api_key = "non-empty-string" if self.is_opem_source else os.getenv("OPENAI_API_KEY")
        self.base_url = "http://localhost:1234/v1" if self.is_opem_source else None
        self.system_prompt = system_prompt

        # Initialize the OpenAI client
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        
        # Determine the system prompt role based on the model type
        self.system_prompt_role_name = "system" if self.is_opem_source else "developer"
        
        # Initialize conversation history with the system prompt
        self.messages = [{"role": self.system_prompt_role_name, "content": self.system_prompt}]

    def get_answer(self, user_input: str) -> str:
        """
        Add the user's input to the conversation history, send a request to the AI model,
        and return the response.
        
        :param user_input: User's input message.
        :return: AI's response message.
        """
        self.messages.append({"role": "user", "content": user_input})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        
        ai_reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": ai_reply})
        
        return ai_reply
    
    def get_answer_streamed(self, user_input: str):
        """
        Appends the user's input to the conversation history, sends a request to the AI model with streaming enabled,
        and yields tokens as they are received.
        
        Based on the Streaming documentation: https://platform.openai.com/docs/api-reference/streaming
        
        :param user_input: The user's message.
        :yield: Tokens of the response.
        """
        self.messages.append({"role": "user", "content": user_input})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=True  # Enable streaming of the response
        )
        
        collected_tokens = ""
        for chunk in response:
            # Instead of using .get(), check if 'content' attribute exists
            delta = chunk.choices[0].delta
            token = delta.content if hasattr(delta, 'content') and delta.content is not None else ""
            collected_tokens += token
            yield token
        
        # Append the complete response to the conversation history
        self.messages.append({"role": "assistant", "content": collected_tokens})
