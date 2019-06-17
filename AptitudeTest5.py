#withdraw money

amount = int(input("Enter amount to withdraw: "))
no_of_50notes = amount // 50
remain = amount % 50
no_of_10notes = remain / 10

print("{0:.0f} $50 notes {1:.0f} $10 notes".format(no_of_50notes, no_of_10notes))