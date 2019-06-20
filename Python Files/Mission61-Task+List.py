'''
input: Prompt user to input weight
        Prompt user for the need for express service
process: checks the conditions and calculate the price
output: Display cost

IF weight less than 1 THEN
    cost is assigned the value of 10
ELSE IF weight < 5 THEN 
    cost is assigned the value of 15
ELSE
    cost is assigned the value of 20
ENDIF

IF express == "y" or express=="Y" THEN
    Cost = cost + 10.5
    
Diplay cost
'''
weight = input("Enter weight of parcel in KG : ")
service = input("Is express service required (y/n) : ")
if weight <= 1:
    cost = 10
elif weight < 5:
    cost = 15
else:
    cost = 20
    
if service == "y":
    cost = cost + 10.50
print("The cost is ${}".format(cost))