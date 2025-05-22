import json
import re
from services.gemini import generate_text, setup_gemini
import os
from dotenv import load_dotenv

load_dotenv()
model = setup_gemini(os.getenv("GEMINI_API_KEY"))

def generate_company_profile(company_name, lead_name, company_email, company_linkedin):
    prompt = f"""
    You are an intelligent assistant. A salesperson is researching a company before reaching out.

    Company name: {company_name}
    Lead: {lead_name}
    Company email: {company_email}
    Company LinkedIn: {company_linkedin}

    Based on your knowledge and public sources, create a realistic company profile in JSON format with the following fields:
    - company_name
    - industry (what kind of business is it in?)
    - company_size (small, medium, large – if unknown, guess based on name or domain)
    - headquarters_location (city, country – best guess)
    - description (what does the company do?)
    - recent_updates (funding, product launches, hiring, new branches – make reasonable assumptions)
    - website_insights (highlight the kind of services/products offered)

    Give realistic-looking, informative values. If unsure, use best guess.
    """

    response_text = generate_text(prompt, model)

    # Remove code blocks if present
    cleaned_response = re.sub(r"```json|```", "", response_text).strip()

    try:
        parsed_json = json.loads(cleaned_response)
    except json.JSONDecodeError:
        parsed_json = {"error": "Invalid JSON returned", "raw_response": response_text}

    return parsed_json
