import string

def validate_password(password):
    uppercase = sum(1 for ch in password if ch.isupper())
    lowercase = sum(1 for ch in password if ch.islower())
    digits    = sum(1 for ch in password if ch.isdigit())
    special   = sum(1 for ch in password if ch in string.punctuation)

    if len(password) < 10:
        return " Password must be at least 10 characters long."
    if uppercase < 3:
        return " Password must have at least 3 uppercase letters."
    if lowercase < 1:
        return " Password must have at least 1 lowercase letter."
    if digits < 1:
        return "Password must have at least 1 digit."
    if special < 1:
        return " Password must have at least 1 special character."

    return " Password is valid and strong!"

# Test it
user_input = input("Enter your password: ")
result = validate_password(user_input)
print(result)

