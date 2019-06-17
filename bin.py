item = ["Apple Pie", "Chicken Pie", "Apple Tart", "Egg Tart", "Durian Tart"]
price = [1.80,2.90,0.85,0.95,1.10]
quantity = [3,5,9,12,30]

def calculate(cost, unit, qty):
    total = 0
    for x in range(len(unit)):
        total += (cost[x] * qty[x])
    print("Total Cost: ${:.2f}".format(total))
    print("{0:<20}{1:<12}{2}".format("Item", "Unit Price", "Quantity"))
    print("{0:<20}{1:<12}{2}".format("====", "==========", "==========="))
    for x in range(len(unit)):
        print("{:<20}${}{}".format(unit[x], cost[x], qty[x]))
calculate(price, item, quantity)
    