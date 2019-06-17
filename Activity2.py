mark = int(input("Enter marks: "))

if 0 <= mark <= 100  :
    if mark >= 50:
        print('You have passed')
        print('Good job done')
    else:
        print('You have failed')
else:
    print('Invalid mark')