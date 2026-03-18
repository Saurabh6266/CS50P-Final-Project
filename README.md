# 📄 Resume Generator

### A CLI-Based PDF Resume Builder | CS50P Final Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![CS50P](https://img.shields.io/badge/CS50P-Final%20Project-crimson?logo=edx&logoColor=white)
![pytest](https://img.shields.io/badge/Tested%20with-pytest-brightgreen?logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

**Video Demo:** [Watch on YouTube](https://youtu.be/S-89j3UQ_pk)

---

## Overview

Resume Generator is a command-line Python application that guides users through an interactive series of prompts to build and export a professionally formatted **PDF resume** — no design tools, no templates, no manual formatting required.

Built as the final project for [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/), the application emphasises real input validation, clean modular code, and a CSV-driven architecture that separates content from logic.

---

## Features

- **Interactive CLI workflow** — step-by-step prompts collect all resume data in a guided session
- **Real input validation** — phone numbers validated via the `phonenumbers` library (international format); emails validated via `validators`; all numeric inputs protected with `try/except`
- **7 customisable sections** — select only the sections you need, in the order you want them:
  - Career Objective
  - Education
  - Skills
  - Experience
  - Projects
  - Certifications
  - Achievements
- **Structured skills input** — skill categories (Programming Languages, Libraries, Frameworks, Tools, Soft Skills) are loaded from `skills.csv` for a consistent, guided experience
- **Dynamic PDF generation** — resume layout is built programmatically with `fpdf`, respecting the user's chosen section order
- **CSV-driven configuration** — section names and skill categories are stored in external CSV files, making the tool easy to extend without touching the source code
- **Unit tested** — 3 pytest tests using `monkeypatch` to simulate and verify CLI input behaviour

---

## Project Structure

```
CS50P-Final-Project/
│
├── project.py          # Main application — all logic, validation, and PDF generation
├── test_project.py     # pytest unit tests (monkeypatch-based CLI testing)
├── sections_name.csv   # Available resume sections with serial numbers
├── skills.csv          # Skill categories and serial numbers for guided input
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## How It Works

```
1. Personal Info    →  Name, phone (validated), email (validated), LinkedIn, GitHub
2. Section Select  →  Choose from 7 sections in your preferred order
3. Section Fill    →  Each section prompts for its specific fields
4. PDF Export      →  Name your file; resume is saved as a .pdf
5. Confirmation    →  ASCII art success message rendered via pyfiglet
```

---

## Installation & Usage

**1. Clone the repository**
```bash
git clone https://github.com/Saurabh6266/CS50P-Final-Project.git
cd CS50P-Final-Project
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the application**
```bash
python project.py
```

**4. Run the tests**
```bash
pytest test_project.py
```

---

## Dependencies

| Library | Purpose |
|---|---|
| `fpdf` | PDF generation and layout |
| `phonenumbers` | Phone number parsing and international format validation |
| `validators` | Email address validation |
| `tabulate` | Grid-style display of section and skill menus |
| `pyfiglet` | ASCII art for the completion message |

Install all at once:
```bash
pip install fpdf phonenumbers validators tabulate pyfiglet
```

---

## Design Decisions

**Why CSV for sections and skills?**
Storing menu options in CSV files decouples content from code. Adding a new resume section or skill category requires only a CSV edit — no code changes. This makes the tool maintainable and extensible without risk of introducing bugs.

**Why command-line only?**
A pure CLI interface keeps the application cross-platform and dependency-light. It also aligns with the CS50P course's focus on Python fundamentals over GUI frameworks.

**Why `fpdf` over a template engine?**
`fpdf` provides enough layout control (fonts, alignment, margins, multi-cell wrapping) for a clean resume format while keeping dependencies minimal. The dynamic layout — where section order follows the user's choices — would be more complex to implement with a static template.

**Input validation philosophy**
Every field that could contain invalid data loops until the user provides correct input, with a clear error message on each failed attempt. This ensures the final PDF never contains malformed data.

---

## Future Improvements

- **Draft save/load** — allow users to resume a partially completed session
- **Multiple templates** — choose between different PDF layouts and fonts
- **GUI interface** — rebuild the input layer with `tkinter` for non-technical users
- **DOCX export** — add `.docx` output alongside PDF
- **Web version** — Flask-based frontend with the same backend logic

---

## Acknowledgements

- Built as the final project for **CS50's Introduction to Programming with Python** by Harvard University (via edX)
- Dataset/config structure inspired by the CS50P project guidelines
