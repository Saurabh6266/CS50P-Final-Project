import csv
import tabulate
import validators
import phonenumbers
from fpdf import FPDF
from pyfiglet import Figlet


def main():
    name, phone_number, email_id = get_personal_info()

    data = {
        "name": name,
        "phone_number": phone_number,
        "email_id": email_id,
    }

    linkedin_id = get_linkedin()
    github_profile = get_github()

    if linkedin_id:
        data["linkedin_id"] = linkedin_id

    if github_profile:
        data["github_profile"] = github_profile

    get_professional_info(data)


def get_personal_info():
    while True:
        name = input("What's your name? ").strip()

        if name:
            break

        print("Name cannot be empty!\n")

    while True:
        phone_number = input("\nWhat's your phone number? ").strip()

        try:
            parsed_number = phonenumbers.parse(phone_number, "IN")

            if phonenumbers.is_valid_number(parsed_number):
                phone_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                break
            else:
                print("Invalid phone number!")
        except phonenumbers.NumberParseException:
            print("Invalid phone number format!")

    while True:
        email_id = input("\nWhat's your email address? ").strip()

        if validators.email(email_id):
            break

        print("Invalid email address!")

    return name, phone_number, email_id


def get_linkedin():
    while True:
        response = input("\nDo you want to add your LinkedIn ID? Please enter 'yes' or 'no'. ").strip().lower()

        if response in ['yes', 'no']:
            break

        print("Please enter a valid response: 'yes' or 'no'.")

    linkedin_id = ''

    if response == 'yes':
        linkedin_id = input("What's your LinkedIn ID URL? ").strip()

    return linkedin_id


def get_github():
    while True:
        response = input("\nDo you want to add your github profile? Please enter 'yes' or 'no'. ").strip().lower()

        if response in ['yes', 'no']:
            break

        print("Please enter a valid response: 'yes' or 'no'.")

    github_profile = ''

    if response == 'yes':
        github_profile = input("What's your github profile URL? ").strip()

    return github_profile


