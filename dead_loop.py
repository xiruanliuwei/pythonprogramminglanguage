
while True:
	try:
		x = int(input("please enter a number:"))
		# break

	except ValueError:
		print("oops, that was not a valid number, try again...")

	else:
		print("%d is a valid number!" %x)
		break
