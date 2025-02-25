import random
options=("rock","paper","scissor")
player=None
comp=random.choice(options)

while player not in options :
   player=input("entre a choice (rock,paper,scissor) :")

print(f"player : {player}")
print(f"comp : {comp}")

if player == "rock" and comp == "scissor":
   print("you win ")
elif player==comp :
   print(" tie")
elif player == "paper" and comp == "rock":
   print("you win")
elif player=="scissor" and comp == "paper":
   print("you win")

else:
   print("you loose try again !")