from random import randint
import numpy as np
import os

def say(text): #Function that converts text to speech
	print(text)
	new_text = ''
	for char in text:
		if char not in ["'",'"']:
			new_text += char
		else:
			new_text += '\\' + char
	os.system('say ' + new_text)

def main():
	p = (randint(0,7), randint(0,7)) # Generates two random integers from 0-7 and assigns to p
	i2f = ['a','b','c','d','e','f','g','h'] #Creates a list of letters that will be used for positions.
	position = i2f[p[0]] + str(p[1] + 1) #Generates a position using p and i2f


	os.system('clear') # Clears the screen
	while 1:           # While loop makes sure that input is correct format.
		say('What color is the square at position ' + position + '? Black or white?')
		answer = input('::: ').lower()
		if answer in ['black', 'white']:
			break
		else: 
			say('Sorry, I don\'t think you answered appropriately. Make sure to say \"black\" or \"white.\"')
	
	if (answer == 'white') != (np.sum(p) % 2 == 0):  
		say('Good job!') # If loop tests answer by taking remainder when sum of p is divided by two and seeing if it is not equal to zero. If the input was 'white,' returns 'good job.'' 
	else:
		say('Maybe next time!') 
while 1:
	main()


