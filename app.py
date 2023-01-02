# Help = input("")
command = ""
started = False
stopped = False

while True:
    command= input("> ").lower()
    if  command == "start":
        if started:
            print("car already started")
        else: 
            started = True
            print("car started... get ready to go")
    elif command == "stop":
        if stopped:
            print("car already started")
        else: 
            stopped = True
            print("car started... get ready to go")
    elif command == "help":
        print('''
        start 
        stop
        quit
        ''')
    elif command == "quit":
        break
    else:
        print("i don't understand that")