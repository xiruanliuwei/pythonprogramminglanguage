
import os

def printStars():
	print("******************************")

#Get current directory
print("Current Directory:")
print(os.getcwd())
printStars()

#List directory
print("List Directory: .")
print(os.listdir("."))
printStars()

#Remove a file
#os.remove()

#Change current directory to a specified directory
os.chdir("/home/liuwei")
print(os.getcwd())
print(os.listdir(os.getcwd()))
printStars()

#os.path
print("/home/liuwei is a file?")
print(os.path.isfile("/home/liuwei"))

#os.path
print(os.path.dirname("/home/liuwei/Desktop"))
print(os.path.basename("/home/liuwei/Desktop"))
# os.path.join(path, name)

# os.walk(path)
# root, dirs, files = os.walk("/home/liuwei")  # ValueError: too many values to unpack (expected 3)
# print(root)
# print(dirs)
# print(files)

# x = os.walk("/home/liuwei")
# print(type(x))  -> <class 'generator'>

# for root, dirs, files in os.walk("/home/liuwei/Codes/pythonprogramminglanguage"):
# 	print(type(root), root)
# 	print(type(dirs), dirs)
# 	print(type(files), files)




