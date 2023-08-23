# _Python for Scientific Data Analysis_


#  Basic Python

## In-Class Exercises (8/23)



### 1. Modify ex29.py as follows:
* include an if-then statement that depends on *two* conditions being true instead of just one
* include an if-then statement that dpeends on *one or another* condition being true

### 2. The Bear Room:

Now we are going to execute a piece of code that combines multiple elements of loops, lists, etc.  Behold the bear game, listed under ``bear.py``.   

```
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
```

* part A - figure out how to get the game started. Look at the source code to see the order in which each function is called.  Make sure you understand the ``if-then`` structures.
* part B - add another option besides the left or right door (with appropriate print statements) .  Make the outcome dependent upon chance (hint use ``np.random.rand``).



### 3. Lists, Arrays, Loops and Type Conversions:

Start with a list 4 elements long, including a mix of floating point numbers and integers: $\pi$, e, 3.1 and 5.

Remove 3.1 using the ``remove`` function and array indexing.  

Append Euler's constant to the list

Write a line of code that prints out ``a``, repeated 3 times

Write a line of code that prints out each element of ``a`` multiplied by 3

Write a for-loop that prints out each element of ``a`` multiplied by 3

### 4. Dictionaries

Use three defined dictionaries with the following entries -- 1. city + country abbreviation, 2. country abbreviation + skyscraper, 3. skyscraper + height.   

Assume the following building heights (i.e. this will be dictionary number 3):
 Petronas Towers - 1483 ft
 WTC - 1776 ft
 Eiffel Tower - 1083 ft
 
 Write a for-loop that prints out the country, abbreviation, city, building, and height converted to au (assume 1 foot = 2.0375e-12 au):
 
 ```
 The tallest building in the city of Paris, FR is the Eiffel Tower with a height of 2.207e-09 au in the city
The tallest building in the city of New York, USA is the WTC with a height of 3.619e-09 au in the city
The tallest building in the city of Kuala Lumpur, MY is the Petronas Towers with a height of 3.022e-09 au in the city
 ```