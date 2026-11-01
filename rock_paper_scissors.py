import random;

ROCK='r'
SCISSORS='s'
PAPER='p'

emojis={ROCK:'🪨',PAPER:'📜',SCISSORS:'✂️'} 
# print(emojis)
choices=tuple(emojis.keys())

def get_user_choice():
        while True:
            your_choice=input("Choose rock, paper or scissors, r/p/s: ").lower()
            if your_choice not in choices:
                print("Invalid input! ⚠️")
                continue
            else:
                return your_choice

def display(your_choice, computer_choice):
     print(f'Your choice is {emojis[your_choice]}')
     print(f'Computer choice is {emojis[computer_choice]}')

def determine_winner(your_choice, computer_choice):
        if your_choice==computer_choice:
             print('Tie!')
        elif(
             (your_choice==ROCK and computer_choice==SCISSORS) or
             (your_choice==SCISSORS and computer_choice==PAPER) or
             (your_choice==PAPER and computer_choice==ROCK)
         ):
             print('You Win 👑')
        else:
             print('You Lose 😔')

def continue_play():
         while True:
            playContinue=input('Do you wanna play continue ? (y/n): ').lower()
            if playContinue=='n':
                return False
            elif playContinue=='y':
                 return True
            else:
                 print("Invalid ❌")

def play_game():      
    while True:
        your_choice=get_user_choice()

        computer_choice=random.choice(choices)
        
        display(your_choice, computer_choice)

        determine_winner(your_choice, computer_choice)

        if not continue_play():
            print("Thanks for playing! 👋")
            break

play_game()