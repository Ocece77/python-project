def email_slicer() -> None:
    while True:
        email_user = input("Please enter your email address: ")
        if "@" in email_user:
            user, domain = email_user.split("@")
            if "." in domain:
                domain, ext = domain.split(".")
                break  # If both "@" and "." are present, break out of the loop
            else:
                print("Invalid email address. Domain must contain a '.'. Please try again.")
        else:
            print("Invalid email address. Please try again")

    print(f'The username is: {user}\n The domain is: {domain}\n The extension is: {ext}')


email_slicer()

