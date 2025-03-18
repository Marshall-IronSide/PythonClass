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
