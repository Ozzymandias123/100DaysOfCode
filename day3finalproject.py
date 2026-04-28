print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************


''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice_left = input('Youre at a cross road, Where do you want to go? Type "left" or "right"\n' ).lower()

# elegimos left or right para llegar al lake
if choice_left == "left":
    choice_wait = input("You've come to a lake. There is and island in the middle of the lake.\n " +
                        'Type "wait" for waiting a boat. Type "swim" to swim across\n').lower()
    # elegimos wait para esperar el bote
    if choice_wait == "wait":
        choice_yellow = input("You arrive at the island unharmed. There is a house with 3 doors.\n" +
                              "One red, one blue and one yellow. Which colour do you choose?.\n").lower()
        # elejimos door yellow
        if choice_yellow == "red":
            print("Burned by fire. Game Over")
        elif choice_yellow == "blue":
            print("Eaten by beasts")
        elif choice_yellow == "yellow":
            print("You've found the treasure. You Win!")
        else:
            print("Game Over.")

    elif choice_wait == "swim" or choice_wait == "Swim":
        print("Attacked by trout")
    

elif choice_left == "right" or choice_left == "Right":
    print("Fell into a hole. Game Over")
