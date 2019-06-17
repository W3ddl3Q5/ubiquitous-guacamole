mains = input("Please enter the main string: ").upper()
targets = input("Please enter the target string: ").upper()
index = 0
similarity = 0
while index != 4:
    if mains[index] != targets[index]:
        similarity += 1
    index += 1
    
print("String Dissimilarity Score: {0:d}".format(similarity))
if similarity < 2:
    print("High Similarity")
else:
    print("Low Similarity")