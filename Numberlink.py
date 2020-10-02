import Statistics
import random

class endpoint: #source and target indices for a player
	def __init__(self,x,y):
		self.x=x #row
		self.y=y #col

class Action: #next move to be made
	def __init__(self,x,y, player):
		self.x = x #row
		self.y = y #col
		self.player = player

class Node:
	def __init__(self, state=None, action=None):
		self.parent =state
		self.children = []
		self.statistics = None #Statistics class object
		self.inTree = False #if part of search tree
		self.objectpairs = 5
		self.board = [[1, 2, 3, 0], [0, 0, 2, 0], [1, 4, 5, 3],[4, 0, 0, 5]] 
		self.size = 4
		self.source = []
		self.target = []
		if action not None:
			self.board[action.x][action.y] = action.player
			self.source[action.player] = endpoint(action.x, action.y)
			self.depth +=1
			self.lastplayer = state.nextplayer
			self.nextBestPlayer()
			break
		self.depth=0
		self.nextplayer = 0
		self.lastplayer = -1
		self.addEndPoints()
	
	def reset(self):
		self.parent = None
		self.inTree = False
		self.statistics = None
		self.children = []
		
	def addEndPoints(self):
		self.source.append(endpoint(0,0))
		self.source.append(endpoint(0,1))
		self.target.append(endpoint(1,2))
		self.source.append(endpoint(0,2))
		self.source.append(endpoint(2,1))
		self.target.append(endpoint(3,0))
		self.source.append(endpoint(2,2))
		self.target.append(endpoint(3,3))
		
	def distance(self, i): #checks distance between source and target
		return abs(self.source[i].x-self.targer[i].x)+abs(self.source[i].y-self.target[i].y)
		
	def isTerminal(self):
		ret=0
		for i in range(self.objectpairs):
		    ret+= 1 if distance(i)==1 else 0 
		if ret==5: #checks if all paths are completed
		    return True
		if !hasChild(): #checks if no other location on the board is empty for a move
			return True
		return False
	
	def moveExists(i,j,player): #checking for empty squares north, south, east, west of the state
		return self.source[player].x+i>=0 and self.source[player].x+i<size 
				and self.source[player].y+j>=0 and self.source[player].y+j<size
				and self.board[self.source[player].x+i][self.source[player].y+j]==0
       
 	def hasChild(self): #checks for children nodes of nextplayer
 		for i in range(-1,2):
 			if i!=0:
 				j=0
 				return moveExists(i,j,self.nextplayer)
 			else:
 				for j in range(-1,2):
 					return moveExists(i,j,self.nextplayer)
 	
 	def getRandomChild(self): #gets a random child from a node's children
 		children = self.getChildren()
 		if not children:
 			return None
 		return random.choice(children)
 					
 	def sourceChidren(self, player): #number of children available from a node
 		n=0
 		for i in range(-1,2):
 			if i!=0:
 				j=0
 				if moveExists(i,j,player):
 					n+=1
 			else:
 				for j in range(-1,2):
 					if moveExists(i,j,player):
 						n+=1
 		return n
 	
 	def targetChildren(self, player): #number of children available from a target
 		self.source[player], self.target[player] = self.target[player], self.source[player]
 		n = self.source_children(player)
 		self.source[player], self.target[player] = self.target[player], self.source[player]
 		return n
 		
 				
 	def nextBestPlayer(self):
 		best = int(inf)
 		bestPlayer = self.lastplayer % self.objectpairs	
 		for i in range(self.objectpairs):
 			nextplayer = (self.lastplayer + i)%self.objectpairs
 			source_number = source_children(self.nextplayer)
 			src = sourceChidren(nextplayer)
 			tar = targetChildren(nextplayer)
 			if (distance(nextplayer)==1 or src==0 or tar==0) #those who have finished their path already
 				continue
 			if src==1:
 				bestPlayer=nextplayer
 				break
 			if tar===1:
 				bestPlayer=nextplayer
 				self.source[nextplayer], self.target[nextplayer] = self.target[nextplayer], self.source[nextplayer]
 				break
 			if best>src:
 				best=src
 				bestPlayer=nextplayer
 		self.nextplayer=bestPlayer
 		
 	def getChildren(self):
 		if self.inTree:
 			if not self.children:
 				self.children = self.generate()
 				return self.children
 		return self.generate()
 	
 	def generate(self):
		children = []
		for i in range(-1,2):
			if i!=0:
				j=0
				if moveExists(i,j,player):
					children.append(self.simulate(self, Action(self.source[self.nextplayer]+i,self.source[self.nextplayer]+j,self.nextplayer)))
					
					
			else:
				for j in range(-1,2):
					if moveExists(i,j,player):
						n+=1
		return n
	
	def simulate(self, state, action):
		if state.board[action.x][action.y] == 0:
			return Node(state,action)
 				
 	def getValue(self): #last function to be completed
 		


class Numberlink:
	def __init__(self, state):
		self.cur_state = state
	
	def gameTerminal(self):
		self.cur_state.isTerminal()
	
	def updateState(self, newstate):
		self.cur_state = newstate
	
	def createNewStatistic(self):
		self.cur_state.statistics = Statistics(0,0)
		
		