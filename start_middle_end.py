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
        #to separate the punch lines of the jokes
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
