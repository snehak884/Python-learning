light = "red"

match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid color")



day = input("Enter day number (1-7): ")

match day:
    case "1":
        print("Monday - Start of work week!")
    case "2":
        print("Tuesday - Keep going!")
    case "3":
        print("Wednesday - Midweek!")
    case "4":
        print("Thursday - Almost weekend!")
    case "5":
        print("Friday - TGIF!")
    case "6":
        print("Saturday - Weekend!")
    case "7":
        print("Sunday - Rest day!")
    case _:
        print("Invalid! Enter number 1-7")



# same examples via if else statement 

day = input("Enter day number (1-7): ")

if day == "1":
    print("Monday - Start of work week!")
elif day == "2":
    print("Tuesday - Keep going!")
elif day == "3":
    print("Wednesday - Midweek!")
elif day == "4":
    print("Thursday - Almost weekend!")
elif day == "5":
    print("Friday - TGIF!")
elif day == "6":
    print("Saturday - Weekend!")
elif day == "7":
    print("Sunday - Rest day!")
else:
    print("Invalid! Enter number 1-7")