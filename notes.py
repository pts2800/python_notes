########
# Notes taken from youtube course
# https://www.youtube.com/watch?v=HGOBQPFzWKo
#######

#lists: order, muteable, allowed duplicate elements
mylist = ["banaout", "cherry","apple"]
print(mylist)

mylist2 = mylist()
print(mylist2)

mylist3 = [5, True, "apple", "apple"]
print(mylist3)
item = mylist[0]
print(item)

#prints last item
print(mylist[-1])
#prints second to last item
print(mylist[-2])

#print each item
for i in mylist:
    print(i)

#check if item is in list
if "banana" in mylist:
    print("yes")
else:
    print("no")

#check how many elements are in list
print(len(mylist))

#append to list (adds at end)
mylist.append("lemon")

#inserts element at specici position
mylist.insert(1, "blueberry")

#removes last item in list
item = mylist.pop()

#remove specific element
item = mylist.remove("cherry")

#remover all elements
item = mylist.clear()

#remove the items in list
item = mylist.reserve()

#sort list - changes og list
mylist = [-1, 2, -3, 4]
item = mylist.sort()

#sort into a new list without modifying og list
new_list = sorted(mylist)
print(mylist)

#create list with multiple of same value, create list iwht 5x 0's
mylist = [0] * 5
mylist2 = [1,2,3,4,5]
#add lists together
new_list = mylist+mylist2

#slicing lists
mylist = [1,2,3,4,5,6,7,8,9]
#start index 1, stop index 5, creates list from 1 to 5, last one is excluded
a = mylist[1:5]
#starts from begining
a = mylist[:5]
#goes to end
a = mylist[1:]
#step index
a = mylist
#goes from beginging to index with step of 1
a = mylist[::1]
#goes from beginging to index with step of 2
a = mylist[::2]
#reverse lists
a = mylist[::-1]

#copy list #lists will always equal eachother, no matter where you make the changes
list_og = ["banana", "cherry", "apple"]
list_cpy = list_og
#how to copy list without it sharing memory
list_cpy = list_og.copy()
list_cpy = list(list_og)
#use slice to make copy
list_cpy = list_og[:]

#creates new list based on mylist were each element is squared
mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]

###############################################################

#Tuples ordered, immutable, allows deuplicate elements

mytuple = ("max", 28, "boston")
mytuple = "max", 28, "boston"
mytuple = ("max",)
print(mytuple)

#create tuple from list
mytuple = tuple(["max", 28, "boston"])

item = mytuple[1]
print(item)

for i in tuple:
    print(i)

my_tuple = ('a','b','c')

#prints length of tuple
print(len(my_tuple))

#checks how many times an element exists
print(my_tuple.count('a'))

#prints index of element
print(my_tuple.index('p'))

#convert list to tuple and vice versa
my_list = list(my_tuple)
my_tuple = tuple(mylist)

#slicing
a = (1,2,3,4,5,6,7,8,9)
b = a[2:5]

#unpacking - sets each element to a var, # of vars much match # of elements
mytuple = ("max", 28, "boston")
name, age, city = my_tuple

# *i2 will unpack everything in between first and last index
my_tuple = (1,2,3,4)
i1, *i2, i3 = my_tuple

