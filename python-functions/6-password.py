def validate_password(number):
    # Check for at least 8 characters
    if len(number) < 8:
        return False

    # Check for at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = any(char.isupper() for char in number)
    has_lowercase = any(char.islower() for char in number)
    has_digit = any(char.isdigit() for char in number)

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check for spaces
    if ' ' in number:
        return False

    return True

