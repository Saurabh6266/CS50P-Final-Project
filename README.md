# RESUME GENERATOR

#### Video Demo: https://youtu.be/S-89j3UQ_pk

#### Description:

Resume Generator is a command-line based Python application designed to help users easily generate professional-looking PDF resumes by answering
a series of prompts. This was developed as the final project for the CS50P (CS50’s Introduction to Programming with Python) course. The project
utilizes several libraries to handle input validation, formatting, PDF generation, and more, offering a smooth interactive experience.

The project starts by collecting basic personal information such as the user’s name, phone number, and email address. The program uses the
`phonenumbers` and `validators` libraries to ensure that the data entered is accurate and properly formatted. Optional fields like LinkedIn and
GitHub profile URLs are also supported.

Once the personal data is collected, the user can select the sections they wish to include in their resume from a predefined list. These sections
include:

- Career Objective
- Education
- Skills
- Experience
- Projects
- Certifications
- Achievements

Each section is filled interactively. For instance, if the user chooses to add education details, they’ll be prompted to enter the degree,
institution, and graduation year for each entry. Similarly, for skills, a CSV file (`skills.csv`) provides predefined categories such as
Programming Languages, Libraries, Frameworks, Tools, and Soft Skills to make the input process easier and more consistent. Another CSV file
(`sections_name.csv`) lists all available sections and their serial numbers for user selection.

After all data is collected, the resume is rendered using the `fpdf` library. The layout is clean and structured, with headers, spacing, and
indentation carefully handled. Every section is displayed based on the order the user selects them.

Finally, the user is asked to name their PDF file, and the resume is saved with that filename. Upon successful creation, a message rendered using
`pyfiglet` confirms the completion.

---

### 🗂️ Project Structure

- **project.py**: The main Python script. It contains all logic to interact with the user, validate input, collect data, and generate the final
PDF resume.
- **sections_name.csv**: A CSV file containing the list of available resume sections along with serial numbers for user selection.
- **skills.csv**: A CSV file with skill categories and options that help guide the user when entering skills.

---

### 🔍 Design Decisions

One key decision was to keep the interface entirely in the command-line to maintain simplicity and cross-platform compatibility. The use of CSV
files for sections and skills was intentional — it decouples content from code, making it easier to expand the tool in the future (e.g., adding
more skill categories or sections without changing the script).

The resume is generated in PDF using `fpdf` because it offers sufficient layout control while keeping dependencies minimal. Instead of relying on
templates, the code dynamically lays out each section based on user input. The formatting prioritizes clarity and readability over visual
complexity.

Error handling was emphasized to ensure a smooth experience. For example, incorrect phone numbers or emails are flagged, and prompts continue
until valid data is entered. This ensures that the final resume does not include erroneous information.

---

### 🛠️ Future Improvements

Some ideas for future enhancement include:
- Adding support for saving and re-editing drafts.
- Creating a graphical interface using `tkinter`.
- Providing customizable templates and themes.
- Exporting to `.docx` in addition to `.pdf`.

---

### 📌 How to Run

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
