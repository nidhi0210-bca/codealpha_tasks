# codealpha_tasks
This repository contains all the tasks performed for python internship program provided by codealpha.

# Email Extractor & Categorizer

A simple and efficient Python script to extract **email addresses** from a text file and categorize them based on domain.

## Features

- Extracts all unique email addresses from any `.txt` file
- Separates:
  - **All emails** → `all_emails.txt`
  - **Only Gmail emails** → `gmail_emails.txt`
  - **Other emails** → `other_emails.txt`
- Uses `regex` for flexible and accurate matching
- Automatically handles duplicates
- Lightweight and beginner-friendly

## File Structure

```

email-extractor/
├── sample\_input.txt         # Sample input text file with emails
├── email\_extractor.py       # Main Python script
├── all\_emails.txt           # Output: all extracted emails
├── gmail\_emails.txt         # Output: only Gmail addresses
├── other\_emails.txt         # Output: non-Gmail addresses
└── README.md                # Project documentation

````

## How to Use

### 1.Clone the Repo

- bash
git clone https://github.com/your-username/email-extractor.git
cd email-extractor

### 2. Run the Script

Make sure you have Python 3 installed.

- bash
python email_extractor.py

### 3. Check Output

After running, you’ll find three new files:

* `all_emails.txt`
* `gmail_emails.txt`
* `other_emails.txt`

## Requirements

* Python 3.x
* No external dependencies (`re`, `os` are standard libraries)
