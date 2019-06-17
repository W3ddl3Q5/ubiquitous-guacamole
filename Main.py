#variable declaration

print("Car Simulator")
user_command = "stop"
car_state = "stop"

while user_command != "quit":
    user_command = input(">").lower()
    if user_command == "start":
        if car_state == "start":
            print("Car is already started")
        else:
            print("Car is starting... Vroom")
            car_state = "start"
        
    elif user_command == "stop":
        if car_state == "stop":
            print("Car is already stopped")
        else:
            print("Car has stopped...")
            car_state = "start"

        car_state = "stop"
    elif user_command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif user_command == "quit":
        break
    else:
        print("Invalid command")
        

        


