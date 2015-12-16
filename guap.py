# find out if user is a value club member
print("Are you a value club member? Respond yes or no.")
club = raw_input()
# find out how many rolls of paper towels usr bought
print("How many rolls of paper towels did you buy?")
rolls = int(raw_input())
# if they're in the club, they get an extra $2
if club == "yes":
	print("in the club")
	if rolls > 10:
		rebate = rolls * .35 + 2
	else:
		rebate = rolls * .25 + 2

else:
	print("not in the club")

# print rebate 
print("Your rebate is $" + str(rebate))

