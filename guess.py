import random


min = 1
max = 10
target_number = random.randint(min, max)


win = False
while not win:
	guess = int(input('Guess a Number Between {} and {}:'.format(min, max)))


	if guess == target_number:
		win = True
		print('Congrats')
	else: 
		print('You Lose')

