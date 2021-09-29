print('Hello! My name is Mifta.')
print('I was created in 2021.')
print('Please, remind me your name.')

name = input()

print(f"What a great name you have, {name}!")
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

your_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

number = int(input())
for i in range(number+1):
    print(f'{i} !')

print('Completed, have a nice day!')