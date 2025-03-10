#variable declaration
x = 5
y = "Hello, World!"
print(x)
print(y)
#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
#to know the type of a variable
print(type(x))
print(type(y))
print(type(z))
#Strings can be declared with '' or with ""

#assign the same or mutiple  values to multiple variables
x,y,z = 'Orange','Banana','Cherry'
print(x)
print(y)
print(z)
print('________')
x = y = z = 'Orange'
print(x)
print(y)
print(z)

#unpack a collection
print('________')
fruits = ['Orange','Banana','Cherry']
x,y,z = fruits
print(x)
print(y)
print(z)
#to output multiples variables of the same type u can use '+' or ',' 
# but only ',' for different type of variables  
print('________')
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)
x = 5
y = "John"
print(x, y)

#global and local variabes

x = "awesome"

def myfunc1():
  print("Python is " + x)

myfunc1()
print('________')

def myfunc2():
  x = "fantastic"
  print("Python is " + x)

myfunc2()

print("Python is " + x)

#u can use the keyword 'global' 
# to declare a global variable inside a fonction
print('________')
def myfunc3():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc3()

print("Python is " + x)
#print the data type of a variable
x = {"name" : "John", "age" : 36}
y = 1.10
z = -3255522
a = 1

print(type(x))
print(type(y))
print(type(z))
print(type(a))