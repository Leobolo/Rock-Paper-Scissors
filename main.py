import random

#taking the name of user as the player
print("Welcome")
name= input("Enter your name: ")
print("Welcome "+ name)
option=["R","P","S"]


while True:
    #checking the user input
    while True:

     choose= input('''pick one option between R, P, S,:
      "R" for "rock",
      "P" for "papper",
      "S" for "scissors" 
      ''')
     choose=choose.upper()
     print (choose) 
     if choose not in option:   
      print('Choice not in option')
     else: break;

      #Players and Computer choice
    if choose == "R":
       playerChoice = "Rock"
    elif choose == "P":
      playerChoice = "Paper"
    elif choose =="S":
      playerChoice = "Scissors"
    computer=random.choice(option)
    if computer == "R":
       computerChoice = "Rock"
    elif computer == "P":
      computerChoice = "Paper"
    elif computer =="S":
       computerChoice = "Scissors"
    print("{a} ({b}) : CPU ({c})".format(a ="player",b =playerChoice, c=computerChoice))

 
    if  playerChoice == computerChoice:
      print("It is a tie")
    else:break;


if choose =="R":
  if computer == "P":
    print("Computer is the winner")
  elif computer == "S":
      print(name + " is the winner")
elif choose =="P":
  if computer == "S":
    print("Computer is the winner")
  elif computer == "R":
      print(name + " is the winner")
elif choose =="S":
  if computer == "R":
    print("Computer is the winner")
  elif computer == "P":
      print(name + " is the winner")