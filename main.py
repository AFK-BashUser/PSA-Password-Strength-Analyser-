import re
import tkinter as tk
from tkinter import StringVar

# Function to check password strength -->

def check_password_strength(password):
    score = 0
    tips = []

    # length check :
    if len(password) >= 8:
        score += 1
    else:
        tips.append("Password should be at least 8 characters long.")

    # uppercase check :
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add at least one uppercase letter.")

    # lowercase check :
    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Add at least one lowercase letter.")

    # digit check :
    if re.search(r"[0-9]", password):
        score += 1
    else:
        tips.append("Add at least one number.")

    # special character check :
    if re.search(r"[@$!%*?&#]", password):
        score += 1
    else:
        tips.append("Add at least one special character (@$!%*?&#).")

    # avoid common weak patterns :
    weak_list = ["password", "123456", "qwerty", "admin"]
    if any(word in password.lower() for word in weak_list):
        tips.append("Avoid common words like 'password' or '123456'.")
    else:
        score += 1

    # final strength :
    if score <= 2:
        return "Weak", tips
    elif score <= 4:
        return "Moderate", tips
    else:
        return "Strong", tips


# GUI logic -->

def evaluate():
    pwd = entry.get()
    result, suggestions = check_password_strength(pwd)
    strength_label.config(text=f"Strength: {result}")

    if suggestions:
        feedback.set("\n".join(suggestions))
        feedback_label.config(fg="red")   # tips in red
    else:
        feedback.set("Good job! Strong password.")
        feedback_label.config(fg="green")  # success message in green


# Tkinter UI -->

root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x250")
root.config(bg="#f0f0f0")

tk.Label(root, text="Enter Password:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)

entry = tk.Entry(root, width=30, font=("Arial", 12), show="*")
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=evaluate, font=("Arial", 12), bg="lightblue").pack(pady=10)

strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
strength_label.pack()

feedback = StringVar()
feedback_label = tk.Label(root, textvariable=feedback, wraplength=350, justify="left", bg="#f0f0f0", fg="red")
feedback_label.pack(pady=5)

root.mainloop()
