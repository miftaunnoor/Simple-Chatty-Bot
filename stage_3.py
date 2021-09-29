print('Hello! My name is Mifta.')
print('I was created in 2021.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
num_1= int(input())
num_2= int(input())
num_3= int(input())
your_age= (num_1 * 70 + num_2 * 21 + num_3 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")