from __future__ import division
from collections import defaultdict, Counter
import random
from functools import partial

#functions

def double (x):
    return x *2

def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)
print x

y = apply_to_one(lambda x: x + 4)
print y

def my_print (message = "Default message"):
    print message

my_print("hello")
my_print()

def substract(a=0, b=0):
    return a - b

substract(10,5)
substract(0,5)
substract(b=5)

#esceptions

try:
    print (0/0)
except ZeroDivisionError:
    print "cannot divide by zero"

#list

integer_list = [1,2,3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]

len(integer_list)
sum(integer_list)

x, y = [1,2]

#tuples

my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3, 4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print "cannot modify tuples"

def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product (2,3)
s, p = sum_and_product (5,10)

x, y = 1,2
x, y = y, x

#dictionaries

empty_dict = {}
empty_dict2 = dict()
grades = { "Joel" : 80, "Tim" : 95}

grades["Joel"]

try:
    grades["Kate"]
except KeyError:
    print "no grade for Kate!"

"Joel" in grades
"kate" in grades

grades.get("Joel",0)
grades.get("Kate",0)
grades.get("No one")

grades["Tim"] = 99
grades["Kate"] = 100
len(grades)

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is awesome",
    "reteet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet.keys()
tweet.values()
tweet.items()

int_dict = defaultdict(int)
int_dict[2] += 3

print int_dict

dd_list = defaultdict(list)
dd_list[2].append(2)

print dd_list

dd_dict = defaultdict(dict)
dd_dict["joel"]["City"] = "seatle"

print dd_dict

Counter([0,1,2,3,0])

#Sets

s = set()
s.add(1)
s.add(2)
s.add(2)
len (s)

2 in s #Faster than on lists

#Control Flow

if 1< 0:
    print "if"
else:
    print "else"

"even" if x%2 == 0 else "odd"

x = 0
while x < 10:
    print x, "is less tan 10"
    x+=1

for x in range(10):
    print x, "is less tan 10"

for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print x

#Sorting

x = [4,1,2,3]
y = sorted(x)

print x, y

x.sort()

print x

sorted([-4,1,-2,3], key = abs, reverse = True)

sorted(grades.items(), 
        key = lambda (name, grade): grade,
        reverse = True)

#List Comprehensions

even_numbers = [x for x in range (5) if x%2 == 0]
squares = [x*x for x in range(5)]
evensquares = [x * x for x in even_numbers]

print even_numbers, squares, evensquares

square_dict = {x: x*x for x in range(5)}
square_Set = {x *x for x in [1, -1]}

print square_dict, square_Set

zeroes = [0 for _ in even_numbers]

print zeroes

pairs = [(x,y) for x in range(10)
                for y in range(10)]

print pairs

increasing_pairs = [(x,y) for x in range(10)
                            for y in range(x + 1, 10)]

print increasing_pairs                            

#Generators and Iterators

def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in lazy_range(10):
    print i

for i in xrange(10): #-> lazy range
    print i

def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

for i in natural_numbers(): # -> Infinite generator
    print i
    if i> 100:
        break

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

for i in lazy_evens_below_20:
    print i

#Randomness

[random.random() for _ in range(4)] #four uniform randoms in range 0,1

random.seed(10)
random.random()
random.seed(10)
random.random()

random.randrange(10)
random.randrange(3,6)

up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten

random.choice(["Alice", "Bob", "Charlie"])

#OOP

class Set:

    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)
    
    def __repr__(self):
        return "Set: "+str(self.dict.keys())
    
    def add(self, value):
        self.dict[value] = True
    
    def contains(self, value):
        return value in self.dict
    
    def remove(self, value):
        del self.dict[value]

s = Set([1,2,3])
s.add(4)
print s.contains(4)
s.remove(3)
print s.contains(3)

#Functional tools

def exp(base, power):
    return base ** power

two_to_the = partial(exp,2)
print two_to_the(3)

square_of = partial(exp, power = 2)
print square_of(3)

xs = [1, 2, 3 ,4]
[double(x) for x in xs]
map(double, xs)
list_doubler = partial(map, double)
list_doubler(xs)

def multiply(x,y): 
    return x*y

map(multiply, [1,2], [4,5])

def is_even(x):
    return x % 2 == 0

[x for x in xs if is_even(x)]
filter(is_even, xs)
list_evener = partial(filter, is_even)
list_evener(xs)

reduce(multiply, xs)
list_product = partial(reduce, multiply)
list_product(xs)
reduce(lambda x,y: x*y, xs)

#Enumerate -> pythonic way of getting indexes and elements

for i, number in enumerate(range(10,0,-1)):
    print i, number

#zip and argument unpacking

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print letters, numbers

def add(a,b):
    return a + b

add(1,2)
add([1,2])
add(*[1,2])

