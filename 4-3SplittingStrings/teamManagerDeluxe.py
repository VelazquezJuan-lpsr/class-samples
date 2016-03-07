# creates the class and tells the computer what to print if the option is like that
class player(object):
  def __init__(self, name, age, goals, JerseyNumber, position):
    self.name = name
    self.age = age
    self.goals = goals
    self.JerseyNumber = JerseyNumber
    self.position = position
  def Stats(self):
    print("Name:" + self.name)
    print("Age:" + self.age)
    print("Goals:" + self.goals)
    print("Jersey Number:" + self.JerseyNumber)
    print("position:" + self.position)

  def savefile(playerList, filename):
    TheFile = open(filename, "a")
    for info in playerList:
    	TheFile.write(info.name + " " + info.age + " " + info.goals + " " + info.JerseyNumber +" " + info.position + "\n")
    TheFile.close()
  def loadfile(filename):
     emptyList = []
     myFile = open(filename, "r")
     myLine = myFile.readline()
     while myLine != "":
		myWords = myLine.split()
		print(myWords)
                emptyList.append(Player(str(myWords[0]),str(myWords[1]),str(myWords[2]), str(myWords[3]),str(myWords[4]) + "\n"))
		myLine = myFile.readline()
     myFile.close()
     return emptyList


print("Press 1 to start with a new team or 2 to load an old file you had")
user_choice = raw_input()


if user_choice == "2": 
	print("Enter the file that you names it previously along with '.py' at the end with it")
	filename = raw_input()
	myPlayers = loadfile(filename)
else:
	myPlayers = []
# introduces the code
print("Welcome! Do you wish to add a player to LPS scoccer team or would you like to view the players?") 
print("Enter 1 to add player or enter 2 to view them, 0 to get out.")
# creates an option that the user will input
option = raw_input()
# Makes a loop so that the option can print over and over
if option != "0":
	print(" ")
# If the option is 1 then it will ask the player to add the player info
if option == "1":
	print("Looks like you want to add a player, please enter the information below.")
	print("Name:")
	name = str(raw_input())
  	print("Age in numbers:")
   	age = input()
   	print("Number of goals scored:")
   	goals = input()
   	print("Please enter the Jersey Number for the player:")
   	JerseyNumber = raw_input()
   	print("Please enter the position that they play in:")
   	position = str(raw_input())  
# this here will print a line telling if the user is good or bad depending on the goals they have made.
   	if int(goals) <= 10:
     		print ("Go back to your country and stop playing soccer.")
   	else:
     		print("You should play in the premier league.")
# will add the new player to the list and then ask the user if they want to change the input that they had.
   	myPlayers.append(player(name, age, goals, JerseyNumber, position))
   	print("Done! Do you want to 1, add another player")
    	print("2 to see the players,")
    	print("3 to save the file.")
    	print("0 the get out")
    	option = raw_input()
# If the user decides 2 it will print through this block of code and will print the whole list that it has then it gives the user another option to change the option.
elif option == "2":
    	print("okay looks like you want to see the players.")
    	for information in myPlayers:
        	information.printStats()
    	print("What do you want to do now?") 
   	print("1 to add another player")
    	print("2 to see the players again.") 
    	print("3 to save the file ")
    	print("Press 0 to get out")
    	option = input()
elif option == "3":
    	print("Please pick a file name and add '.txt' to the end of the file. If this is a previous file please add a new name")
    	filename = raw_input()
    	savefile(myPlayers, filename)
    	option = "0"
    	print("Done, goodbye.")
