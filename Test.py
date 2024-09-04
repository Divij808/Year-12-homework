import datetime


def validate_name(name):
    return name.isalpha() or (name.isspace() == False)


def validate_dob(dob):
    try:
        dob_in_new_format = datetime.datetime.strptime(dob, "%d%m%Y")

    except ValueError:
        return False

    return dob_in_new_format < datetime.datetime.now()


surname = input("Enter your surname: ")
while not validate_name(surname):
    print("Invalid surname. Please enter a surname ")
    surname = input("Enter your surname: ")

first_name = input("Enter your first name: ")
while not validate_name(first_name):
    print("Invalid first name. Please enter a your first name ")
    first_name = input("Enter your first name: ")

date_of_birth = input("Enter your date of birth (DDMMYYYY): ")
while not validate_dob(date_of_birth):
    print("Invalid date of birth. Please enter a date in the format DDMMYYYY.")
    date_of_birth = input("Enter your date of birth (DDMMYYYY): ")

username = surname[:2].upper() + first_name[:2].upper() + date_of_birth
print("Your username is:", username)
