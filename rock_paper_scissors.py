import random
game =["Rock","Paper","Scissors"]
i=1
while i>0:
  user = input("Please, enter either Rock - Paper - Scissors ")
  comp = random.sample(game,1)
  compa = comp[0]
  compa = compa.lower()
  user = user.lower()
  print("User selection %s" %user)
  print("Computer Random generator %s" %compa)
  if compa == user: print("Tie Game")
  if ((compa == "rock" and user == "paper") or (compa == "scissors" and user == "rock") or (compa == "paper" and user == "scissors")): print ("Congratulation you won")
  if ((compa == "paper" and user == "rock") or (compa == "rock" and user == "scissors") or (compa == "scissors" and user == "paper")): print("You lost")
  if ((user != "rock") and (user != "paper") and (user != "scissors")):break