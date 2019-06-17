    '''
Prompt user to enter NRIC
Check if NRIC is valid
ouput if its valid or not valid

if NRIC is valid:
    return true
else
    return false 
'''
#multiplication
listnumbers = [2,7,6,5,4,3,2]
keypairnumber = {0:'J',1:'Z',2:'I',3:'H',4:'G',5:'F',6:'E',7:'D',8:'C',9:'B',10:'A'}

#validation
def validation(NRIC):
    
    index = 0
    checksum = 0
    
    #Doing calculation
    while index != 7:
        checksum = checksum + (int(NRIC[index + 1]) * listnumbers[index])
        index += 1
    
    checksum += 4
    remainder = checksum % 11
    lastalphanumber = keypairnumber[remainder]
    
    #Check if last alphabet of NRIC is matched
    if lastalphanumber is NRIC[-1]:
        Valid = "True"
    else:
        Valid = "False"
        
    print("Validity of the IC: {}".format(Valid))

#input NRIC
NRIC = input("Enter NRIC: ").upper()
validation(NRIC)