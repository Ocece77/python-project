import time, random # python module

def devinette():
    #Le prompt de base / de bienvenue

    print("Bienvenue dans ce super jeu de devinette")
    time.sleep(1) #Met un pause de 1 seconde grâce au module time
    print("Tu vas devoir deviner de 1 à 100 le chiffre choisit par l'ordinateur")
    time.sleep(1)
    pret = input("Est ce que tu es prêt ?? (Oui / Non) :").lower()

    if pret == "oui":
        print("Okay on démarre !")
    elif pret == "non":
        print("okay je te laisse encore 5 seconde")
        time.sleep(5)
    else:
        print("Ce n'est pas une réponse correcte mais peu importe\nCommençons !")



    veut_rejouer = True

    while veut_rejouer: #Tant que c'est vrai, on rejoue
        essaie = 0  #On initialise le nbr d'essaie de l'utilisateur
        computer_numbers = random.choice([x for x in range(101)]) #choisi un nombre random entre 0 et 100

        while essaie < 8:
            not_number = True #re-demmande SI ce n'est pas un nombre valide
            while not_number:
                try:
                    user_number = int(input("Donne un chiffre et essaye de trouver si c'est le bon 😃 : "))
                    not_number = False
                except ValueError:
                    print("Entre un chiffre entier stupide 🤦🏿‍")
                    not_number = True

            if user_number == computer_numbers:
                print("Bien joué fréro :D")
                essaie = 8
            else :
                if user_number > computer_numbers:
                    print("C'est trop grand :/")
                elif user_number < computer_numbers:
                    print("C'est trop petit :(")
                essaie += 1

            if essaie == 7:
                print("C'est ton dernier essaie :/")

        else:
            print("----------------Loading------------------")
            time.sleep(1)

            #Demande au joueur si il souhaite rejouer
            rejouer = input(f"\nC'était {computer_numbers}\nEst ce que tu veux rejouer ? (Oui / Non) : ").lower()

            if rejouer == "oui":
                essaie = 0
                veut_rejouer = True
            else:
                veut_rejouer = False


devinette()