import re

def check_password_strength(password):
    score = 0
    feedback = []

    # checking minimum length :
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    # checking uppercase :
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # checking lowercase :
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # checking digit :
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    # checking special characters :
    if re.search(r"[@$!%*?&#]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # checking against common passwords :
    common_list = ["password", "123456", "qwerty", "admin"]
    if any(word in password.lower() for word in common_list):
        feedback.append("Avoid common patterns like 'password' or '123456'.")
    else:
        score += 1

    # final rating -->
    if score <= 2:
        return "Weak", feedback
    elif score <= 4:
        return "Moderate", feedback
    else:
        return "Strong", feedback
