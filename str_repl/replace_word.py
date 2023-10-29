def replace_word():
    
    user_str = input("Enter your sentence : ")
    word_str = user_str.split(" ")

    word_to_replace = input("Enter the word you want to replace: ")
    

    while word_to_replace not in word_str:
        word_to_replace = input("Enter a word that is already in your sentence : ")
        
  
    word_replacement = input("Enter the replacement word: ")
    r =" ".join(word_str).replace(word_to_replace , word_replacement)
    print(r)
        
        


    

replace_word()