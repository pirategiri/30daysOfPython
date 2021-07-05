#Implementation of queue using collection module python
#Author: Kiran Giri

from collections import deque
#making a new deque with 5 values
d=deque('kiran')

#iterating over deque's item
#converting to uppercase
for elem in d:
	print(elem.upper())

#adding new entry to right side

d.append(' giri ')
print("after aappending",d)

d.appendleft('Hey this is')
print("after adding to left of element")
print(d)

print("converting into list")
print(list(d))

print(" Reversing elements ")
print(list(reversed(d)))

print("rotating the list to right")
print(d.rotate(1))

#emptying deque
d.clear()