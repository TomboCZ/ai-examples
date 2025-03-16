import config
from flask import Flask, request, jsonify, Response
from flask_cors import CORS  # Import CORS
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
def chat():
    """
    Endpoint for handling chat messages.
    Accepts a JSON payload with a 'user_input' field.
    If streaming is enabled, returns a streaming response (text/plain).
    Otherwise, returns a JSON response with the complete answer.
    """
    data = request.get_json()
    user_input = data.get("user_input", "")
    if not user_input:
        return jsonify({"error": "No user input provided"}), 400

    if IS_OUTPUT_STREAMED:
        def generate():
            collected_tokens = ""
            # Stream tokens from the chatbot
            for token in chatbot.get_answer_streamed(user_input):
                collected_tokens += token
                yield token
        # Return streaming response with plain text mimetype
        return Response(generate(), mimetype='text/plain')
    else:
        ai_reply = chatbot.get_answer(user_input)
        return jsonify({"response": ai_reply})

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

