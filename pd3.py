# JOKE GENERATOR V1.1
# MADE BY p0isonedpanda

import random
import os

# This is our pool of jokes
j1 = "Why did the chicken cross the road?"
j2 = "To get to the idiot's house"
j3 = "Knock Knock."
j4 = "Who's there?"
j5 = "The chicken."
j6 = "What did the lawyer say to the other lawyer?"
j7 = "We are both lawyers."
j8 = "What did the farmer say when he lost his tractor?"
j9 = "Where's my tractor?"
j10 = "Why did the blonde get fired from the M&M factory?"
j11 = "Repeated absence and stealing."
j12 = "What do you call a priest that becomes a lawyer?"
j13 = "A Father in law."
j14 = "Knock Knock"
j15 = "Who's there?"
j16 = "Ho Ho."
j17 = "Ho Ho Who?"
j18 = "You know your Santa impression could use a little work..."



# Placeholder for raw_input parameter
para = "Press [ENTER] for a joke!\n> "
para2 = "Press [ENTER] for another joke or input 'stop' to end\n>"

# Start up screen
print """"You may call me the...\n\n\n\n\n

 _______           _           _________ _______           _______  _______
(  ____ )|\     /|( (    /|    \__   __/(  ____ \|\     /|(  ____ \(  ____ )
| (    )|| )   ( ||  \  ( |       ) (   | (    \/| )   ( || (    \/| (    )|
| (____)|| |   | ||   \ | | _____ | |   | (_____ | (___) || (__    | (____)|
|  _____)| |   | || (\ \) |(_____)| |   (_____  )|  ___  ||  __)   |     __)
| (      | |   | || | \   |       | |         ) || (   ) || (      | (\ (
| )      | (___) || )  \  |    ___) (___/\____) || )   ( || (____/\| ) \ \__
|/       (_______)|/    )_)    \_______/\_______)|/     \|(_______/|/   \__/


\n
Presented by smp101\n
Version 2.0\n"""

raw_input(para)

# Will let us end the program loop if we need to
i = True

# Main program loop where fun stuff happens
while i == True:

	# Simply clears the screen before a new entry appears
	os.system('cls')

	joke = random.randint(1, 6)

	if joke == 1:
		print j1
		print "-" *10
		print j2
		print "-" * 10
		print j3
		print "-" * 10
		print j4
		print "-" * 10
		print j5
	elif joke == 2:
		print j6
		print "-" * 10
		print j7
	elif joke == 3:
		print j8
		print "-" * 10
		print j9
	elif joke == 4:
		print j10
		print "-" * 10
		print j11
	elif joke == 5:
		print j12
		print "-" * 10
		print j13
	elif joke == 6:
		print j14
		print "-" *10
		print j15
		print "-" * 10
		print j16
		print "-" * 10
		print j17
		print "-" * 10
		print j18

	# Checks if we want more jokes or to close
	close = raw_input(para2)
	if close == 'stop':
		i = False
os.system('cls')
