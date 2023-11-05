import string, random


char = list(string.ascii_letters + string.digits + string.punctuation)
random.shuffle(char)  # Mix the character list
pw = []

def password_genenator():
  not_valid = True 
  password_length = 0
 
  while not_valid : #Test if the user input is valid
    try:
      password_length = int(input("Enter the desired password length (should be at least 4): "))
      if password_length < 4 :  
        not_valid = True
      else:
        not_valid = False
    except ValueError:
      print("Enter a valid number please and superior of 3 \n")

  
  for i in range(password_length):
    pw.append(random.choice(char))
  print("You can use this passord : " ,  "".join(pw))  # Display the generated password


password_genenator()







