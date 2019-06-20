def find_max(listofnumbers):
    maxe = listofnumbers[0]
    for number in listofnumbers:
        if number > maxe:
            maxe = number
    return maxe
    