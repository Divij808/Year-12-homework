import datetime

validity = True


def validate_name(name):
    return name.isalpha() or (name.isspace() == False)


def validate_dob(dob, valid_dob):
    dob_in_new_format = datetime.datetime.strptime(dob, "%d%m%Y")
    if len(dob) != 8 or dob_in_new_format > datetime.datetime.now():
        valid_dob = False
    return valid_dob


surname = input("Enter your surname: ")
while not validate_name(surname):
    print("Invalid surname. Please enter a name containing only letters")
    surname = input("Enter your surname: ")

first_name = input("Enter your first name: ")
while not validate_name(first_name):
    print("Invalid first name. Please enter a name containing only letters")
    first_name = input("Enter your first name: ")

date_of_birth = input("Enter your date of birth (DDMMYYYY): ")
day = date_of_birth[0:2]
month = date_of_birth[2:4]
year = date_of_birth[4:8]
date_of_birth = day + "-" + month + "-" + year
while not validate_dob(date_of_birth, validity):
    print("Invalid date of birth. Please enter a date in the format DDMMYYYY.")
    date_of_birth = input("Enter your date of birth (DDMMYYYY): ")

username = surname[:2].upper() + first_name[:2].upper() + date_of_birth
print("Your username is:", username)
