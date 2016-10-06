##########################
# if-statement
##########################

if <condition1>:
	<statements>
elif <condition2>:
	<statements>
else:
	<statements>

#-> <conditions> = any expression evaluated to True or False
#-> <statements> = any number of instructions
# indentation is part of the syntax
# elif and else are optional

# if...elif...elif...else
# => not the same as if...if...if... => when one True, not get through the other
# if all if/elif false => else statements executed

##########################
# comparisons
##########################

# Comparison operators
# >, <, >=, <=   	-> compare numbers
# !=, ==  		-> compare the contain
# is, is not		-> compare the reference

x = [1,23,45]
y = x[:]	# y is a copy of x
y==x 		# True, they have the same values
y is x		# False, they are different objects
y = x
y is x		# True

# None, False, 0, 0.0, "", (), {}, [], set(())	-> assumed False
# everything else is assumed True

# Resulting expressions are not necessarily Booleans !
1 or 5  # -> 1
0 or 5  # -> 5

z = 0
z==0 and 3   # -> 3	
z==0 or 3    # -> True
z==1 and 3   # -> False
z==1 or 3    # -> 3

# Not reverses an expression
not 0   # -> True
not 5   # -> False

# Logical expressions: shortcuts
x = 1
x and "Yes" or "No"	# -> "Yes"
x = 0
x and "Yes" or "No"	# -> "No"
# => same as:
"Yes" if x else "No"

x or y 	# y evaluated only if x False
x and y # y evaluated only if x True

a!=b
# is the same as
not a==b

# precedence
x = y = 0
z = 1
x and (y or z)
(x and y) or z

##########################
# try-statement
##########################

x = raw_input("Enter a number:")
try:
	num = int(x)
except:
	print("This is not a number.")
	quit()
else:
	print(str(num**2))

# try is a way to handle error -> catches an expression
# raised by an error and recovers gracefully
# if error -> do "except:" if not error -> do "else:"

##########################
# for-loop
##########################

nt = ['A', 'C', 'G', 'T']

# loop via the value

for i in nt:
	print(i)

# for dictionaries: i would be assigned to the keys of the dictionaries
# looping for sets and dictionaries (unordered collections) will happen
# in an arbitrary order

range(5) 	# -> [0,1,2,3,4]
range(2,5)	# -> [2,3,4]
range(2, 13, 3)	# -> [2,5,8,11]
range(7,2,-2)	# -> [7,5,3]

# loop via the position

for i in range(len(nt)):
	print(nt[i])


# access value and position at once: enumerate() -> position and value

vec1 = (4,7,9)
vec2 = (1,3,5)
dot_product=0

for i, x in enumerate(vec1):
	dot_product = vec2[i]*x

##########################
# while-loop
##########################

# keep doing while condition is True
nt = ['A', 'C', 'G', 'T']
i = 0
while i < len(nt):
	print(nt[i])
	i += 1

# careful: if statement never False -> infinite loop
# good if not an initial collection of elements to loop over
# i defined before-hand
# increment i within the loop

# You can add else: after a while loop to indicate that the loop is finished

##########################
# skipping and breaking loops
##########################

nt = ["A", "T", "C", "G"]

for nuc in nt:
	if nuc=="C":       
		continue	# skip the rest of the code for this particular iteration
	print(nuc)

for nuc in nt:
	if nuc=="C":       
		break		# causes all looping to finish
	print(nuc)

##########################
# list comprehension
##########################

squares = []
for x in range(1,8):
	squares.append(x*x)

# more efficient alternative using list comprehension:

squares = [x*x for x in range(1,8)]

##########################
# looping tips
##########################
# bad idea to alter the number of elements in a loop

num = list(range(9))
for n in num:
	if n<5:
		num.remove(n)
print(num)
# does not work as expected

# => duplicate the list to get the expected result:
for n in list(num):   # create a new list similar to num
	if n<5:
		num.remove(n)
print(num)

# => or use list comprehension
num = [n for n in num if n>=5]

#=> or use a second list explicitly
num2 = []
for n in num:
	if n>=5:
		num2.append(n)
num = num2
