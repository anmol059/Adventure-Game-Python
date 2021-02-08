import time
import random
weapon = []
word = random.choice(["Dragon", "Gorgon", "Pirate", "Witch"])


def print_pause(string):
    print(string)
    time.sleep(.5)


def choice():
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n"
                "What would you like to do?")
    enter()


def start():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")
    choice()


def cave_again():
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the good"
                " stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field.\n")
    choice()


def play_again():
    play_again_res = input("Would you like to play again? (y/n)\n").lower()
    if play_again_res == 'y' or play_again_res == 'yes':
        start()
    elif play_again_res == 'n' or play_again_res == 'no':
        print_pause("Thanks for playing! See you next time.")
        return
    else:
        play_again()


def fight():
    if 'sword' in weapon:
        print_pause(f"As the {word} moves to attack, you unsheath "
                    "your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your  hand"
                    " as you brace yourself for the attack.")
        print_pause(f"But the {word} takes one look at your shiny new"
                    " toy and runs away!")
        print_pause(f"You have rid the town of the {word}."
                    "You are victorious!")
        play_again()
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {word}.")
        print_pause("You have been defeated!")
        play_again()


def field():
    print_pause("You run back into the field. Luckily, you don't "
                "seem to have been followed.\n")
    choice()


def inside_house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens"
                f" and out steps a {word}.")
    print_pause(f"Eep! This is the {word}'s house!")
    print_pause(f"The {word} attacks you!")
    fight_or_run()


def fight_or_run():
    input2 = input("Would you like to (1) fight or (2) run away?\n")
    if input2 == '1':
        fight()
    elif input2 == '2':
        field()
    else:
        fight_or_run()


def enter():
    entered_input = input("Please enter 1 or 2.\n")
    if entered_input == '2' and 'sword' in weapon:
        cave_again()
    elif entered_input == '1':
        inside_house()
    elif entered_input == '2':
        weapon.append("sword")
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take"
                    " the sword with you.")
        print_pause("You walk back out to the field.\n")
        choice()
    else:
        enter()


start()      # The function which makes the game start.
if __name__ == "__main__":
    play_game()