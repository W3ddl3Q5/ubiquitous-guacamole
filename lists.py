'''
listofnumber = [1, 2, 3, 4, 6, 5, 9, 10, 10, 20, 30, 20, 20, 1, 25]
for number in listofnumber:
    for number1 in listofnumber:
        if number < number1:
            store = number1

print(store)
'''            
'''
#2d lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]    
]

print(matrix[0][1])
'''

#Removing duplicates in a list

names = ['dog12','dog', 'god', 'dog', 'cat', 'eat','dog', 'god', 'dog', 'cat', 'eat','dog', 'god', 'dog', 'cat', 'eat']
emptyset = []
for name in range(len(names)):
    if names[name] not in emptyset:
        emptyset.append(names[name])        
print(emptyset)