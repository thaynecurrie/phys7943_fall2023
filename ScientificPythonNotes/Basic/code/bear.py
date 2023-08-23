from sys import exit
import numpy as np

def gold_room():
    print("This room is full of gold.  How many gold coins do you take?")

    try:
       choice = int(input("> "))
    except:
       dead("You chose a non-integer amount of coins. \n Trying in vain to break one of the coins into pieces, you upset the bear who rips your face off.")

    if how_much < 50:
        print("Nice, you're not greedy.  You escape the bear on your way out.  You Win!")
        exit(0)
    else:
        dead("You drop coins as you flee, upsetting the bear who rips your face off")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        if bear_moved == True:
         choice = input("> [take honey,taunt bear, open door] ")
        else:
         choice = input("> [take honey,taunt bear] ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Game Over!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take [right, left]?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


