import random ,time


def roll_dice():
    
  user_answer = input("Do you want to roll the dice\nWrite \"yes\" or \"no\": ").lower()
  if user_answer == "yes":
      print("The dice is rolling")
      time.sleep(2)
      print(f"The dice has stopped, and it's the number: {random.randrange(1, 7)}")
  else:
      print("The program is stopped")

roll_dice()