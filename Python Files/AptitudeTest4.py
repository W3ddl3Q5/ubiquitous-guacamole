import math

def cal(payment, interest, years):
    total = payment / math.pow((1+interest), years)
    print("Discounted value {:.2f}".format(total))

payment = float(input("Payment: "))
rate = float(input("Rate: "))
n = int(input("No. of years: "))

cal(payment, rate ,n)