"""
write a function that asks for user input with the input() function
Ask them to create a password that is greater than >6 and <12 characters long ( 6< pwd < 12)

Use an assert statement to validate their password choice

"""
def create_password():
    password = input("Please enter a password (6 to 12 characters): ")
    assert 6 < len(password) < 12, "Password length is not within the required range."
    print(f"The password is acceptable!")

create_password()