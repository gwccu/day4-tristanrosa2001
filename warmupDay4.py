# File name: warmupDay4.py
from random import randint
player = input("rock(r), paper(p) or scissors(s)?")
print(player, "vs", end=" ")
chosen = randint(1,3)
if chosen == 3:
    computer = "r"
elif chosen == 1:
    computer = "p"
else:
    computer = "s"
print(computer)
if player == computer:
    print("Draw!")
elif player == "r" and computer == "s":
    print("Player Won!!!")
elif player == "s" and computer == "r":
    print("Computer Won!!")
elif player == "p" and computer == "s":
    print("Computer won")