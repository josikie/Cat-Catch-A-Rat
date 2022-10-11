import time
import random

cat_breed = ["Persian", "Angora", "Russian Blue", "Siamese"]


def print_pause(string):
    print(string)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def intro():
    print_pause("In this game you are a cat with a "
                + random.choice(cat_breed) +
                " breed")
    print_pause("Your humans told you to catch a rat")
    print_pause("Your humans will reward you your"
                " favorite fish if you catch that rat")
    print_pause("The Rat run very fast")
    print_pause("You saw the rat running into the living room.")


def play_again():
    ask_to_play_again = valid_input("Would you like to play again? (y/n)",
                                    ['y', 'n'])
    if ask_to_play_again == "n":
        print_pause("Thank you for play this game!")
        exit(0)
    print_pause("Restarting the game... \n")


def catch_or_not(claws, items):
    catch_the_rat = valid_input("Will you catch the rat? (y/n)", ['y', 'n'])
    if catch_the_rat == "y":
        print_pause("You chase the rat")
        if claws is True:
            if "pill" in items:
                print_pause("But...")
                print_pause("Even though you run fast,"
                            " your short claws can't catch the rat")
                print_pause("The rat run out of the house")
                print_pause("You lose!")
            else:
                print_pause("But...")
                print_pause("The rat run faster than you")
                print_pause("And your short claws can't catch anything")
                print_pause("The rat run out of the house")
                print_pause("You lose!")
        elif claws is False:
            if "pill" in items:
                print_pause("You run very fast to catch the rat")
                print_pause("Your claws catch the rat")
                print_pause("Congratulations! You catch the rat!")
                print_pause("You are rewarded with a fish")
            else:
                print_pause("Trying to catch the rat with your long claws")
                print_pause("But...")
                print_pause("Rat run faster than you")
                print_pause("The rat run out of the house")
                print_pause("You lose!")
    elif catch_the_rat == "n":
        print_pause("You go back to the living room")
        decide_which_room_to_go(claws, items)


def room_number_one(claws, items):
    if claws is False:
        print_pause("No rat in the first room")
        print_pause("There is only one naughty human child")
        print_pause("Oh no! The kid cut your claws")
        print_pause("You don't have long claws anymore")
        claws = True
        print_pause("You go back to the living room")
        decide_which_room_to_go(claws, items)
    elif claws is True:
        print_pause("There is nothing in the first room")
        print_pause("You go back to the living room")
        decide_which_room_to_go(claws, items)


def room_number_two(claws, items):
    if "pill" in items:
        print_pause("You don't find anything here,"
                    " Just empty room")
        print_pause("You go back to the living room")
        decide_which_room_to_go(claws, items)
    else:
        print_pause("You don't find a rat here")
        print_pause("But there is valuable pill here, "
                    "the pill increases your speed")
        items.append("pill")
        print_pause("You go back to the living room")
        decide_which_room_to_go(claws, items)


def room_number_three(claws, items):
    print_pause("You find a rat in this room!")
    print_pause("You have to catch the rat "
                "to get the fish reward.")
    catch_or_not(claws, items)


def decide_which_room_to_go(claws, items):
    print_pause("\nIn the living room there are three rooms (room 1,"
                " room 2, room 3). Rat is in one of the rooms.")
    room = valid_input("Which room will you enter? (1/2/3) ", ['1', '2', '3'])
    if room == "1":
        room_number_one(claws, items)
    elif room == "2":
        room_number_two(claws, items)
    elif room == "3":
        room_number_three(claws, items)


def main():

    while True:
        claws = False
        items = []
        intro()
        decide_which_room_to_go(claws, items)
        play_again()


main()