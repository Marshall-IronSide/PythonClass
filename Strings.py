#You can use quotes inside a string, as long as they don't match the quotes surrounding the string
print("He is called 'Johnny'")
#go through each charactar in a string, strings are arrays
for x in "banana":
  print(x)
#get a string lengh the keyword is len
a = "Hello word"
print(len(a))
#check if a certain phrase or character is present in a string
txt = "The best things in life are free"
print("free" in txt)
# true if it's present false if not
if "free" in txt:
  print("Yes, 'free' is present.")
#check if a certain phrase or character is present in a string
txt = "The best things in life are free"
print("hush" not in txt)
if "hush" not in txt:
  print("yes hush is not in txt")
  x = 'Welcome'
print(x[3])

#You can return a range of characters by using the slice syntax
b = "Hello world!!"
print(b[1:4])
print(b[:4])
print(b[1:])
b = "Hello, World!"
print(b[-5:-2])

x = 'Welcome'
print(x[3:])

#Upper Case
print(x.upper())
print(b.upper())

#lower case
a = " WELCOME"
b = "HELLO, WORLD!! "
print(a.lower())
print(b.lower())

#remove any whitespace from the beginning or the end:
b = "   HELLO, WORLD!! "
print(b.strip())

#replaces a string with another string
a = " WELCOME"
print(a.replace("W","h"))

#splits the string into substrings 
print(b.split(","))

#combine strings and numbers(F-trings)
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 1000
txt =f"the price of rice is : {price} F CFA"
print(txt)

price = 1000.328823882
txt =f"the price of rice is : {price:.2f} F CFA" # :2.f fix the float to only 2 decimals
print(txt)
txt = f"The price is {20 * 59} F CFA"
print(txt)

#escape characters in python
txt = "We are the so-called \"wikings\" of the north"
 
print(txt)
