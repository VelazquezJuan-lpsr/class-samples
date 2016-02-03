import time
# open the file that is asked 
myFirstHaiku = open('haiku1.txt', 'r')
# tell the user the user which haiku is it and show them what is in it  
print('Here is the first haiku:') 
print(myFirstHaiku.read())
# tell the user that you will give them the second haiku but ask them how long will they want the lines to take
print('I will give you the second haiku line by line.') 
print('How many seconds should I wait between lines?') 
seconds = int(raw_input())
 
mySecondHaiku = open('haiku2.txt', 'r')
 
lineToPrint = mySecondHaiku.readline() 
while lineToPrint != "":
    print(lineToPrint)
    lineToPrint = mySecondHaiku.readline()
    time.sleep(seconds) 
# close the files that were used and opened
myFirstHaiku.close()
mySecondHaiku.close()
