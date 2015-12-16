print("Welcome to your worst nighmare.(Its a dream)")
print("What will be your characters name?")
name = str(raw_input())
print("Enter strength (1-10):")
strength = int(raw_input())
print("Enter health (1-10):")
health = int(raw_input())
print("Enter luck (1-10):")
luck = int(raw_input())
character = strength + health + luck
if character > 15:
	print("You gave your character too many points!")
	print("Default values have been assinged, " + name )
	print("Strength: 5, health: 5, luck: 5.")
	strength = 5
	health = 5
	luck = 5 
else:
	print(name , strength , health , luck)
print(name + ", you've come to a fork in the road. Do you want to go left or right?")
right = 4
left = 2
path = raw_input()
if path == 4:
	if luck >= 6:
		print(name + ", you were lucky enough to dodge all the falling rocks. You win!")
	else:
		print(name + ", you werent lucky enough to dodge all of the falling rocks. You lose!")
else:
	if strength <= 6:
		print(name + ", you didnt have that much strength to fight the zombies. You lose!")
	else:
		print(name + ", you had enough strength to fight the zombies. You win.")
