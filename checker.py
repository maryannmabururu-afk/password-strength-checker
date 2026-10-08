import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Too short (minimum 8 chars)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add UPPERCASE letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add a number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add special character (!@#$...)")

    print(f"\nPassword: {password}")
    print(f"Score: {score}/5")

    if score == 5:
        print("✅ STRONG - Good for cybersecurity!")
    elif score >= 3:
        print("⚠️ MEDIUM - Can be cracked")
        for f in feedback:
            print(f)
    else:
        print("❌ WEAK - Hackers will crack this easily!")
        for f in feedback:
            print(f)

# Test it
while True:
    pwd = input("\nEnter password to test (or type 'exit'): ")
    if pwd.lower() == 'exit':
        break
    check_password_strength(pwd)