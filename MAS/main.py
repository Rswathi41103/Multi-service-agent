from agents.company_agent import generate_company_profile
from agents.lead_agent import generate_lead_profile
from agents.summary_agent import generate_combined_profile
from agents.pitch_agent import generate_sales_pitch
import json

def main():
    # Step 1: Input company profile details
    company_name = input("Enter the company name: ")
    company_email = input("Enter the company email ID: ")
    company_linkedin = input("Enter the company LinkedIn URL: ")
    lead_name = input("Enter the lead name: ")

    # Step 2: Generate and display company profile
    company_profile = generate_company_profile(
        company_name=company_name,
        lead_name=lead_name,  # No lead info at this point
        company_email=company_email,
        company_linkedin=company_linkedin
    )
    print("\nCompany Profile:")
    print(company_profile)
    print("\n" + "="*50 + "\n")

    # Step 3: Input lead profile details
    lead_name = input("Enter the lead name: ")
    lead_email = input("Enter the lead email ID: ")
    lead_linkedin = input("Enter the lead LinkedIn URL: ")

    # Step 4: Generate and display lead profile
    lead_profile = generate_lead_profile(
        lead_name=lead_name,
        lead_email=lead_email,
        lead_linkedin=lead_linkedin,
        company_name=company_name
    )
    print("Lead Profile:")
    print(lead_profile)
    print("\n" + "="*50 + "\n")

    # Step 5: Generate and display combined summary
    combined_summary = generate_combined_profile(
        company_name=company_name,
        lead_name=lead_name,
        lead_email=lead_email,
        lead_linkedin=lead_linkedin,
    )
    print("Summary:")
    print(json.dumps(combined_summary, indent=2))
    print("\n" + "=" * 50 + "\n")

    # Step 6: Generate and display sales pitch
    sales_pitch = generate_sales_pitch(
        company_name,
        lead_name,
        lead_email,
        lead_linkedin
    )
    print("\nSales Pitch:\n")
    print(sales_pitch)


if __name__ == "__main__":
    main()
