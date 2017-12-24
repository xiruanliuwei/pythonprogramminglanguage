
def add(x):
	x = x + 1
	return x #this statement is necessary, without this statement, val is nonetype

val = add(2)
print("val is: %d" %val)

# str = add("xxx") #it is incorrect, because \"Can't convert 'int' object to str implicitly\"
# print("str is: %s" %str)

flo = add(3.8) #it works here
print("flo is: %f" %flo)

