import google.generativeai as genai

def setup_gemini(api_key: str):
    """
    Configures and returns the Gemini 1.5 Pro text model.
    """
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('models/gemini-2.0-flash')

def generate_text(prompt: str, model):
    """
    Generates a response using the provided prompt and Gemini model.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating content: {e}"

