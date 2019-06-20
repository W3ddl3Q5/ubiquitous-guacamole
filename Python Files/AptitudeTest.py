'''
Prompt user to input speed and acceleration
Calculate Length by using speed * speed divided by 2 * acceleration
Output runway length

Length = (speed*speed) / (2*acceleration)
'''

#calculate of length of runway
def length(a,v):
    Length = (v*v) / (2*a)
    print("The length of the runway is {:.0f}".format(Length))
    
a = int(input("Input acceleration: "))
v = int(input("Input speed: "))
length(a,v)
