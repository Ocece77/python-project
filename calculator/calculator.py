def calculator():
    r = 0
    e = True
    while e:
        # Ask and verify the user numbers
        try:
            n1 = float(input("Enter your first number: "))
            n2 = float(input("Enter the second number: "))
            e = False
        except ValueError:
            print("Only enter an integer or a float, please.\n")

    # Ask and verify the user operators
    op = ""
    while op != "+" and op != "-" and op != "*" and op != "/":
        op = input(
            "\nChoose one of these operators:\n\naddition (+)\nsubtraction (-)\nmultiplication (*)\ndivision (/)\nEnter your choice here: "
        )

    match op:
        case "+":
            r = n1 + n2
        case "-":
            r = n1 - n2
        case "*":
            r = n1 * n2
        case "/":
            if n2 == 0:
                print("You can't divide by zero... bruh")
            else:
                r = n1 / n2

    # Print the result
    print(f'The result of your {n1} {op} {n2} is {r}')


calculator()
