# tests/test_pass_val.py

import pytest
from app.utils.pass_val import validate_password

# Test cases for valid passwords
@pytest.mark.parametrize("password", [
    "Valid1Password!",  # Valid: meets all criteria
    "Another$Valid2",   # Valid: meets all criteria
    "StrongPass#123",   # Valid: meets all criteria
    "P@ssw0rd!",        # Valid: meets all criteria
    "Complex!Password3" # Valid: meets all criteria
])
def test_validate_password_valid(password):
    assert validate_password(password) is True

# Test cases for invalid passwords
@pytest.mark.parametrize("password", [
    "short",              # Invalid: too short (less than 8 characters)
    "noNumbers!",         # Invalid: no numbers
    "NoSpecialChars123",  # Invalid: no special characters
    "nosmallletters123!",  # Invalid: no uppercase letters
    "NOUPPERCASE123!",    # Invalid: no lowercase letters
    "12345678",           # Invalid: only numbers
    "!" * 8,              # Invalid: only special characters
    "   ",                # Invalid: only whitespace
    "",                    # Invalid: empty string
    "NoSpecial123",       # Invalid: no special characters
    "NOLOWERCASE1!",      # Invalid: no lowercase letters
    "nouppercase1!",      # Invalid: no uppercase letters
    "1234567A",           # Invalid: too short (only 7 characters)
])
def test_validate_password_invalid(password):
    assert validate_password(password) is False

# Test cases for edge cases
@pytest.mark.parametrize("password, expected", [
    ("A1@b2C3D", True),            # Valid: exactly meets the minimum length (8 characters)
    ("A1@b2C3D4E5F6G7H8", True),  # Valid: long and meets all criteria
    ("A1!", False),                # Invalid: too short (only 4 characters)
    ("A1B2C3D4", False),          # Invalid: no special characters
])
def test_validate_password_edge_cases(password, expected):
    assert validate_password(password) is expected