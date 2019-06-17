import math

Fahrenheit = float(input("Please enter the outside temperature in Fahrenheit: "))
wind = float(input("Please enter the wind speed in miles per hour: "))

if (Fahrenheit > -58 and Fahrenheit) < 41 and (wind > 2):
    twc = 35.74 + 0.6215 * Fahrenheit - 35.75 * math.pow(wind, 0.16) + 0.4275 * Fahrenheit * math.pow(wind, 0.16)
    print("The wind-chill index is {:.2f}".format(twc))
else:
    print("Incorrect input")
