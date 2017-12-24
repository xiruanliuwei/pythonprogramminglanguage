
accounts = [100, 200, 300, 400]
print(accounts)
print("type(accounts) is: ", type(accounts))
print("id(accounts) is: ", hex(id(accounts)))

def reverseList(x):
	length = len(accounts)
	for index in range(int((length/2))):
		tmp = x[index]
		x[index] = x[length - 1 - index]
		x[length - 1 - index] = tmp
		print("index: ", index)

reverseList(accounts)
print("id(accounts) new is: ", hex(id(accounts)))
print(accounts)

val = 100
print("val id is: ", id(val))
val = 200
print("val id 2 is: ", id(val))

