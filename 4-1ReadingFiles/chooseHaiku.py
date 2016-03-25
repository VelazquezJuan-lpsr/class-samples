import time

print("Hi, welcome to the Haiku Reader!") 
print("Choose...") 
print("(3) For a haiku about a silly person.") 
print("(4) For a haiku about writing haikus.")	
choice = input()
if choice == 3:	
	myThirdhaiku = open('haiku3.txt', "r")
	print(myThirdhaiku.read())
else:
	myFourthhaiku = open('haiku4.txt', "r")
	print(myFourthhaiku.read())

if choice == 3:
	myThirdhaiku.close()
else:
	myFourthhaiku.close()
