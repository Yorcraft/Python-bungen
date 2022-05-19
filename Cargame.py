userip = input(">")

motorstatus = False
while True:
    if userip == "start":
        if motorstatus == True:
            print("Motor is already running")
            userip = input(">")
        else:
            motorstatus = True
            print("Motor started")
            userip = input(">")
    elif userip == "stop":
        if motorstatus == True:
            motorstatus = False
            print("Motor stopped")
            userip = input(">")
        elif motorstatus == False:
            print("motor is already stopped")
            userip = input(">")
    elif userip == "quit":
        print("see ya")
        break
    elif userip == "help":
        print("> start - start the car\n> stop - stop the car\n> quit - exit the program\n> help - does this lol")
        userip = input(">")
    else:
        print("Sorry can't quiet understand ya")
        userip = input(">")
