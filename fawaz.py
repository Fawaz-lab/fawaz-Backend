import re

def check_identical_strings(str1: str, str2: str) -> bool:
    return str1 == str2

def is_valid_email(email_string: str) -> bool:
    pattern = r"^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email_string.strip()) is not None

def check_minimum_length(input_string: str, min_length: int = 8) -> bool:
    return len(input_string) >= min_length
    
def is_complex_password(password_string: str) -> bool:
    if len(password_string) < 8:
        return False
    has_lower = bool(re.search(r"[a-z]", password_string))
    has_upper = bool(re.search(r"[A-Z]", password_string))
    has_digit = bool(re.search(r"\d", password_string))
    has_special = bool(re.search(r"[^a-zA-Z0-9]", password_string))

    return has_lower and has_upper and has_digit and has_special
