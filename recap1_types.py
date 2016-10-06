# Force a reload of a module
import imp
imp.reload(file)

# Importing parts of a module
import myfile
from myfile import a

# List of the function available in a module
dir(math)

# Complex numbers
3 + 4j  # always a coefficient before j

# Binary, octal and hexadecimal representation of 15:
0b1111
Oo17
Oxf

# Basic operators
3 + 6       # 9
3 - 6       # -3
3 * 6       # 18
3 / 6       # 0.5 
6. // 4.    # 1.0
6 // 4      # 1
3 ** 4      # 81
6 % 4       # 2
1 << 2      # 4      => décalage des bits vers la gauche
8 >> 2      # 2      => décalage des bits vers la droite
10 & 6      # 2      => copies a bit to the result if it exists in both operands 
10 | 6      # 14     => copies a bit if it exists in either operand
~10         # -11    =>'flipping' bits (2's complement)

# Convert int <-> float
int(3.8)
float(3)

# Implicit conversion (to higher precision)
3.4 + 7 

# Returns the type of a variable
type(a)

# Precedence rule
** > ~ > * , / , % , // > + , -    [...etc...]

################################################
# Strings
################################################

# Escape sequence
\t   # => horizontal tab
\v   # => vertical tab
\a   # => bell
\b   # => backspace
\r   # => carriage return
\n   # => new line
\f   # => formfeed
\0   # => null byte
\xhh  #=> byte with hexadecimal value hh (e.g. \x66 -> f)

# Length of a string
s = "abcdef"
len(s)

# Overloaded + and *
a = "abc" + "def"
a = "abc"*4

# Strings and numbers cannot be mixed
a = "abc" + 4 # ERROR !

# But can be converted explicitly
a = "abc" + str(4)

# String indexing (begin at index 0)
dna = "AGTCGAT"
dna[0]     # A
dna[-1]    # T  # access from the end with negative number (begin at -1)

# String subscript: slicing
dna[2:4]   # from 2 included to 4 excluded
dna[2:]    # from 2 to the end
dna[:2]    # from beginning to 2 excluded

# Slicing with stride
dna[0::2]  # from 0 'til the end 2 by 2
dna[::-1]  # revert the string

# Strings are immutable
dna[0] = "T" # ERROR ! The object in memory cannot be modified

# But we can create new object
dna = dna[0] + dna  # it's ok because new object is created

# Some strings methods
"AC" in dna              # test if it is contained in the string
"AC" not in dna          # test if not in the string
dna.lower()              # convert to lower case
dna.replace("A", "T")    # replace character(s) by the one(s) given
dna.find("AT")           # return the index of the character(s) if found else -1 
dna.rfind("AT")          # return the index of the character(s) if found else -1 but begin from the right
dna.index("CT")          # return the index of the character(s) if found else raise ValueError 
dna.rindex("CT")         # return the index of the character(s) if found else raise Value Error but begin from the right
dna.strip("A")           # removed if the character is found at the extremities
dna.lstrip("A")          # removed if the character is found at the left extremity
dna.rstrip("A")          # removed if the character is found at the right extremity
dna.split("A")           # split at the given character (return a list)
dna.count("A")           # count the number of occurence of the character

################################################
# Tuples and lists
################################################

# Tuples: fixed, ordered, immutable
(2+3,)                   # is a tuple but (2+3) not
(2+3, a, "hello")        # objects can be mixed
mx = ((0,1,2), (1,0,3))  # multidimensional  (access: e.g. mx[0][1]

# Lists: ordred but modifiable
[2+3, "hello", a]        # can be mix
nt = [A, C, G, T]
tuple(nt)                # list can be convert in tuple
list(tuple(nt))          # tuple can be convert in list
nt + nt                  # + defined for list -> new list with 8 elements
nt * 3                   # * defined for list -> repeat the original list 3 times

# Membership for tuple and list
"A" in nucList
"A" in nucTuple      # => but not computationally efficient -> use sets to do that
"T" not in nucList
"T" not in nucTuple

# Methods for lists and tuples
nuc.count("A")     # count the number of occurence of given character(s)
nuc.index("T")     # return the index of the 1st occurence (not efficient !)
len(nuc)

