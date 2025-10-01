print(f'{' MULTIPLICATION TABLE - VERSION 2 ':=^50}')
number = int(input('Enter a number: '))
for i in range(10, 0, -1):
    print(f'{number} x {i} = {number * i}')
print('='*50)
