room1 = [20, 21, 23, 25, 22]
room2 = [27, 23, 25, 20, 30, 24]
room3 = [22, 23, 24, 22]
measurement = [room1, room2, room3]

for room in measurement:
    total = 0
    for temp in room:
        total += temp
    avg = total / len(room)
    print("Average temperature in room {} is {:.1f}".format(room ,avg))