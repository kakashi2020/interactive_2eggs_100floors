#easy and interactive format to understand the 2 eggs, 100 floors puzzle

#BUGS TO FIX: egg and egg_2 are registered as tuples, therefore I can not use
#.casefold to ensure that the inputs "N" or "Y" work instead of "n" and "y".

min_floor = 1
max_floor = 100
floors = (min_floor, max_floor)
drop_floor = min_floor + (max_floor - min_floor) // 2
egg = ()
egg_2 = ()
broken = "y"
safe = "n"
possibilities = [broken, safe]
throws = 0
instructions = input("Easy way to understand the 2 egg 100 floors challenge. Basically,\n"
                     "you have 2 eggs to figure out from which floor of a 100 story\n"
                     "building the egg would break using the minimum amount of tosses.\n"
                     "\n"
                     "The operation is simple enough. You find the average of the lower\n"
                     "and higher floor and drop the egg from that floor (at fist being the\n"
                     "floor number 50). If it brakes, then you have only one egg to figure\n"
                     "out the break-floor, therefore, you start\ntossing it from floor 1\n"
                     "upwards until it brakes. In the other scenario, if it doesn't break\n"
                     "from floor 50, 51 becomes your new lower floor and you repeat the\n"
                     "operation. [NOTE: a NOT broken egg can be used again]"
                     "\n"
                     "\n"
                     "Confused? Press ENTER to interact with hypothetical example.")
while egg != broken:
    drop_floor = min_floor + (max_floor - min_floor) // 2
    print()
    egg = input("You dropped the egg from floor number {}. Did it break? ".format(drop_floor))
    if egg == safe:
        min_floor = drop_floor + 1
        throws += 1
    if egg not in possibilities:
        print()
        print("Please choose a valid option. 'y' for YES, 'n' for NO")


else:
    throws += 1
    print()
    print("The first egg broke from the floor number {}".format(drop_floor))
    while egg_2 != broken:
        drop_floor = min_floor
        print()
        egg_2 = input("You dropped your 2nd egg from floor number {}. Did it break? ".format(drop_floor))
        if egg_2 == safe:
            min_floor = drop_floor + 1
            throws += 1
        if egg_2 not in possibilities:
            print()
            print("Please choose a valid option. 'y' for YES, 'n' for NO")
    else:
        throws += 1
print()
print("It took {} throws to find that the egg breaks in the floor {}".format(throws, drop_floor))