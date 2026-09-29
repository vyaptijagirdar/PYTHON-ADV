import re

text = """
For online shopping inquiries,contact shopper@gmail.com or orders2016@gmail.com.
for product support, email support.shop@gmail.com
"""
email_pattern = r'[a-zA-Z0-9,_%+-]+@[a-zA-Z0-9,-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern,text)

print("Email addresses found:")

for email in emails:
    print(email)
