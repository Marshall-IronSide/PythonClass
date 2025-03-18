#List is a collection which is ordered and changeable. Allows duplicate members
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(type(thislist))

#Since lists are indexed, lists can have items with the same value
thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)

#determine how many items a list has
print(len(thislist))

#List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

#The list() Constructor to make a List
thislist = list(("apple","banana","cherry")) #double round-brackets

#access a list item
print(thislist[2])
print(thislist[-3])

#range of indexes
#specify where to start and where to end the range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#The search will start at index 2 (included) and end at index 5 (not included)
print(thislist[:4])#the search will end at index 4 (not included)
print(thislist[2:])#The search will start at index 2 (included)
print(thislist[-4:-1])##The search will start at index -4{orange} (included) and end at index -1{mango}(not included)

#Check if Item Exists
if "orange" in thislist:
    print("Yes! 'orange' is in the fruit list")

#change item
thislist[1] = "blackcurrant"
print(thislist)

#change range of items value
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)

#Insert Items
thislist.insert(1,"watermelon")# without replacing any of the existing values
print(thislist)

#add an item to the end of the list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.append("orange")
print(thislist)

#append elements from another list to the current list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#removes a specified item
thislist.remove("orange")#remove the first "orange" of the list
print(thislist)
thislist.remove("orange")
print(thislist)#remove the second "orange" of the list

#Remove Specified Index
thislist.pop(5)#removes the first "mango"
print(thislist)
thislist.pop()#removes the last item "papaya"
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
del thislist[1]#removes "banana"
print(thislist)
del thislist #Delete the entire list
#print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.clear()#clear the content of the list
print(thislist)

#loop List
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#loop through the list items
for x in thislist:
    print(x)
print("_________________")
[print(x) for x in thislist]
print("_________________")
#loop through the list items by referring to their index number
for i in range(len(thislist)):
    print(thislist[i])
print("_________________")
# using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
    
 #List Comprehension
# a new list, containing only the fruits with the letter "a" in the name using for
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = []
for x in thislist:
    if "a" in x:
        newlist.append(x)
print(newlist)
 
#With list comprehension
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = [x for x in thislist if "a" in x]
print(newlist)
#Syntax newlist = [expression for item in iterable if condition == True]
newlist = [ x for x in thislist if x != "apple"]#Only accept items that are not "apple"
print(newlist)

#Iterable (an object that can be looped over)
#create an iterable
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = [x.upper() for x in thislist]
print(newlist)
newlist = ["Hello" for x in thislist]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in thislist] #replace banana with orange
print(newlist)

#Sort Lists
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# sort descending
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.sort(reverse= True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse= True)
print(thislist)

#Customize Sort Function
def myfunc(n):
    return abs(n - 50)# Sort the list based on how close the number is to 50
thislist = [100, 50, 65, 82, 23]
thislist.sort(key= myfunc)
print(thislist)
#Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
#reverse the order of a list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy a List
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = thislist.copy()
print(thislist)

newlist = []
print(newlist)
newlist = list(thislist)
print(newlist)

newlist = []
print(newlist)
newlist = thislist[:]
print(thislist)

#Join or concatenate Lists
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = [23, 89, 12, 45, 67, 78, 34]
mylist = thislist + newlist
print(mylist)

for x in newlist:
    thislist.append(x)#concatenate by appending
print(thislist)
#the extend() method
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = [23, 89, 12, 45, 67, 78, 34]
thislist.extend(newlist)
print(thislist)
