digits = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero"
    }

numbers = input("What digits do you want to covert? : ")

index = 0;
while index != len(str(numbers)):
    print(digits.get(int(numbers[index])), end =" ")
    index += 1