def is_leap_year(year):
    # Leap years are divisible by 4
    if year % 4 == 0:
        # But if a year is divisible by 100, it must also be divisible by 400 to be a leap year
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

# Get the year from the user
try:
    year_to_check = int(input("Enter a year to check for leap year: "))
    if is_leap_year(year_to_check):
        print(f"{year_to_check} is a leap year.")
    else:
        print(f"{year_to_check} is not a leap year.")
except ValueError:
    print("Please enter a valid year.")
