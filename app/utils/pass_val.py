# utils.py

import re

def validate_password(password: str) -> bool:
    # Check for minimum length
    if len(password) < 8:
        return False
    # Check for at least one uppercase letter, one lowercase letter, one number, and one special character
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True