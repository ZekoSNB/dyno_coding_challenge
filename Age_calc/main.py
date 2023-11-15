
from datetime import date

today = date.today()

def age_calc():
    while True:
        try:
            print("Enter your date of birth: ")
            year = int(input("Year: "))
            month = int(input("Month: "))
            day = int(input("Day: "))
            age = today.year - year - ((today.month, today.day) < (month, day))
            print("You are {} years old.".format(age))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

age_calc()
