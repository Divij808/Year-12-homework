import datetime

current_year = datetime.datetime.now().year
validity = True


def create_username(last_name, first_names, date_of_births):
    surname_prefix = last_name[:2].upper()
    first_name_prefix = first_names[:2].upper()

    # Combine the prefixes with the full date of birth
    usernames = surname_prefix + first_name_prefix + date_of_births

    return usernames


def validate_name(name):
    return name.isalpha() or name.isspace()


def validate_dob(dob, valid_dob):
    if len(dob) != 8:
        valid_dob = False
    else:
        day = int(dob[0:2])
        month = int(dob[2:4])
        year = int(dob[4:8])

        # Check for leap year if month is February and day is 29
        if month == 2 and day == 29:
            if not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                valid_dob = False

        # Check for valid day and month based on special months
        special = [4, 6, 9, 11]
        if month in special:
            if not (1 <= day <= 30):
                valid_dob = False
        elif not (1 <= day <= 31):
            valid_dob = False

        # Check for valid year
        if not (year < current_year):
            if not (year == current_year):
                if not (1 <= month <= 12):
                    valid_dob = False

    return valid_dob


surname = input("Enter your surname: ")
while not validate_name(surname):
    print("Invalid surname. Please enter a name containing only letters and spaces.")
    surname = input("Enter your surname: ")

first_name = input("Enter your first name: ")
while not validate_name(first_name):
    print("Invalid first name. Please enter a name containing only letters and spaces.")
    first_name = input("Enter your first name: ")

date_of_birth = input("Enter your date of birth (DDMMYYYY): ")
while not validate_dob(date_of_birth, validity):
    print("Invalid date of birth. Please enter a date in the format DDMMYYYY.")
    date_of_birth = input("Enter your date of birth (DDMMYYYY): ")

# Create the username
username = create_username(surname, first_name, date_of_birth)

# Display the username to the user
print("Your username is:", username)
