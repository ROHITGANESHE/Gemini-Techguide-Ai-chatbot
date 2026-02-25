import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables securely
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

# Configure the API
genai.configure(api_key=api_key)

# Advanced Prompt Engineering: Define the persona and rules
SYSTEM_PROMPT = """
You are 'TechGuide', an expert AI assistant specializing in Cloud Computing and Software Engineering. 
Rules:
1. Provide concise, highly technical, and accurate answers.
2. If asked about non-tech topics (like cooking or sports), politely decline and steer the conversation back to technology.
3. Always structure complex answers with bullet points or numbered lists.
4. If writing code, always include brief comments explaining the logic.
"""

def initialize_gemini_chat():
    """Initializes the model with system instructions and returns a chat session object for memory."""
    # Using gemini-1.5-flash as it is fast and supports system instructions
    model = genai.GenerativeModel(
        model_name="gemini-3-flash-preview",
        system_instruction=SYSTEM_PROMPT,
        generation_config={
            "temperature": 0.4, # Lower temperature for more deterministic/factual responses
            "top_p": 0.95,
            "max_output_tokens": 1024,
        }
    )
    
    # start_chat() automatically handles multi-turn conversation memory
    chat_session = model.start_chat(history=[])
    return chat_session