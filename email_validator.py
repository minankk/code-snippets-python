# email_validator.py
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    test_email = "minan@example.com"
    print(f"{test_email} is valid? {is_valid_email(test_email)}")
