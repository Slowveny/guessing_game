from random import randint
print(f'{ ' GUESSING GAME ':=^50}')
random_number = randint(1, 10)
while True:
    attempt = int(input('Guess the number I thought of from 1 to 10: '))
    if attempt < 1 or attempt > 10:
        print('The number I thought of is from 1 to 10. Please try again!')
        continue
    elif attempt != random_number:
        print('Wrong number, try again!')
        continue
    else:
        print(f'* You got it right! I thought of number {random_number}!')
        
        play_again = input('Would you like to play again (y/n)? ').lower()

        while play_again != 'y' and play_again != 'n':
            print('Maybe you typed it wrong.')
            play_again = input('Would you like to play again (y/n)? ').lower()
        
    if play_again == 'y':
        print('='*50)
        random_number = randint(1, 10)
        continue
    else:
        break
print('Thanks for playing!')
print('='*50)
