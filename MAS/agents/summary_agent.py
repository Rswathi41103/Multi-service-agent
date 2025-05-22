import json
import re
import os
from dotenv import load_dotenv
from services.gemini import generate_text, setup_gemini
from agents.company_agent import generate_company_profile
from agents.lead_agent import generate_lead_profile

load_dotenv()
model = setup_gemini(os.getenv("GEMINI_API_KEY"))  # Initialize once

def generate_combined_profile(company_name, lead_name, lead_email, lead_linkedin):
    company_profile = generate_company_profile(company_name, lead_name, lead_email, lead_linkedin)
    lead_profile = generate_lead_profile(lead_name, lead_email, lead_linkedin, company_name)

    summary_prompt = f"""
You are an expert assistant that combines company and lead profiles into a concise report.

Company profile:
{json.dumps(company_profile, indent=2)}

Lead profile:
{json.dumps(lead_profile, indent=2)}

Task:
1. Highlight the 5 most important facts or insights from both profiles.
2. Write a short, clear summary for a salesperson preparing for a call.

Return the response as a JSON with keys:
- "highlights": list of strings
- "summary": a concise string

Only return valid JSON without any markdown or code blocks.
"""

    response_text = generate_text(summary_prompt, model)

    cleaned_response = re.sub(r"```json|```", "", response_text).strip()

    try:
        parsed_json = json.loads(cleaned_response)
    except json.JSONDecodeError:
        parsed_json = {"error": "Invalid JSON returned", "raw_response": response_text}

    return parsed_json
