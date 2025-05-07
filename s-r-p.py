#Schere-Stein-Papier
import random


scissors="s"
rock="r"
paper="p"


choices=[rock, scissors, paper]


tie= "tie"
win= "you win"
lose= "you lose"


user_p= 0
pc_p= 0


def game(user_in, computer):
   global user_p, pc_p
   if user_in == computer:
       return tie
   elif user_in == scissors and computer == paper:
       user_p += 1
       return win
   elif user_in == paper and computer == rock:
       user_p += 1
       return win
   elif user_in ==  rock and computer == scissors:
       user_p += 1
       return win
   else:
       pc_p += 1
       return lose
while True:
   user_in=input("Take your choice: (s)cissors, (r)ock oder (p)aper:")
   if user_in not in choices:
       print("only choose (s), (r), or (p)!")
       continue
   computer=random.choice(choices)
   result= game(user_in, computer)


   print (f"You chose {user_in}, Computer chose {computer}. Result: {result}")
   print (f"You have {user_p} points, Computer has {pc_p} points")
   print("\n")


   retry = input("want to retry? - y/n:")
   if retry.lower() != "y":
       print(f"Thanks for playing! Your final points: {user_p}")
       break


#game(user_in, computer)

