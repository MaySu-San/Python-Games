import random;
playmethod=int(input('1.Play customized?\n2.Play with times\n Just press 1 or 2\n'));
if playmethod==1:
    times=0;
    while True:

        choice =input("Roll the dice? y/n:").lower();
        if choice=='y':
            dice1=random.randint(1,6);
            dice2=random.randint(1,6);
            print(f'({dice1},{dice2})')
            times+=1
        elif choice=='n':

            print(f'You plays {times} times . Thanks for playing')
            break
        else:
            print("Invalid choice")

elif playmethod==2:
    playTime=int(input("How many times do you want to roll? "))
    
    for n in range(1, playTime+1):
        print(f'Rolling for ({n}) times ')
        print(f'({random.randint(1,6)},{random.randint(1,6)})')
else :
    print("Invalid only choose 1 or 2")