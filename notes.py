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

#intertools: product, permutations, combinations, accumlate, goupby, and infinite iterators

#product
from intertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod)) #[(1,3),(1,4),(2,3),(2,4)]
a = [1,2]
b = [3]
prod = product(a,b)
prod = product(a,b, repeat=2)
print(list(prod)) #[(1,3,1,3),(1,3,2,3),(2,3,1,3),(2,3,2,3)]

from itertools import permutations #returns all possible orderings
a = [1,2,3]
perm = permutations(a)
print(list(perm)) #[(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,2,1),(3,1,2)]
perm = permutations(a, 2) #only makes list of 2 pairs
print(list(perm)) #[(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

from itertools import combinations #make all possibile combinations with a specified length
a = [1,2,3,4]
comb = combinations(a, 2) #lenth 2
print(list(comb)) #[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]

from itertools import combinations, combinations_with_replacement
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr)) #will make combinations with smae number as well [(1,1),(1,3),etc]

from itertools import accumlate #accumulated sums
a = [1,2,3,4]
acc = accumulate(a)
print(a) #1,2,3,4
print(list(a)) #1,3,6,10

from itertools import accumlate #accumulated sums
import operator
a = [1,2,3,4]
acc = accumulate(a, func=operator.mul) #multiple instead of sum
print(a) #1,2,3,4
print(list(a)) #1,3,6,24

from itertools import accumlate #accumulated sums
import operator
a = [1,2,5,3,4]
acc = accumulate(a, func=operator.maz) #finds maximum
print(a) #1,2,3,4
print(list(a)) #1,2,5,5,5

import itertools import groupby
def smaller_than_3(x):
    return x < 3
a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value)) # True [1,2], False [3,4]

import itertools import groupby
a = [1,2,3,4]
group_obj = groupby(a, key=lambda x: x<3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value)) # True [1,2], False [3,4]

#list of dictionary
persons = [{'name': 'tim', 'age':25},{'name':'dan','age':25}]
group_obj = groupby(perons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value)) #25 [{'name':'Tim', 'age':25}, {'name',:'Dan','age':25}] (repeasts for each age in list)

from intertools import count, cycle, repeat
for i in count(10):
    print(i) #creates loop starting at 10, will go indefinitely

for i in count(10):
    print(i)
    if i == 15: #ends loop at 15
        break

a = [1,2,3]
for i in cycle(a):
    print(i) #will cycle indefinitely through list

for i in repeat(1):
    print(i) #will indefintely print 1

for i in repeat(1,4): #will repeat '1' four times
    print(i)

###############################################################

#lambda arguements: expressions, 1 line functions without a name

add10 = lambda x: x + 10
add10(5)
print(add10(5)) #will print 15

#same as 
def add10_func(x):
    return x + 10

mult = lambda x,y: x*y
print(mult(2,7)) #print 14

points2D = [(1,2),(15,1),(5,-1),(10,4)]
points2D_sorted = sorted(points2D) #will sort by the X arguement of list
points2D_sorted = sorted(points2D, key=lambda x: x[1]) #will sort by Y index
points2D_sorted - sorted(points2D, key=lambda x: x[0] + x[1]) #sorted by sums of each tuple

#map function #map(func,seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b)) #[2,3,6,8,10]

#filter functions: filter(func,seq) must return true or false and will return all elements that are true
a = [1,2,3,4,5]
b = filter(lambda x: x%2==2, a)
print(list(b)) #2,4

#reduce function: reduce(func, seq) - repeatdly 
from functools import reduce
a = [1,2,3,4]
product_a = reduce(lambda x,y: x*y, a)
print(product_a) #24

###############################################################

#errors and exceptions

a = 5 print(a) #will throw syntax error for 'print' not being on new line
print(a)) #will throw syntax error for too many brackets
a = 5 + '10' #type error, can't add string and int
import somemodulethatdoesntexist #modulenotfounderror
b = c #C not defined, name error
f = open('somefile.txt') #filenotfound error
a = [1,2,3]
a.remove(1)
a.remove(4) #ValueError, 4 not in list
a[4]
print(a) #indexerror - index does not exist
my_dict = {'name': 'max'}
my_dict['age'] #keyerror - key doesn't exist

x = -5
if x < 0:
    raise Exception('x should be positive')

assert(x>=0), 'x is not positive'

try:
    a = 5 / 0 #will raise an error, can't divide by 0
except:
    print('an error happened')

try:
    a = 5 / 0
except Exception as e:
    print(e) #prints error from issue

try:
    a = 5 / 0
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally: #will run no matter what
    print('cleaning up....')

#defining our own exceptoin
class ValueTooHighError(Exception):
    pass
def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
try:
    test_value(200) #will throw error
except ValueTooHighError as e:
    print(e)

#defining our own exceptoin
class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError('value is too small', x)
try:
    test_value(200) #will throw error
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

###############################################################

#logging: 

import logging




