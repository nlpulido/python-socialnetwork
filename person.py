class Person:
	def __init__(self, username, password, statusUpdates, friends): # initializes person objects
		self._username = username
		self._password = password
		self._statusUpdates = statusUpdates
		self._friends = friends

	def __str__(self): # returns strings of person objects
		return(str(self._username) + ', ' + str(self._password) + ', messages, ')

	def postStatusUpdate(self, newStatusUpdate): # adds a status update to a list of status updates
		self._statusUpdates.append(newStatusUpdate)

	def addFriend(self, friend): # adds friend to list of friends
		self._friends.append(friend)

	def getUsername(self): # returns username
		return(self._username)

	def getFriends(self): # returns list of friends
		return(self._friends)

	def getPassword(self): # returns password
		return(self._password)

	def getStatusUpdates(self): # returns status updates
		return(self._statusUpdates)
