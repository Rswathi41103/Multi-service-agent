import json
import re
from services.gemini import generate_text, setup_gemini
import os
from dotenv import load_dotenv
from agents.company_agent import generate_company_profile
from agents.lead_agent import generate_lead_profile

load_dotenv()
model = setup_gemini(os.getenv("GEMINI_API_KEY"))

def generate_sales_pitch(company_name, lead_name, lead_email, lead_linkedin):
    # First, generate company and lead profiles
    company_profile = generate_company_profile(company_name, lead_name, lead_email, lead_linkedin)
    lead_profile = generate_lead_profile(lead_name, lead_email, lead_linkedin, company_name)

    # Build the prompt for generating the pitch
    pitch_prompt = f"""
    You are an expert sales assistant helping to craft a persuasive and personalized sales pitch.

    Company profile:
    {json.dumps(company_profile, indent=2)}

    Lead profile:
    {json.dumps(lead_profile, indent=2)}

Based on these profiles, create a professional sales pitch email to {lead_name} that:
- Highlights key benefits of our product/service relevant to their company and role.
- Addresses potential pain points or needs suggested by the profiles.
- Is concise, clear, and engaging.
- Ends with a strong call to action for a meeting or demo.

Return ONLY the sales pitch text as plain text (no JSON, no markdown, no code blocks).
"""

    response_text = generate_text(pitch_prompt, model)

    # Clean any accidental code blocks or markdown if present
    cleaned_response = re.sub(r"```.*?```", "", response_text, flags=re.DOTALL).strip()

    return cleaned_response
