total_distance = 0

while True:
    print("Would you like to walk or run?")
    walk_or_run = input()
    if walk_or_run.lower() == "walk":
        total_distance+=1
        print("Distance from home is {} km".format(total_distance))
    elif walk_or_run.lower() == "run":
        total_distance+=5
        print("Diistance from home is {} km".format(total_distance))
    else: 
        print("Please only type in \"walk\" or \"run\"")
