import os
from services.gemini import generate_text
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_lead_profile(lead_name, lead_email, lead_linkedin, company_name):
    prompt = f"""
    You are an intelligent assistant helping a salesperson understand a potential lead.

    Lead Information:
    - Name: {lead_name}
    - Email: {lead_email}
    - LinkedIn: {lead_linkedin}
    - Company: {company_name}

    Generate a JSON object with the following fields:
    - name
    - email
    - linkedin
    - current_position
    - company_name
    - seniority_level (Junior, Mid, Senior, Executive)
    - past_companies (list)
    - education (institute and year if possible)
    - is_decision_maker (Yes/No/Maybe)
    - insights (a few bullet points about the lead)

    If you cannot find exact details, make an educated guess based on the name and LinkedIn.
    """

    response = model.generate_content(prompt)
    return response.text.strip()
