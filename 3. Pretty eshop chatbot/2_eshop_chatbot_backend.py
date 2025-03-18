"""
Flask backend server for the e-shop chatbot.
Provides REST API endpoints for chat functionality and bot management.
"""

from typing import Generator, Dict, Any
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from openai import OpenAIError
from ai_core import prompts
from ai_core.chatbot import Chatbot
from ai_core.models import Model

# AI model configuration
IS_OUTPUT_STREAMED = True
AI_MODEL = Model.GPT_4O_MINI

# Initialize the chatbot instance
chatbot = Chatbot(model=AI_MODEL, system_prompt=prompts.ESHOP_CHATBOT_SYSTEM_PROMPT)

# Create Flask app and enable CORS
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    """Basic index route."""
    return "Flask Chatbot Server is running."

@app.route('/chat', methods=['POST'])
def chat() -> Response:
    """
    Handle chat messages from clients.
    
    Expected JSON payload: {"user_input": "string"}
    Returns: 
        - Streaming response (text/plain) if streaming is enabled
        - JSON response {"response": "string"} otherwise
        
    Status codes:
        200: Success
        400: Invalid input
        500: Server/API error
    """
    try:
        data = request.get_json()
        if not isinstance(data, dict):
            return jsonify({"error": "Invalid request format"}), 400
            
        user_input = data.get("user_input", "").strip()
        if not user_input:
            return jsonify({"error": "No user input provided"}), 400

        if IS_OUTPUT_STREAMED:
            return Response(
                generate_stream(user_input), 
                mimetype='text/plain'
            )
        else:
            ai_reply = chatbot.get_answer(user_input)
            return jsonify({"response": ai_reply})
            
    except OpenAIError as e:
        return jsonify({"error": f"AI service error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

def generate_stream(user_input: str) -> Generator[str, None, None]:
    """Generate streaming response for chat messages."""
    try:
        for token in chatbot.get_answer_streamed(user_input):
            yield token
    except Exception as e:
        yield f"Error: {str(e)}"

@app.route('/restart', methods=['POST'])
def restart():
    """
    Endpoint for restarting the chatbot.
    Reinitializes the chatbot instance to clear the conversation history.
    """
    global chatbot
    chatbot = Chatbot(model=AI_MODEL, system_prompt=prompts.ESHOP_CHATBOT_SYSTEM_PROMPT)
    return jsonify({"message": "Chatbot has been restarted."})

if __name__ == "__main__":
    # Run the Flask server on a dynamically allocated port with mDNS service registration
    app.run(port=1122, debug=False, use_reloader=False)

