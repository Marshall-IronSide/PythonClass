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
thislist.pop()