import os
import re

# Input and output file paths
input_file = 'sample_input.txt'
output_all = 'all_emails.txt'
output_gmail = 'gmail_emails.txt'
output_others = 'other_emails.txt'

# Email regex pattern
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Ensure the input file exists
if not os.path.exists(input_file):
    print(f"Error: {input_file} not found!")
    exit()

# Read input file
with open(input_file, 'r') as file:
    text = file.read()

# Extract emails
emails = re.findall(email_pattern, text)
unique_emails = sorted(set(emails))  # Remove duplicates

# Categorize emails
gmail_emails = [email for email in unique_emails if email.endswith('@gmail.com')]
other_emails = [email for email in unique_emails if not email.endswith('@gmail.com')]

# Write all emails
with open(output_all, 'w') as file:
    file.write('\n'.join(unique_emails))

# Write Gmail only
with open(output_gmail, 'w') as file:
    file.write('\n'.join(gmail_emails))

# Write Other emails
with open(output_others, 'w') as file:
    file.write('\n'.join(other_emails))

# Output status
print(f"Total Emails Extracted: {len(unique_emails)}")
print(f"Gmail Emails: {len(gmail_emails)} saved in {output_gmail}")
print(f"Other Emails: {len(other_emails)} saved in {output_others}")
