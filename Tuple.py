#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
mytuple = ("apple", "banana", "cherry")
print(mytuple)
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created
print(len(mytuple))

#To create a tuple with only one item, you have to add a comma after the item
thistuple = ("applle",)
print(type(thistuple))

thistuple = ("applle")#reconized as a string
print(type(thistuple))

#Using the tuple() method to make a tuple
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#Access Tuple Items
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple[1])
print(thistuple[-1])
#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])#2 (included) and end at index 5 (not included)
print(thistuple[:4])
print(thistuple[2:])
