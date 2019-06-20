#Program calculate the rate for photocopy in a printing shop based on the number of pages input

pages = int(input("Enter number of pages to print: "))
initpages = pages
if pages > 100:
    cost = 100 * 0.03
    pages = pages - 100
    if pages > 200:
        cost = cost + (200 * 0.02)
        pages = pages - 200
        cost = cost + (pages * 0.01)
    else:
        cost = cost + (pages * 0.02)
else:
    cost = pages * 0.03

print("Cost of printing {0:d} pages is ${1:.2f}".format(initpages, cost))
    
    