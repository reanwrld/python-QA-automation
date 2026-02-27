# password input 
password = input("Enter your password: ")

# Logic for special characters
has_special = False 
special_chars = "$#@^&%*()!"

for char in password:
    if char in special_chars:
        has_special = True

# Conditions
if len(password) >= 8 and has_special and password != "password":
    print("Access Granted: your password is secure.")
else:
    print("Password must be at least 8 characters, include special characters, and not be the word password.")

