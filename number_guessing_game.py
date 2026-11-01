import random
guess_number=random.randint(1,100)
while True:
    try:
        guess=int(input("Guess the number between 1 and 100: "))
        if guess>guess_number:
            print('Too high!')
        elif guess<guess_number:
            print('Too low!')
        else:
            print('Congratulations . You guessed the number')
            break
    except:
        print("Put the valid number! ")