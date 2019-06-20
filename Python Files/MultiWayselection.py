'''
Prompt user to Enter temperature

if temp <= -5 then
    print Go bowling
if temp <= 0 then
    print go skiing
if temp <=20 then
    print go jogging
if temp <=25 then
    print play tennis; wear white clothes
if temp <=30 then
    print Sun-tan in the park
if temp > 30 then
    print go swimming
    
'''


temp = int(input("What's the temperature now: "))
if temp <= -5:
    print("Go Bowling")
elif temp <= 0:
    print("Go Skiing")
elif temp <= 20:
    print("Go Jogging")
elif temp <= 25:
    print("Play Tennis; wear white clothes")
elif temp <= 30:
    print("Go Sun-tanning in the park")
else:
    print("Go Swimming")
    
