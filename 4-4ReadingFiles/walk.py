# open the file walking_instructions.txt
walking_file = open('walking_instructions.txt' , 'r')

# let the word duh appear in each line
lineToPrint = walking_file.readline()
while lineToPrint !="":
	print(lineToPrint + ", duh")
	lineToPrint = walking_file.readline()
# close the file
walking_file.close()
