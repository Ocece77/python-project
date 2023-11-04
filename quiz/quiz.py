import time

#Kpop Blind Test

#Dictionnary of the question and the answer to the question
questions = {
    "1":{
      "question" : "Which group sing \"Hype Boy\" ?\n\t- MNIXX\n\t- Fithy Fithy\n\t- New Jeans (NJWS)\n Enter your answer here:  ",
      "answer" : "new jeans"
    },
    "2":{
     "question" : "Which group sing \"Nude\" ?\n\t- G-Idle\n\t- Blackpink\n\t- Aespa\n Enter your answer here:   ",
      "answer" : "g-idle"
    },
    "3":{
     "question" : "Which group sing \"Shhh\" ?\n\t- Ive\n\t- Everglow\n\t- Kiss Of Life\n Enter your answer here:  ",
      "answer" : "kiss of life"
    },
    "4":{
     "question" : "Which group sing \"Unforgiven\" ?\n\t- Aespa\n\t- Le Sserafim\n\t- Itzy\n Enter your answer here:  ",
      "answer" : "le sserafim"
    },
    "5":{
     "question" : "Which group sing \"Feel Special\" ?\n\t- Girls Generations(WJSN)\n\t- Red Velvet\n\t- Twice\n Enter your answer here:   ",
      "answer" : "twice"
    },
    "6":{
     "question" : "Which group sing \"Tiger Inside\" ?\n\t- Super M\n\t- NCT 127\n\t- EXO\n Enter your answer here:    ",
      "answer" : "super m"
    },

}

#Print the prompt with delay between each sentence

print("Kpop Quiz")
time.sleep(1)

print("You will have 6 questions about kpop song !")
time.sleep(1.5)

user_mood = input("Are you ready for the first question ?\nEnter Yes or No :  ")
user_mood = user_mood.lower()

if user_mood == "yes":
    print("I love your enthusiasm!")
    time.sleep(1)
elif user_mood == "no" :
    print("Okay! I'll give you 5 seconds before the quiz starts")
    time.sleep(5)
else :
     print("That's not a correct answer, but I'll take it as a yes.")
     time.sleep(1)
print("Okay ! Let's get started!")
time.sleep(1)


score = 0 #initialize the score


#Display and verify each answer

for key, value in questions.items():
    
    user_answer = input(value["question"]).lower()

    if user_answer == value["answer"]:
          score += 1
          print(f"\nCorrect ! \nYour score is {score} / 6\n")
    else :
          print(f"\nIncorrect :c \nYour score is {score} / 6\n")

#Display the final score !

time.sleep(1)
print(f"-----------Loading-----------")
time.sleep(1)
print(f"Your final score is {score} / 6")
time.sleep(1)
print(f"This represent {round((score/6)* 100)} % of good answer\n")
time.sleep(1)

if score  >= 1 and score <= 3:
    print("You can do better ! ")
elif score > 3 and score <= 5:
    print("That's a good score! ")
elif score == 6:
    print("That's PERFECT! ")
else :
    print("You are so bad at this game :/\n You've got no good answer")
    

