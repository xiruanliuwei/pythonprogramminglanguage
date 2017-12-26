
def printStars():
	print("*******************")

students = {"203-2012-045":"John", "203-2012-037":"Peter"}
print(type(students))
print(students)
printStars()

#Add an entry
students["203-2012-038"] = "Susan"
print(type(students))
print(students)
printStars()

#Del an entry
del students["203-2012-045"]
print(students)
printStars()

#Iterate all keys
for key in students:
	print(key, " : ", students[key])
printStars()

students["123-2017-001"] = "Kevin"
students["234-2017-002"] = "Antony"

#Iterate all keys in this dictionary
for key in students.keys():
	print(key)
printStars()

#Iterate all values in this dictionary
for value in students.values():
	print(value)
printStars()

#Iterate all entries/items in this dictionary
for entry in students.items():
	print(entry)
printStars()

#Iterate all key-value s in this dictionary
for key, value in students.items():
	print(key, value)
printStars()

#Check the type of the return value of method keys()
print(type(students.keys()))
printStars()
