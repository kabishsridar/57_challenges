silent = input("Is the car silent when you turn the key? ")

if silent == "y":
    battery_terminals = input("Are the battery terminal corroded? ")
    if battery_terminals == "y":
        print("Clean terminals and try starting again")
    elif battery_terminals == "n":
        print("Replace cables and try again")
elif silent == "n":
    clicking_noice = input("Does the car make a clicking noice? ")
    if clicking_noice == "y":
        print("Replace the battery")
    elif clicking_noice == "n":
        crankup = input("Does the car carnk up but fail to start? ")
        if crankup == "y":
            print("Check spark plug connections.")
        elif crankup == "n":
            engine_start = input("Does the engine start and then die? ")
            if engine_start == "y":
                fuel_injection = input("Does the car have fuel injection? ")
                if fuel_injection == "y":
                    print("Get it in for service.")
                elif fuel_injection == "n":
                    print("Check to ensure the choke is opening and closing.")