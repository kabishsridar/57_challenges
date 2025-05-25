def password_validator(password):
    has_letter = False
    has_number = False
    has_symbol = False
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
        elif not char.isalnum():
            has_symbol = True
    
    if password.isdigit() and len(password) < 8:
        print(f"The password {password} is a very weak password")
    elif password.isalpha() and len(password) < 8:
        print(f"The password {password} is a weak password")
    elif password.isalnum() and len(password) >= 8:
        print(f"The password {password} is strong")
    elif has_symbol and has_letter and has_number and len(password) >= 8:
        print(f"The password {password} is very strong")
            
password = input("Enter the password: ")

password_validator(password)