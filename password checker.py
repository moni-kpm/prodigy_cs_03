import re

def check_password_strength(password):
    
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&#]', password) is not None

    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if strength_score == 5:
        feedBack = "Strong password"
    elif 3 <= strength_score < 5:
        feedBack = "Moderate password"
    else:
        feedBack = "Weak password"

    return feedBack, {
        "Length (>= 8)": length_criteria,
        "Uppercase Letter": uppercase_criteria,
        "Lowercase Letter": lowercase_criteria,
        "Number": number_criteria,
        "Special Character (@$!%*?&#)": special_char_criteria
    }

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    feedback, criteria = check_password_strength(password)

    print("\nPassword Strength Feedback:")
    print(feedback)
    print("\nPassword Criteria Check:")
    for criterion, passed in criteria.items():
        status = "Passed" if passed else "Failed"
        print(f"{criterion}: {status}")