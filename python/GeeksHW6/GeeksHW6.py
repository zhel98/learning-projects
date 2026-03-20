while True:

    password = input("Введите свой пароль ('q'-чтобы выйти): ")
    if password == 'q':
         break

    def is_pass_gucci(password) -> bool:
        
            score = 0
            special_counter = 0

            if len(password) < 6:
                return False
            else: score +=1
            if any(character.islower() for character in password):
                score +=1
            if any(character.isupper() for character in password):
                score +=1 
            if any(character.isdigit() for character in password):
                score +=1
            
            for character in password:
                if not character.isalnum():
                    special_counter += 1
            if special_counter >= 2:
                    score +=1
            if score > 4: 
                return True
            else: 
                return False

    if is_pass_gucci(password) == True:
        print("My man ur pass is gucci")
    else:
        print("Fool. Try again")

    