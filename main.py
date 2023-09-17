import string

phrase = "turn this into a password for me please?"

password = []

words = phrase.split()
first_letters = []

puncs = list(string.punctuation)

streak = 1
current_streak = words[0][0]

for word in words:
	first_letters.append(word[0])

for letter in first_letters:
	try:
		if password[-1] == letter:
			streak +=1
			continue
		else:
			password.append(f"{streak}{letter}" if streak > 1 else letter)
			streak = 1
	except IndexError:
		password.append(letter)	

print(''.join(password))