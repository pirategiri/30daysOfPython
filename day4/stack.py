#Python data structures
#Author: Kiran giri
#Stack using list

class stack():

	#passing list as starting value
	def __init__(self,startVal=[]):
		self.stack=startVal

	#adding element to an empty list

	def push(self,ele):
		self.stack.append(ele)
		return self.stack

	#removing from tail of the list
	def pop(self):
		return self.stack.pop(-1)

	#returns the stack
	def checkStack(self):
		print(self.stack)

	#returns tail element
	def checktop(self):
		print(self.stack[-1])

s=stack([1,2,3,4,5])
print(s.checkStack())







		
