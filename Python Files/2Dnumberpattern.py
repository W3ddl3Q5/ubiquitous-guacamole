for i in range(1, 6):
    dots = 5 - i
    while dots != 0:
        print("." , end='')
        dots -= 1
    for j in range(i):
        print(i, end='')
    print()
        
        
        