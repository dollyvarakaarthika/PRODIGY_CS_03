import re

def password_complexity_checker(password):
    length = len(password)
    
    # Criteria for password complexity
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[\W_]', password) is not None
    # Scoring the password
    score = 0
    feedback = []
    
    if length >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if has_upper:
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
    
    if has_lower:
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
    
    if has_digit:
        score += 1
    else:
        feedback.append("Password should include at least one number.")
    
    if has_special:
        score += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, etc.).")
    
    # Determine strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Prepare feedback message
    if strength == "Very Strong":
        feedback_message = "Your password is very strong."
    else:
        feedback_message = "Your password is " + strength.lower() + ". " + " ".join(feedback)
    
    return {
        "password": password,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "strength": strength,
        "feedback": feedback_message
    }

# Get password input from the user
password = input("Enter a password to check its complexity: ")
result = password_complexity_checker(password)

# Print the result in a more readable format
print(f"Password: {result['password']}")
print(f"Length: {result['length']}")
print(f"Has Uppercase: {result['has_upper']}")
print(f"Has Lowercase: {result['has_lower']}")
print(f"Has Digit: {result['has_digit']}")
print(f"Has Special Character: {result['has_special']}")
print(f"Strength: {result['strength']}")
print(f"Feedback: {result['feedback']}")
