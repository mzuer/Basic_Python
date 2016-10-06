##########################
# function use and definition
##########################
# maximal code reuse
# procedural decomposition of the problem

def func_name(arg1, arg2):
	<statements>

# usually returns an object but can also have side effect
# when called, execution flow transfers to the function
# when finished, control returned to instruction following the call


# Function with side effect
# no return value, only side effect
def hello():
	print("Hello world")

# Function returning a value:
# return statement to return the value
# exits the function
def mult(x,y):
	return(x*y)

a = mult(2,3) 		#6
a = mult("bla", 2)	#"blabla"

# Polymorphism:
# -> arguments type not defined in function definition
# -> arguments and return values have no type constraints
# -> will work as long as operations are defined on the objects passed as arguments

# Position
# -> can be defined anywhere
# -> must be defined before use
# -> def creates function object, that can be reassigned to a new name

times = mult
print(times(2,3))

# Modifying argument value: mutable objects
def func(x):
	x[0] = 5
L = [1,2]
func(L)
print(L) 	# [5,2]  # if tuple: error
# -> mutable objects if passed as arguments can be modified in the body of a function
# -> mutable objects are passed by reference

def func(a,b):
	(a,b) = (b,a)
(x,y) = (2,3)

func(x,y)
print((x,y))  # (2,3)
# -> immutable objects are passed by value, use the return value to modify them

def func(a,b):
	return (b,a)
(x,y) = (2,3)	
z = func(x,y) # -> value of z: (3,2)


# Scope of variable
# - variables defined within a function are only accessible inside it
# - scope limited to the body of the function
# - local variables disappear from memory when a function is exited
# e.g. a defines in the main program, not same a as defined in a function

# Local variables
# - any assignment within a function makes the assigned variable local
# - otherwise, a variable not assigned in a function is considered as global
# - scope limited to the programe it is defined in (-> need import statement)

# Priority between nested scopes
# - search sequence: local scope then global one
# - 3d level: built-in scope (e.g. reserved words like str, int, etc.)
# - possible to reuse them in local scope:
def func():
	open = 3		# possible
	open("file.txt") 	# will not work !
# => better not to use reserved words !

# Global variables
def func():
	global x
	x = 2
x = 99
func()
print(x) 	# -> 2
# but not recommended !

# Functions arguments:
# - should be called with the right number of arguments (given in the definition)
# - arguments are matched by position

def func(name, age, job):
	print("%s is %d years old and is a %s" %(name, age, job))

func("Joe", 32, "teacher")
func(name="Joe", job="teacher", age=32)

def func(name, age, job="doctor"):	# with default values
	print("%s is %d years old and is a %s" %(name, age, job))

func("Allan", 45)
func("Allan", 45, "lawyer")

# Arbitrary numbers of arguments
def func(*args):
	print(args)

# pack a collection of arguments into tuple
# in the body of the function, args becomes a tuple with all
# the argument passed to the function

def func(item, *args, **kw):
	print("Mandatory argument: ", item)
	print("Unnamed argument: ", args)
	print("Keyword dic: ", kw)

# in the body of the function, args becomes a tuple with all
# the argument passed to the function and kw a dictionary
# additional arguments passed without "=" -> args
# additional arguments passed with "=" -> kw

func("Hello", 1,2,3,4,var1="a", var2="b")
	# Mandatory argument: Hello
	# Unnamed argument: (1,2,3,4)
	# Keyword dic: {"var2":"b", "var1":"a"}   -> unordred (dic!)


# Unpacking collection
# * can be used when calling a function: unpacks a 
# sequence into a collection of arguments
def func(*val):                 # func should be called with unpacked arguments 
	x = 0			# the function itself packs the elements
	for y in val:
		x+=y
	return (x)

func(1,2,3)   # 6

a = (1,2,3)   # a is a tuple
func(*a)      # unpack the tuple for calling the function [func(a) => error]

b = [2,3,5]
func(*b)

# Recursivity = a function can be defined through itself

def factorial(n):
	if n==1:
		return (1)
	else:
		return (n*factorial(n-1))

# A function can also be passed as argument
def add(x, y):
	return (x+y)

def mult(x,y):
	return (x*y)

def combine(f, *args):
	a = args[0]
	for b in args[1:]:
		a = f(a,b)
	return (a)

t = (1,2,3,4)
v = combine(add, *t)   # v is the sum: 10
v = combine(mult, *t)  # v is the product: 24

# map function
# => very efficient way to apply a function on all elements of a list
def func(x,y):
	x+y

L1 = [1,2,3]
L2 = [3,4,5]
L3 = map(f, L1, L2) 	# [4,6,8]
