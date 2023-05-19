celsius_1 = float(input("Temperature value in degree Celsius: "))
Fahrenheit_1 = (celsius_1 * 1.8) + 32
print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'
      % (celsius_1, Fahrenheit_1))
Fahrenheit_1 = float(input("Temperature value in degree Fahrenheit: "))
celsius_1 = (Fahrenheit_1 - 32) / 1.8
print('The %.2f degree Fahrenheit is equal to: %.2f Celsius'
      % (Fahrenheit_1, celsius_1))
