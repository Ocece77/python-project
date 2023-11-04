'''
"Suppose you borrowed 10,000 euros at an annual interest rate of 5% for 2 years. To calculate simple interest, you can use the formula:"
"I = 10,000 * 0.05 * 2"
'''

def interest_calculator(): #Define a function that calculate the interest
    
    not_number = True
    #Try if the number is valid
    while not_number:
      try :
        init_capital = float(input("Enter the initial amount : "))
        periods = int(input("Enter the number of year amount : "))
        rate_period = float(input("Enter the interest rate per period : "))
        not_number = False
      except ValueError:
            print("Enter a valid number please !")

      else:
         result = round(init_capital * (rate_period * 0.01) * periods)
         print(f'If you borrowed {init_capital}$ at an annual interest rate of {rate_period}% for {periods} {"year" if periods <= 1 else  "years"} is {result}$')



        
interest_calculator()