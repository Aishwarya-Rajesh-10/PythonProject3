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
*******************************************************************************''')
print("Welcome to treasure hunt island.")
print("Your mission is to find the treasure")
choice1=input('You\'re at cross road . where do u want to go?'
                'type "right" or "left".\n').lower()
if choice1=="left":
   choice2 =input ( 'You\'ve come to lale.'
                    'there is an island in the middle of the lake.'
                    'type "wait"to wait for the boat.'
                    'type "swim" to swim across .') .lower()
   if choice2=="wait":
       choice3=input("you arrive at the island un harm."
                     "there is house with 3 dross. one red,"
                     "one yellow and one blue."
                     "which colour do you choose?").lower()
       if choice3== "red":
           print("Its room full of fire>Game over.")
       elif choice3=="yellow":
           print("You found a treasure you win")
       elif choice3=="blue":
           print("You entered room of beets .Game over")
       else:
           print("You have choosen the door that doesnt exist.")
   else:
       print("You got attacked by an angry trout.Game over.")
else:
    print("You fell into a hole.Game over.")


