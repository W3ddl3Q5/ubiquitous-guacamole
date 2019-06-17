print("Car Insurance Calculator")
print("========================")
gender = input("Enter gender [M/F]: ")
age = int(input("Enter age: "))
accident = input("Have you been in a traffic accident before? [Y/N] ")

if age < 25:
    if gender == "M":
        multiplier = 1.8
    else:
        multiplier = 1.4
        

elif age > 24 and age < 35:
    if gender == "M":
        multiplier = 1.5
    else:
        multiplier = 1.3


elif age > 34 and age < 45:
    if gender == "M":
        multiplier = 1.2
    else:
        multiplier = 1.1


elif age > 44 and age < 54:
    if gender == "M":
        multiplier = 1.0
    else:
        multiplier = 0.9


elif age > 54 and age < 65:
    if gender == "M":
        multiplier = 1.4
    else:
        multiplier = 1.2

else:
    if gender == "M":
        multiplier = 1.7
    else:
        multiplier = 1.4

premium = 800 * multiplier

if accident == "Y":
    premium += 300

print("Your annual premium is: {}".format(premium))
    

