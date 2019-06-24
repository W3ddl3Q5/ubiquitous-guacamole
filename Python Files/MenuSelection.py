menu = ["reboot system now","apply sdcard:update.zip","wipe data/factory reset", "+++++Go Back+++++ \n"]

def menuprinter():
    count = 0
    print("Onix Recovery v2.5.1.0 \n")
    for select in menu:
        count += 1
        print("[{0}] {1}".format(count ,select))
    print("---------------------------------------------")

selection = 0
while selection != 4:
    menuprinter()
    selection = int(input())
    print(menu[selection-1])
    print("\n")
    

    
        


    