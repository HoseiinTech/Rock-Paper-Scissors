import random

print("rock...paper...scissor")

lap = int(input("please return lap ?"))

for num in range(1,lap+1):
       user = input("please return your choise?")
       number = random.randint(1,3)
       player = ""
       if number == 1 :
              player = "rock"
              print("player choise rock")
       elif number == 2 :
              player = "paper"
              print("player choise paper")
       elif number == 3 :
              player = "scissor"
              print("player choise scissor")
       if player == "rock" and user == "paper":
              print("!you win!")
       elif player == "rock" and user == "scissor":
              print("!player win!")
       elif player == "papar" and user == "rock":
              print("!player win!")
       elif player == "paper" and user == "scissor":
              print("!you win!")
       elif player == "scissor" and user == "paper":
              print("!player win!")
       elif player == "scissor" and user == "rock":
              print("!you win!")
       else:
              print("equls !!!")
