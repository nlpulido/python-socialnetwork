import person
def main():
	inputFile = open('network.txt', 'r') # opens up network.txt for read
	network = inputFile.readlines()
	listOfUsers = []
	listOfObjects = []
	x = 0

	for user in network: # splits each line by commas 
		user = user.split(", ")
		listOfUsers.append(user) # appends each account to a list of users

	for account in listOfUsers: # for each account in the list of users
		friendList = []
		messageList = []
		itemIndex = 0
		itemIndexTwo = 0
		while itemIndex >= 0: # creates a temp list of friends
			if itemIndex == len(account):
				break
			if "friend" in account[itemIndex]:
				itemIndex = itemIndex + 1
				while account[itemIndex] != "\n":
					friendList.append(account[itemIndex])
					if account[itemIndex] == account[-1]:
						break
					itemIndex = itemIndex + 1
			else:
				itemIndex = itemIndex + 1
		while itemIndex >= 0: # creates a temp list of messages
			if "friend" in account[itemIndexTwo + 1]: # if friend is in the current account, break
				break
			elif "messages" in account[itemIndexTwo]: # if messages is hit with the index
				itemIndexTwo = itemIndexTwo + 1
				while account[itemIndexTwo] != "friends": 
					messageList.append(account[itemIndexTwo]) # appends the current message to the temp list of messages
					if "friend" in account[itemIndexTwo + 1]:
						break
					itemIndexTwo = itemIndexTwo + 1
			else:
				itemIndexTwo = itemIndexTwo + 1
		newObject = person.Person(account[0], account[1], messageList, friendList) # creates a person object for each account in List Of Users
		listOfObjects.append(newObject) # Appends each person object to a list of Objects

	userNameInput = input("Enter a username.") # asks user to input password and username to access account
	passWordInput = input("Enter a password.")

	for p in listOfObjects: # checks through each person objects for password and username verification
		if userNameInput == p.getUsername() and passWordInput == p.getPassword():
			print("Success! Logged In!")
			while x >= 0: # while loop of menu
				print("""
					Social Network Manager
					1. Print all my friends.
					2. Print all my messages/status updates.
					3. Post a message/status update.
					4. Print all my friends' messsages/status updates.
					5. Add a Friend
					6. Logout (Change User)
					7. Exit
					""")
				userChoice = input("Pick an Option!") # asks user for an option
				if userChoice == "1": # prints all friends of the current user
					myFriends = p.getFriends()
					for friend in myFriends:
						print(friend)
				elif userChoice == "2": # prints status updates of current user
					myMessages = p.getStatusUpdates()
					for message in myMessages:
						print(message)
				elif userChoice == "3": # posts a new message for the user
					newUpdate = input("Enter a message to post!")
					p.postStatusUpdate(newUpdate)
				elif userChoice == "4": # prints the messages of the current user's friends
					myFriends = p.getFriends() 
					listOfFriends = []
					for friend in myFriends: # iterates through the friends list of the current user
						for y in listOfObjects: # checks through the list of person objects for the friend
							if friend == y.getUsername(): # if the current friend is the current person in the list of objects
								friendMessages = y.getStatusUpdates() # get status updates of the current person objects
								for message in friendMessages: 
									print(message) # prints each message of the current friend 
				elif userChoice == "5": # adds the name of the friend to the current user's friend list
					friend = input("Enter the name of the friend you want to add.")
					p.addFriend(friend)
				elif userChoice == "6": # logs out of current user and logs into the new user
					print("Logged out.")
					userNameInput2 = input("Enter a username.")
					passWordInput2 = input("Enter a password.")
					for np in listOfObjects:
						if userNameInput2 == np.getUsername() and passWordInput2 == np.getPassword():
							p = np 
							print("Success, Logged in!")
							x = x + 1
				elif userChoice == "7": # Exits the menu
					inputFile.close() # closes file for reading
					outfile = open('network.txt', 'w')
					for p in listOfObjects: # checks each person in the list of objects
						outfile.write(str(p)) # writes out the username, password, and message format of each user
						statusUpdates = p.getStatusUpdates() # gets each status update of each user in the list of person objects
						for message in statusUpdates: # for message in list of updates
							outfile.write(str(message)) # writes each message to the network file
							outfile.write(', ') # writes a comma after each friend
						outfile.write('friends, ')
						friends = p.getFriends() # gets each friend of each user in the list of person objects
						for friend in friends: # for friend in list of friends 
							friendString = str(friend) # creates a string of a friend
							friendString = friendString.replace(',', '') # replaces any commas with null 
							friendString = friendString.replace('\n', '') # replaces any new lines with null 
							if friendString == '': # if null is hit, breaks
								break
							outfile.write(friendString) # writes the friend to the network file
							outfile.write(', ') # writes a comma after each friend
						outfile.write('\n') # writes a new line to the network file
					outfile.close() # closes outfile
					break

main()