# Methods to modify lists  => it modifies the variable itself
seq.append("G")               # add the element at the last position              
seq.append(["G", "C", "T"])   # add the element at the last position => nested list
seq.extend(["G", "C", "T"])   # add the elemens at the end of the list
seq.insert(1, "A")            # insert "A" in position 1
seq.remove("A")               # remove the 1st occurence of A
seq.pop(2)                    # remove element in position 2 and return it
seq.reverse()                 # reverse the order of the items 
seq.sort()                    # sort the items of a list  # ERROR if elements are not comparable

# Sort the list without modfiying the list itself
seq = ["A", "T", "G"]
y = sorted(seq)        # seq is not modified

################################################
# Reference vs. copy (1)
################################################

# Reference vs. copy
L1 = [1,2,3]
L2 = L1        #=> L1 and L2 = 2 variables pointing to the same data in memory
L3 = L1[:]     #=> L3 is a new copy (object) of L1 (different part of the memory)

################################################
# Sets
################################################

# Sets: unordered and modifiable
x = {4, ["A", "C", "G"]}    # you can only mix numbers, strings and tuples (hashable!)
codons = ["ATG", "TTC", "CGT"]
x = tuple(codons)           # you can convert sets into tuples or list and inversely
w = set(codons)             # however content might  change
z = list(codons)	    # can convert from set to list...
y = set(z)	 	    # ... and from list to set	

# Test of presence in sets (like dictionary; unordered so indexing is impossible)
aa = {"Ala", "Thr", "Leu"}
"Pro" in aa                   # efficient !
"Met" not in aa

# Various methods for set manipulation
len(aa) 
aa.add("Iso")
aa.remove("Iso") # decrease aa by one
aa.pop()         # remove the last item and decrease aa

# Methods working on multiple sets
s = {1,2,3,4,5}
t = {4,5,6,7}
a = s&t       # intersection of sets s and t
b = s|t       # union of sets s and t
 
################################################
# Dictionaries
################################################

# = Unorderable and modifiable key:value pairs
aa = {"CCC":"Pro", "GCA":"Ala"}

# The key must be hashable, the value can be of any type !
# Keys and values can be of different types
aa = {("CCA", "CCC"):"Pro"}
aa = {["CCA", "CCC"]:"Pro"}  # ERROR: list is an unhashable type !

# Dictionaries manipulation
aa = {"CCC":"Pro", "GCA":"Ala", "AGA":"Arg"}   # unordered -> no indexing
aa['CCC']
aa['AAC']	 # ERROR: not in aa
aa.get('AAC')    # alternative: do not raise error
aa.get('AAC', 'unknown')   	#  return 'unkown' if not in aa (but aa not changed)
aa.setdefault('AAC', 'blabla') 	# return 'blabla' and add the pair "AAC":"blabla" in aa

# Membership et co. in dictionaries
"CCC" in aa
len(aa)			# number of key:value pairs
aa['CCC'] = "Proline" 	# change the value of the key 'CCC'
aa['ACA'] = "Thr" 	# addd a new pair
del aa['CCC']		# remove the key:value pair of the key 'CCC'
print(aa.keys(), aa.values())
z = list(aa.keys())     # aa.keys() returns a dict_keys object
print(aa.items())	# returns dict_items object

################################################
# Reference vs. copy (2)
################################################

# Be careful when list or dictionary is define through
# variables referencing mutable objects

L = [1,2]   # L points to the list [1,2]
D = {'a':L} # reference to the list [1,2] also pointed to by L
print(D)    # {'a':[1,2]}

L[0] = 3    # change L "in-place", i.e. the list [1,2]
print(D)    # {'a':[3,2]}

D['a'][1] = 17   # modify the list pointed to by L
print(L)    # [3,17]
# => the reference is copied not the list that is referenced !

# Different behavior:
L = [1,2]   # L points to the list [1,2]
D = {'a':L} # reference to the list [1,2] also pointed to by L
L = [3,4]   # L assigned to a new list
print(D)    # {'a':[1,2]}  -> list [1,2] still in memory and pointed to by D

# A better way:
L = [1,2]   # L points to the list [1,2]
D = {'a':L[:]}   # L[:] returns a copy of L
#or
D = {'a':L.copy()}
print(D)    # {'a':[1,2]}
L[1] = 23   # we change L in place
print(D)    # D did not change, points to the copy of [1,2]

# to copy list or dictionary -> .copy() 
# because = makes the new variable point to the same location in memory
