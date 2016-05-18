# applyCipher.py
# A proram to encrypt/decrypt user text
# using Caesar's Cipher 
# 
# Author: rc.velasquez.juan [at] leadps.org
# makes a mapping of encoded alphabet to decoded alphabet 
# arguments: key
#returns: dictionary of mapped letters
def createDictionary(key):
	
	# placeholder
	return{}

# gets the incrypted message from the user
# arguments: none
# returns: encoded message 
def getMessage():
	pass

# for each letter in message, decodes and records
# arguments: encoded message, dictionary
# returns: decoded message 
def decodeMessage(encoded message, dictionary):
	pass

# outputs the message to the terminal
# arguments: decoded message 
# returns: none 
def printMessage(message):
	pass


# execution starts here

# ask user for key
print("What key would you like to use to decode?")
key = int(raw_input())

dictionary = createDictionary(key)
encodedMessage = getMessage()
decodedMessage = decodedMessage(encodedMessage, dictionary)
printMessage(decodedMessage) 
