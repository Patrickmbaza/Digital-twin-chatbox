import json
import os

# Read LinkedIn data - try text file first, fallback to PDF
linkedin = ""
linkedin_path = "./data/linkedin.txt"

if os.path.exists(linkedin_path):
    try:
        with open(linkedin_path, "r", encoding="utf-8") as f:
            linkedin = f.read()
    except Exception as e:
        print(f"Error reading LinkedIn text file: {e}")
        linkedin = "LinkedIn profile not available"
else:
    # Fallback to PDF if text file doesn't exist
    try:
        from pypdf import PdfReader
        reader = PdfReader("./data/linkedin.pdf")
        for page in reader.pages:
            text = page.extract_text()
            if text:
                linkedin += text
    except Exception as e:
        print(f"Error reading LinkedIn PDF: {e}")
        linkedin = "LinkedIn profile not available"

# Read other data files
with open("./data/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

with open("./data/style.txt", "r", encoding="utf-8") as f:
    style = f.read()

with open("./data/facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)

print(f"Successfully loaded resources. LinkedIn: {len(linkedin)} chars")
