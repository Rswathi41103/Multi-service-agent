import json
from agents.company_agent import generate_company_profile
from agents.lead_agent import generate_lead_profile
from agents.summary_agent import generate_combined_profile
from agents.pitch_agent import generate_sales_pitch
import re

def get_single_line_json_input(prompt_title):
    print(f"\n📌 {prompt_title}")
    input_str = input("Enter JSON input in single line:\n")
    try:
        return json.loads(input_str)
    except json.JSONDecodeError:
        print("❌ Invalid JSON format. Please try again.")
        return None

def main():
    # Step 1: Get company details (single line JSON)
    company_data = None
    while company_data is None:
        company_data = get_single_line_json_input("Step 1: Enter company and initial lead details JSON:")

    company_profile = generate_company_profile(
        company_name=company_data["company_name"],
        lead_name=company_data["lead_name"],
        company_email=company_data["company_email"],
        company_linkedin=company_data["company_linkedin"]
    )
    print("\nCompany Profile:")
    print(json.dumps(company_profile, indent=2))
    print("\n" + "=" * 60 + "\n")

    # Step 2: Get lead details (single line JSON)
    lead_data = None
    while lead_data is None:
        lead_data = get_single_line_json_input("Step 2: Enter lead details JSON:")

    lead_profile = generate_lead_profile(
        lead_name=lead_data["lead_name"],
        lead_email=lead_data["lead_email"],
        lead_linkedin=lead_data["lead_linkedin"],
        company_name=company_data["company_name"]
    )
    print("\n Lead Profile:")
    if isinstance(lead_profile, str):
        cleaned_lead_profile = re.sub(r"json|", "", lead_profile).strip()
        try:
            lead_profile_json = json.loads(cleaned_lead_profile)
            print(json.dumps(lead_profile_json, indent=2))
        except json.JSONDecodeError:
            print("⚠ Could not parse lead profile JSON correctly.")
            print(cleaned_lead_profile)
    else:
        print(json.dumps(lead_profile, indent=2))

    print("\n" + "=" * 60 + "\n")

    # Step 3: Combined summary
    combined_summary = generate_combined_profile(
        company_name=company_data["company_name"],
        lead_name=lead_data["lead_name"],
        lead_email=lead_data["lead_email"],
        lead_linkedin=lead_data["lead_linkedin"]
    )
    print("Summary:")
    print(json.dumps(combined_summary, indent=2))
    print("\n" + "=" * 60 + "\n")

    # Step 4: Sales pitch
    sales_pitch = generate_sales_pitch(
        company_name=company_data["company_name"],
        lead_name=lead_data["lead_name"],
        lead_email=lead_data["lead_email"],
        lead_linkedin=lead_data["lead_linkedin"]
    )
    print(" Sales Pitch:\n")
    print(sales_pitch)


if __name__ == "__main__":
    main()
