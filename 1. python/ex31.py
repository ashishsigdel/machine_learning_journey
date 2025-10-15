print("""You enter a dark room with the doors.
Do you go through door #1 or door #2""")

door = input("> ")

if door == "1":
    print("There is a giant bear.")
    print("what do you do?")
    print("1. Hit the bear")
    print("2. Keep slient and hide.")

    bear = input("> ")

    if bear == "1":
        print("Bear attack you! You die.")
    elif bear == "2":
        print("Congratulation, You survived.")
    else: 
        print("Invalid input.")

elif door == "2":
    print("There is a giant party.")
    print("what do you do?")
    print("1. Drint beer.")
    print("2. Barbeeque.")

    party = input("> ")

    if party == "1":
        print("Congratulation. You enjoyed.")
    elif party == "2":
        print("You die. There is poison.")
    else: 
        print("Invalid input.")
else: 
    print("You fall, and die. Try next time.")