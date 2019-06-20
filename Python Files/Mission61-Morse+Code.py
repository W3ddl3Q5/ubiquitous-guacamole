#Programming I

#######################
#     Mission 6.1     #
#     Morse Code      #
#######################

#Background
#==========
#Tom has a partner to help him with the cases. To
#communicate to each other, they uses Morse code.
#Write a Python program that prompts the user to
#key in a number, convert each digit according to
#the diagram below. Each Morse code of a digit has
#to be separated with 3 spaces. The following shows
#a sample output of the program.
#
#Enter a number to convert:9
#The morse code for 9 is ----.
#>>> 
#Enter a number to convert:101
#The morse code for 101 is .----   -----   .----
#>>> 


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - num
#   - morse_code



#START CODING FROM HERE
#======================

#Prompt user to enter the number to convert
num = str(input('Enter a number to convert:'))


#convert to morse code
def convert_code(num):
    dots = 0
    converted = ""
    for i in range(len(num)):
        if int(num[i]) < 6:
            dots = int(num[i]) % 5
            converted = ("{}{:<8}".format(converted, "." * dots + "-" * (5-dots)))
        elif int(num[i]) > 5:
            dash = int(num[i]) % 5
            converted = ("{}{:<8}".format(converted, "-" * dash + "." * (5-dash)))

    print(converted) #Modify to display the morse code
    morse_code = converted
    return morse_code#Do not remove this line

    
#Do not remove the next line
convert_code(num)

#test cases
#input 9        output ----.
#input 101      output .----   -----   .----
#input 0906     output -----   ----.   -----   -....

