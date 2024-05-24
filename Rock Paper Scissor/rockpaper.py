import random
print("!! WELCOME TO ROCK PAPER SCISSOR GAME BY Pankaj Sharma!!")
print("________________________________________________________________\n")
print("""INSTRUCTIONS\n1)IF YOU WIN YOU WILL EARN 50+ SCORE\n2)IF YOU LOSE, SCORE WILL BE -20 points""")
computer_choices = [3, 2, 1]
round = 1
score = 0


while True:
  print("_________________________________________________________________")
  print(f"\nROUND : {round}\n")
  computer_choice = random.choice(computer_choices)
  user_choice = int(input("Enter number Rock(1) Paper(2) Scissor(3): "))

  computer = "Rock" if computer_choice == 1 else "Paper" if computer_choice == 2 else "Scissor"
  user = "Rock" if user_choice == 1 else "Paper" if user_choice == 2 else "Scissor"
  
  
  while user_choice < 1 or user_choice > 3:
    print("Please enter a valid number:\nRock(1)\nPaper(2)\nScissors(3)\n")
    user_choice = int(input("Enter number Rock(1) Paper(2) Scissor(3): "))
    user = "Rock" if user_choice == 1 else "Paper" if user_choice == 2 else "Scissor"
  else:
    if user_choice == computer_choice:
      print(f"\nIt's a tie!!\nScore : {score}\n")
      print(f"YOUR CHOICE : {user}\nCOMPUTER CHOICE : {computer}\n")
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
      score = score + 50
      print(f"\nYou win!!\nScore : {score}\n")
      print(f"YOUR CHOICE : {user}\nCOMPUTER CHOICE : {computer}\n")
    else:
      score = score - 20 if score > 20 else score
      print(f"\nYou lose!!\nScore : {score}\n")
      print(f"YOUR CHOICE : {user}\nCOMPUTER CHOICE : {computer}\n")
    
  play = input(f"\nWant to play another round (Yes/No) :- ")
  while play != "yes" and play != "no":
    print("Invalid Input Enter Yes/No\n")
    play = input(f"\nWant to play another round (Yes/No) :- ")
  if play.lower() == "no":
    print(f"Total Score : {score}")
    print("Thanks for Playing !!")
    break
  round = round + 1

  
