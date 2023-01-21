#BookBot is a simple program that reads the input from the command line(the input will be a text file) and generates the repord about it.


with open('./books/frankenstein.txt') as f:
	file_contents = f.read();
	#print(file_contents.split(" "))
	#print(len(file_contents))


def no_of_occurence(s):
	s=s.lower()
	out = s.split(" ")
	store = {}
	for string in out:
		for letter in string:
			if letter not in store:
				store[letter]=1
			else:
				store[letter]+=1;


	for x in store:
		print('The Character {x} appears {y} times'.format(x=x,y=store[x]))


no_of_occurence(file_contents)