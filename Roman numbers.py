def arabic_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

# Get user input for the Arabic numeral
user_input = input("Enter an Arabic numeral: ")
try:
    arabic_number = int(user_input)
    if arabic_number >= 1:
        roman = arabic_to_roman(arabic_number)
        print(f"{arabic_number} in Roman numerals is: {roman}")
    else:
        print("Please enter a positive Arabic numeral.")
except ValueError:
    print("Invalid input. Please enter a valid Arabic numeral.")