#compare list and tuple - tuples use less mem, also faster
import sys
my_list = [0,1,2,"hello", True]
my_tuple = (0,1,2,"hello", True)
print(sys.getsizedof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")

###############################################################

#dictionaries: key-value pairs, unordered, mutable

mydict = {"name": "max", "age": 28, "city": "new york"}
print(mydict)
mydict2 = dict(name="mary", age=27, city="boston")
value = mydict["name"]
#add key/value
mydict["email"] = "max@zyz.com"
#delete key/value
del mydict["name"]
#removes last
mydict.popitem()
#check if key exists
if "name" in mydict:
    print(mydict["name"])
#loops through dict
for key in mydict.keys():
    print(key)
#loops through values
for value in mydict.values():
    print(value)
#print both
for key, value in mydict.items():
    print(key, value)

#copy dict - like lists, will modify both
mydict_cpy = mydict

#made actual copy
mydict_cpy = mydict.copy
mydict_cpy = dict(mydict)

#update dicts
dict1 = {"name": "max", "age": 28, "city": "new york"}
dict2 = {"name": "mary", "age": 27, "city": "boston"}

dict1.update(dict2)

#key types:
mydict = {3:9, 6:36, 9:81}
value = mydict[3] # = 9

#tupledict
mytuple = (8,7)
mydict = {mytuple: 15}

###############################################################

#sets unordered, mutable, no duplicates
myset = {1,2,3}
myset = set([1,2,3])
myset = set("hello") #each char will be it's own value, only 1 'L' will be added to set

#emprt set
myset = set()
myset.add(1)
myset.add(2)

#removes element
myset.remove(1)

#removes element without error if it doesn't esist
myset.discard(1)

myset.pop()

#loop through set
for i in myset:
    print(i)

#if in set
if 1 in myset:
    print("yes")

#union and intersection
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
#unions adds all without duplications
u = odds.union(evens)
#interections will only take values in both sets
i = odds.intersection(evens)

#differences of 2 sets
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
#returns all elements in first set that aren't in 2nd
diff = setA.difference(setB)
#returns values that aren't shared between sets
diff = setB.symmetric_difference(setA)

#modify sets - combines both sets together without duplication
setA.update(setB)

#update sets with elements only found in both sets
setA.intersection_update(setB)

#update sets with elements that only different in set A
setA.difference_update(setB)

#updates the set but only keeps the elements in both sets
setA.symmetric_difference_update(setB)

#subset = if all elements are in setA are in setB
setA = {1,2,3,4,5,6}
setB = {1,2,3}
setA.issubset(setB)

#superset
setA.issuperset(setB)

#disjoined - if sets have no same elements
setA.isdisjoint(setB)

#coping 2 sets - will modify both like lists
setB = setA

#make actual copy
setB = setA.copy
setB = set(setA)

#frozen set, can't change it after it was created
a = frozenset([1,2,3,4])

###############################################################

#strings: ordered, immutable, text representation
my_string = "hello world"
print(my_string)
my_string = 'hello world'
print(my_string)
my_string = """ this is a
multiline string"""

#chars or substrings
my_string = "hello world"
char = my_string[0] #return 'h'

#index of string
substring = my_string[1:5] #'ello'
#step index
substring = my_string[::1]
#reverse step index (reverses string)
substring = my_string[::-1]

#add two strings together
greeting = "hello"
name = "tom"
sentence = greeting + " " + name

#print every letter
for i in greeting:
    print(i)

#check if char in string
if 'e' in greeting:
    print("yes")
else:
    print("no")

#strip - removes whitespace
my_string = "   hello world   "
my_string = my_string.strip()

#conver to uppercase
print(my_string.upper())
#convert to lowercase
print(my_string.lower())
#check if string starts with letter/word
print(my_string.startswith('h'))
print(my_string.endswith("world"))
#returns index of first letter/string found, return -1 if not found
print(my_string.find('o'))
#count number of char/string found
print(my_string.count("l")) #lowercase L
print(my_string.replace('World', 'universe')) #replaces word in string

#convert string to list
my_string = 'how are you doing'
my_list = my_string.split() #default arg is whitespace
print(mylist)

my_string = 'how,are,you,doing'
my_list = my_string.split(",") #default arg is whitespace
print(mylist)

#convert list to string
new_string = ' '.join(my_list) #puts whitespace between elements in list
print(new_string)

#create list with mutiple elemetns into string
my_list = ['a']*6
#bad way
my_string = ''
for i in my_list:
    my_string +=i
#good way, cleaner and faster
my_string = ''.join(my_list)

#format a string
#old way: %, .format() newway: f-strings
var = "Tom"
my_string = "the var is %s" % var
var = 3
my_string = "the var is %d" % var
var = 3.1415
my_string = "the var is %f" % var #default 6 digits, %.2f would do 2 digits
my_string = "the var is {}".format(var) #{:.2f} specifies 2 digits
var2 = 6
my_string = "the var is {:.2f} and {}".format(var,var2)
#fstring - use this way if possible
my_string = f"the var is {var} and {var2}"
my_string = f"the var is {var*2} and {var2}" #multiplies first var by 2

###############################################################

#collections: counter, namedtuple, ordereddict, defaultdict, deque

#counter
from collections import Counter
a = "aaaaaabbbbbcccccc"
my_counter = Counter(a)
print(my_counter) #returns counter as dict counter({'a':5, 'b':4, 'c':3})
#prints only keys:
print(my_counter.keys())
#prints only values
print(my_counter.values())
#primts most common
print(my_counter.most_common(1)) #prints 1st most common

from collections import namedtuple
Point = namedtuple('Point', 'x,y') #creates class called point
pt = Point(1,-4)
print(pt) #Point(x=1, y=4)
print(pt.x, pt.y) #prints x and y

#used in older versions of python
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict) #prints in order it was added

from collections import defaultdict
#will have default value of key if value doesn't exist yet
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['b']) #print B
print(d['c']) #since C doesn't exisit, will return int (default int is 0)

from collections import deque
#double ended que, can add or remove elements on both ends
d = deque()
d.append(1)
d.append(2)
print(d) #deque([1,2])
d.appendleft(3)
print(d) #deque([3,1,2])
d.pop() #remvoe last element
d.popleft() #removes left most element
d.clear() #removes all elements
d.extend([4,5,6]) #add elements
d.extendleft([4,5,6])
d.rotate(1) #moves all elements to right by 1 index
d.rotate(-1) #moves all eletements to left by 1 index


###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################