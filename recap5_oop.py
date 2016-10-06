##########################
# object oriented programming
##########################
# programming paradigm based on the concept of objects
# objects = data structures containing data (or attributes) and methods (or procedures)

# create your own data types -> object definitions known as classes

# class = definition of a particular kind of object in terms of its component features 
#         and how it is constructed or implemented in the code
# object = specific instance of the thing which has been made according to the class definition
# => everything that exists in Python is an object

# common principle of OOP is that class definition
# -> makes available certain functionality
# -> hides internal information about ho a specific class is implemented
# => encapsulation and information hiding (but Python quite permissive)

# Class definition
class Sequence:
	<statements>

# Common practice: save each class into specific files, then
from Sequence import Sequence

# Inheritance
class MultipleSeq(Sequence):
	<statements>
#-> inherits methods from superclass
#-> classes can have >1 superclass

# Class functions
# -> functions are defined within the construction of a class
# -> defined in the same way as ordinary functions
# -> first argument is special: the object called from (self)
# -> accessed from the variable representing the object via 'dot' syntax
myseq = Sequence(...)
name = myseq.getName()   #getName() defined in Sequence class

class Sequence:
	def getName(self):
		return (self.name)

	def getCapitalisedName(self):
		name = self.getName()
		if name:	
			return (name.capitalize())
		else:
			return (name)

# order of the functions does not matter
# if function definition appears more than once, the last instead replaces the previous one

class MultipleSeq(Sequence):
	def getMSA(self):
		<statements>
	def getSeqID(self):
		<statements>

msa = MultipleSeq(...)

# can call msa.getMSA() as usual
# can also call msa.getName() because of inheritance

# Attributes
# -> attributes hold information useful for the object and its functions
# -> e.g. associate a variable storing sequence name in Sequence objects

# Object attributes:
# -> specific to a particular object
# -> defined inside class functions
# -> use the self keyword to access it

# Class attributes:
# -> available to instance of a class
# -> defined outside all function blocks
# -> usually used for variables that do not change
# -> access directly using the variable name
# -> bare function names are also class attributes

class Sequence:
	type = "DNA"	# class attribute
	
	def setSeq(self, l):
		self.length = l

	def getSeqLength(self):
		return(self.length)

myseq = Sequence()
print(myseq.type)	# variable type can be accessed from the object [not use () to access variable]
print(Sequence.type)	# access through the class itself

getSeqFunc = Sequence.getSeqLength
getSeqFunc(myseq)
# same as
myseq.getSeqLength()

length = myseq.length	# error, length not yet set
myseq.setSeq(541)
length = myseq.length   # returns now 541

myseq.getSeqLength()

myseq.l = 541 	# create new attributes on the fly

# Object life cycle:
# creation of object handled in a special function called constructor
# removal handle by a function called destructor
# Python has automatic garbage collection (usually no need to define a destructor)

# Class constructor:
# called whenever the corresponding object is created
# special name: __init__
# first argument is the object itself (self)
# any other arguments needed to create the object)
# good idea: introduce key to uniquely identifies objects of a given class

class Sequence:
	def __init__(self, name, type="DNA"):
		self.type = type
		try name:
			self.name = name
		except:
			print("Name must be set to sth")
myseq = Sequence("opsin")
myseq2 = Sequence("opsin", "AA")

# When create attributes?
# -> can be created in any class function (or directly on the object)
# -> convention to create most of them in the constructor either directly
#    or through the call to a function
# -> set it to None if it cannot be set at object creation
# -> constructors are inherited by subclasses

