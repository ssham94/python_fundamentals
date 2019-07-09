total_distance = 0
energy = 10
wallet = True
ate_garbage = False

while energy > 0:
    print("What would you like to do?")
    user_action = input()
    if user_action.lower() == "walk":
        total_distance+=1
        energy += 1
        print("Distance from home is {} km".format(total_distance))
        print("Your energy level is {}".format(energy))
    elif user_action.lower() == "run":
        total_distance+=5
        energy -= 5
        print("Distance from home is {} km".format(total_distance))
        print("Your energy level is {}".format(energy))
    elif user_action.lower() == "go home":
        break
    elif user_action.lower() == "eat healthy":
        energy += 5
        print("You found a apple and ate it. Your energy level increases to {}".format(energy))
    elif user_action.lower() == "eat unhealthy":
        energy -=10
        ate_garbage = True
        print("You found some garbage on the floor. You decided to eat it. You feel sick. Your energy level decreases to {}.".format(energy))
    elif user_action.lower() == "nap":
        energy += 50
        if wallet == True:
            wallet = False
            print("You napped and felt great after waking up. But your wallet got stolen. Your energy level increases to {}. Your happiness level drops by 80 :(".format(energy))
        else:
            print("Being sad that you lost your wallet, you decided to nap again. Your energy level increases to {}. You wake up still feeling sad".format(energy))
    elif energy <= 0:
        print("You were so tired you passed out on the street.")
    else: 
        print("You had an incorrect input. Please only type in \"walk\" or \"run\" or \"go home\" or \"eat healthy\" or \"eat unhealthy\" or \"nap\"")

if energy > 0 and ate_garbage:
    print("You made it home safely, possibly with garbage in your system. You travelled a total of {} km roundtrip though, so congrats?".format(total_distance*2))
elif energy > 0:
    print("You made it home safely. Congrats, you travelled a total of {} km roundtrip!".format(total_distance*2))
else: 
    print("You were so tired you passed out on the street. At least you're only {} km away from your home".format(total_distance))