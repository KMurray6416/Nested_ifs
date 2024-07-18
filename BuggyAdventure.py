    # Task 1

place = input("Choose a place. (forest/cave): ")
action = input("Which would you prefer? (climb a tree/cross a river): ")
action2 = input("Would you like to (light a torch/proceed in the dark): ")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    if action2 == "light a torch":
        print("Look at all that shiny treasure!")
    elif action2 == "proceed in the dark":
        print("Might be able to spot some ghost pirates!")

    #Task 3

    else:
        pass