# Thu Nguyen
# March 20 2022
# Code by "Automate the Boring Stuff with Python"

# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?') # prompt for name input
myName = input()
print('Nice to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?') # prompt for age input
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')