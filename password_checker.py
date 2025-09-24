import string

def check_password_strength(password):
    """
    Analyzes the strength of a password based on a set of rules and returns a score and feedback.
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    # Check for special characters
    special_chars = string.punctuation
    has_special = any(c in special_chars for c in password)

    # --- Scoring System ---
    score = 0
    feedback = []

    # 1. Length Score
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append(" Password should be at least 8 characters long.")

    # 2. Character Variety Score
    if has_upper:
        score += 1
    else:
        feedback.append(" Missing an uppercase letter (A-Z).")

    if has_lower:
        score += 1
    else:
        feedback.append(" Missing a lowercase letter (a-z).")

    if has_digit:
        score += 1
    else:
        feedback.append(" Missing a number (0-9).")

    if has_special:
        score += 1
    else:
        feedback.append(" Missing a special character (e.g., !@#$%).")

    # --- Final Strength Assessment ---
    if score >= 6:
        strength = " Strong"
    elif score >= 4:
        strength = " Medium"
    else:
        strength = " Weak"
        
    return strength, feedback

# --- Main part of the script ---
if __name__ == "__main__":
    print("--- Password Strength Analyzer ---")
    print("Enter a password to check its strength, or type 'exit' to quit.")
    
    while True:
        password_input = input("\nEnter a password: ")
        
        if password_input.lower() == 'exit':
            break
            
        strength, feedback = check_password_strength(password_input)
        
        print(f"Password Strength: {strength}")
        if feedback:
            print("\nRecommendations:")
            for item in feedback:
                print(f"- {item}")
        print("\n" + "="*40)
