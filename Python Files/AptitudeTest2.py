'''
Prompt user to enter volume of fuel in liters
calculate the mass of co2 produced for diesel and petrol
Display both mass in 2 d.p.

1Liter Diesel: 2.6391kg of Co2
1Liter Petrol: 2.3035kg of Co2

'''

def calulateCo2(d,p):
    dco2 = d * 2.6391
    pco2 = p * 2.3035
    print("The mass of carbon dioxide is {:.2f}kg".format(dco2)) 
    print("The mass of petrol is {:.2f}kg".format(pco2))
    
d = float(input("Enter volume of carbon dioxide (in Liters): "))
p = float(input("Enter volume of petrol (in Liters): "))
calulateCo2(d, p)