def get_professional_info(data):
    with open("sections_name.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        headers = rows[0]
        sections = rows[1:]

    print("\nEnter the serial number of the section you want to include in your resume.")
    print("Enter one by one in the order you want.")
    print("Type 'done' when you're finished.")

    serial_nos = []

    while True:
        print()
        print(tabulate.tabulate(sections, headers, tablefmt='grid'))

        serial_no = input("Serial Number: ").strip()

        if serial_no == 'done':
            break

        if serial_no == "1":
            data["summary"] = input("\nEnter your career objective or summary: ").strip()
        elif serial_no == "2":
            data["education"] = []

            while True:
                try:
                    edu_count = int(input("\nNumber of educational qualifications: "))
                    if edu_count <= 0:
                        raise ValueError("It must be a postive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid number.")

            for _ in range(edu_count):
                degree = input("Degree: ").strip()
                institution = input("Institution: ").strip()
                year = input("Year: ").strip()
                data["education"].append({"degree": degree, "institution": institution, "year": year})
        elif serial_no == "3":
            data["skills"] = []

            with open("skills.csv", "r") as file:
                reader = csv.reader(file)
                skills_rows = list(reader)
                heading = skills_rows[0]
                skills_list = skills_rows[1:]

            print("\nEnter the serial number of the skill you want to include in your resume.")
            print("Enter one by one in the order you want.")
            print("Type 'done' when you're finished.")

            while True:
                print()
                print(tabulate.tabulate(skills_list, heading, tablefmt='grid'))

                skill_serial_no = input("Serial Number: ").strip()

                if skill_serial_no == 'done':
                    break

                if skill_serial_no == "1":
                    programming_languages = input("\nProgramming Languages (comma separated): ").strip()
                    data["skills"].append({"Programming Languages": programming_languages})
                elif skill_serial_no == "2":
                    library = input("\nLibrary (comma separated): ").strip()
                    data["skills"].append({"Library": library})
                elif skill_serial_no == "3":
                    frameworks = input("\nFrameworks (comma separated): ").strip()
                    data["skills"].append({"Frameworks": frameworks})
                elif skill_serial_no == "4":
                    tools = input("\nTools (comma separated): ").strip()
                    data["skills"].append({"Tools": tools})
                elif skill_serial_no == "5":
                    soft_skills = input("\nSoft Skills (comma separated): ").strip()
                    data["skills"].append({"Soft Skills": soft_skills})
                else:
                    print("\nInvalid serial number. Please enter again.")
        elif serial_no == "4":
            data["experience"] = []

            while True:
                try:
                    exp_count = int(input("\nNumber of working experience entries: "))
                    if exp_count <= 0:
                        raise ValueError("It must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid number.")

            for _ in range(exp_count):
                company = input("Company: ").strip()
                job_title = input("Job Title: ").strip()
                duration = input("Duration (e.g., Jan 2020 - Dec 2021): ").strip()
                description = input("Description of your role: ").strip()
                data["experience"].append(
                    {
                        "company": company,
                        "job_title": job_title,
                        "duration": duration,
                        "description": description,
                    }
                )
        elif serial_no == "5":
            data["projects"] = []

            while True:
                try:
                    count = int(input("\nNumber of projects you want to include in your resume: "))
                    if count <= 0:
                        raise ValueError("It must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid number.")

            for _ in range(count):
                project_name = input("Project Name: ").strip()
                technologies_used = input("Technologies used (comma separated): ").strip()
                description = input("Description of the project: ").strip()
                data["projects"].append(
                    {
                        "project_name": project_name,
                        "technologies_used": technologies_used,
                        "description": description,
                    }
                )
        elif serial_no == "6":
            data["certifications"] = []

            while True:
                try:
                    count = int(input("\nNumber of certificates you want to include: "))
                    if count <= 0:
                        raise ValueError("It must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid number.")

            for _ in range(count):
                certificate_name = input("Certificate Name: ").strip()
                issuing_organization = input("Issuing Organization: ").strip()
                year = input("Year of issue: ").strip()
                data["certifications"].append(
                    {
                        "certificate_name": certificate_name,
                        "issuing_organization": issuing_organization,
                        "year": year
                    }
                )
        elif serial_no == "7":
            data["achievements"] = []

            while True:
                try:
                    count = int(input("\nNumber of achievements: "))
                    if count <= 0:
                        raise ValueError("It must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid number.")

            print("Please enter your achievements in a single sentence format.")

            for _ in range(count):
                achievement = input("Achievement: ").strip()
                data["achievements"].append(achievement)
        else:
            print("\nInvalid serial number. Please enter a valid serial number.")
            continue

        serial_nos.append(serial_no)

    generate_pdf(data, serial_nos)


def generate_pdf(data, serial_nos):
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, data['name'], ln=True, align="C")

    contact_info = f"{data['phone_number']} | {data['email_id']}"

    if "linkedin_id" in data:
        contact_info += f" | {data['linkedin_id']}"

    if "github_profile" in data:
        contact_info += f" | {data['github_profile']}"

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 9, contact_info, ln=True, align="C")

    pdf.ln(7)

    for serial_no in serial_nos:
        if serial_no == "1":
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 7, "Career Objective", ln=True)

            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 8, data['summary'])

            pdf.ln(5)

        elif serial_no == "2":
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 7, "Education", ln=True)

            for edu in data['education']:
                pdf.set_font("Arial", "B", 13)
                pdf.cell(150, 8, edu['institution'], align="L")

                pdf.set_font("Arial", size=12)
                pdf.cell(0, 7, edu['year'], align="R", ln=True)
                pdf.cell(0, 7, edu['degree'], ln=True)

            pdf.ln(5)

        elif serial_no == "3":
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 7, "Skills", ln=True)

            i = 1

            pdf.set_font("Arial", size=12)
            for skill in data['skills']:
                for key, value in skill.items():
                    pdf.cell(0, 8, f"{i}. {key}: {value}", ln=True)

                    i += 1

            pdf.ln(5)

        elif serial_no == "4":
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 7, "Experience", ln=True)

            for exp in data['experience']:
                pdf.set_font("Arial", "B", 12)
                pdf.cell(150, 8, exp['company'], align="L")

                pdf.set_font("Arial", size=12)
                pdf.cell(0, 7, exp['duration'], align="R", ln=True)

                pdf.cell(0, 7, exp['job_title'], ln=True)

                pdf.set_left_margin(15)
                pdf.set_x(15)
                pdf.multi_cell(0, 7, f"-{exp['description']}")
                pdf.set_left_margin(10)
                pdf.set_x(10)

            pdf.ln(5)

        elif serial_no == "5":
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 7, "Projects", ln=True)

            for project in data['projects']:
                pdf.set_font("Arial", size=13)
                pdf.cell(0, 8, f"{project['project_name']} | {project['technologies_used']}", ln=True)

                pdf.set_font("Arial", size=12)

                pdf.set_left_margin(15)
                pdf.set_x(15)
                pdf.multi_cell(0, 7, f"-{project['description']}")
                pdf.set_left_margin(10)
                pdf.set_x(10)

            pdf.ln(5)

        elif serial_no == "6":
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 7, "Certifications", ln=True)

            pdf.set_font("Arial", size=12)
            for certificate in data['certifications']:
                pdf.cell(0, 8, f"{certificate['certificate_name']} | {certificate['issuing_organization']}, {certificate['year']}", ln=True)

            pdf.ln(5)

        else:
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 7, "Achievements", ln=True)

            pdf.set_font("Arial", size=12)
            for achievement in data['achievements']:
                pdf.multi_cell(0, 8, f"-{achievement}")

    file_name = input("\nEnter the name of the file for your resume (without extension): ").strip()

    pdf.output(f"{file_name}.pdf")

    figlet = Figlet()
    print(figlet.renderText("Your resume is successfully created!"))


if __name__ == "__main__":
    figlet = Figlet()

    print("Hello, World!")
    print(figlet.renderText("Resume Generator"))
    main()
