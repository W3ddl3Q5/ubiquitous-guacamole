days = ['S', 'M', 'T', 'W', 'Th', 'F', 'S']
for i in days:
    print("{:>3}".format(i), end='')
print()
day = 1
while day < 31:
    for i in range(7):
        print("{:>3}".format(day), end='')
        day += 1
    print()