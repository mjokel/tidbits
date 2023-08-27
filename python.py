# VENV -------------------------------------------------------------------------
"""
    in Unix/Linux shell:

    python3 -m venv <name>
    source <name>/bin/activate

    to deactivate:
    deactivate
"""


# MAIN -------------------------------------------------------------------------

if __name__ == "__main__":
    pass


# TYPE HINTS -------------------------------------------------------------------

# receives and returns numeric: either float or int, as float includes int!
def a(x: float) -> float:
    pass

# returns either int or None (Python +3.10)
def a() -> int | None: 
    pass


# CLASSES ----------------------------------------------------------------------

class Animal():
    def __init__(self, name): # initializer
        self.name = name

    def speak(self):
        return f'Animal {self.name} says hi!'
    
    def __str__(self):
        return f'{self.name} is an Animal.'

class Dog(Animal):
    def speak(self):
        return f'Dog {self.name} barks!'
    
    def __str__(self):
        return f'{self.name} is a Dog.'

a = Animal("Alice")
print(a, a.speak())

b = Dog("Bob")
print(b, b.speak())


# LOOPS ------------------------------------------------------------------------

# iterate [0, n-1]
for i in range(5): # NOTE: more verbose: range(0, 5)
    print(i) # → 0,1,2,3,4

for i in range(5, 10):
    print(i) # → 5,6,7,8,9


# iterate over array length
a = ["a", "b", "c"]
n = len(a)
for i in range(n):
    print(i) # → 0,1,2


# iterate elements
for i in ["a", "b", "c"]:
    print(i) # → a,b,c


# iterate index and value
for i, val in enumerate(["a", "b", "c"]):
    print(f'{i}-{val}') # → 0-a, 1-b, 2-c


# iterate key and value
d = {'foo': 1, 'bar': 2, 'baz': 3}
for key in d:
    print(f'{key}-{d[key]}') # → foo-1, bar-2, baz-3

# iterate values only
for val in d.values():
    print(val) # → 1,2,3


# advanced
for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('Done.')  # Will not execute!


# enumerate: index and value
for i, el in enumerate(["a", "b", "c", "d"], start=10): # NOTE: start at 10
    print(f'{i}-{el}') # → 10-a, 11-b, 12-c, 13-d 

# advanced
for index, user in enumerate( ["Test User", "Real User 1", "Real User 2"] ):
    if index == 0:
        print("Extra verbose output for:", user)
    else:
        print(user)



# DATA STRUCTURES --------------------------------------------------------------

# lists: collection of arbitrary objects
a = [1,2,3]
b = ['a', 'b', 'c']

# appending lists 
a + b # → [1, 2, 3, 'a', 'b', 'c']

# NOTE: must be of type list, 'd' would not work!
print(b + ['d']) # → ['a', 'b', 'c', 'd']

for i in range(4, 7):
    # a += [i] # NOTE: works, but not preferred
    a.append(i)
# → [1, 2, 3, 4, 5, 6]

# inserting
a.insert(2, '#') # → [1, 2, '#', 3, 4, 5, 6]

# remove item
a.remove('#') # → [1, 2, 3, 4, 5, 6]

# remove last item; NOTE: index may be specified!
a.pop() # → [1, 2, 3, 4, 5]


# tuples: only difference to lists: immutable!
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')


# dicts
d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}

# value at key 0
d[0] # → 'a'

# NOTE: no access via index!

# init empty dict and incrementally fill it
person = {}
person['name'] = 'Joe'
person['age'] = '34'

# return value for a key if it exists; otherwise return default
person.get('age', 0) # → 34

# remove key
del person['age'] # → {'name': 'Joe'}

# get list of keys, resp. values
d.keys() # → [0, 1, 2, 3]
d.values() # → ['a', 'b', 'c', 'd']

# remove key, if it is present, and returns its value
d.pop(3) # → 'd'

# removes the last key-value pair added from d and returns it as a tuple
print(d.popitem()) # → (2, 'c')

# merge dicts
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2) # → {'a': 10, 'b': 200, 'c': 30, 'd': 400}


# SLICING ----------------------------------------------------------------------

"""
    a[start:stop]  # items start through stop-1
    a[start:]      # items start through the rest of the array
    a[:stop]       # items from the beginning through stop-1
    a[:]           # a copy of the whole array

    a[start:stop:step] # start through not past stop, by step
"""

# reversing
l = a+b
l[::-1] # → ['c', 'b', 'a', 5, 4, 3, 2, 1]

# first, second and third element
l[0] # → 1
l[1] # → 2
l[2] # → 3

# last, second to last and third to last element: "first from the end + `-` sign"
l[-1] # → 'c'
l[-2] # → 'b'
l[-3] # → 'a'

# first two elements
l[:2] # → [1,2]

# last two elements
l[-2:] # → ['b', 'c']

# every second element: no `stop`, with `step=2`
l[1::2] # → [2, 4, 'a', 'c']



# COMPARING --------------------------------------------------------------------

"""
    is  will return True if two variables point to the same object (in memory), 
    ==  if the objects referred to by the variables are equal.
"""

a = None
if a is None: # preferred; however a == None would work, too
    pass

b = ""
if b is None: # FALSE
    pass
if b == "": # TRUE
    pass



# LIST COMPREHENSION -----------------------------------------------------------

arr = [2, 3, 5, 7, 9, 11]

# functional approach
def squares(x: float) -> float:
    return x*x

j = map(squares, arr)
list(j) # → [4, 9, 25, 49, 81, 121]


# list comprehension

"""
    new_list = [expression for member in iterable (if condition)]

    NOTE: does work with sets and dicts, too!
"""

# squares
j = [i * i for i in arr] # → [4, 9, 25, 49, 81, 121]


# int to string
[f'a-{i+1}' for i in arr] # → ['a-3', 'a-4', 'a-6', 'a-8', 'a-10', 'a-12']

# filter
[i for i in arr if i > 3] # → [5, 7, 9, 11]


import random
def get_weather_data():
    return random.randrange(90, 110)

# walrus operator
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
hot_temps # → [107, 102, 109, 104, 107, 109, 108, 101, 104]


# same as above, but more verbose
c = 0
l = []

while c < 10:
    x = get_weather_data()
    if x >= 100:
        l.append(x)
        c += 1
# → [109, 104, 103, 105, 108, 102, 108, 107, 102, 107]



# LAMBDAS ----------------------------------------------------------------------

"""
    one-liner (!) anonymous functions, based on functional programming
"""


# sort a list of strings in ascending word-length order
sorted(["apple", "banana", "cherry", "date", "fig"], key = lambda x: len(x))


# filter list for odd numbers only
list( filter(lambda x: x%2==1, [2, 5, 8, 11, 14, 17, 20]) ) # lambda
[i for i in [2, 5, 8, 11, 14, 17, 20] if i%2==1 ]           # list comprehension

# program that calculates the factorial of a given positive integer using recursion and a lambda function.

# traditional recursive approach
def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)
factorial(5) # → 120

# achieve recursion with lambda by assigning it to a variable!
factorial_lambda = lambda x: x * factorial(x-1) if x > 1 else 0
factorial_lambda(5) # → 120



# EXCEPTIONS -------------------------------------------------------------------

# # rasing an exception
# raise Exception(f'There was an error: 1==2: {1==2}')

# # raising a specific error
# raise ValueError('Variable i must be smaller than ...')

# IndexError, ValueError, KeyError, ZeroDivisionError, TypeError, ...

# catching errors
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as err:
    print(err)
except TypeError as err: # catch another error type
    print(err)
else: # runs if there is no exception
    print('Executing the else clause.')
finally: # will always run
    pass


# FILE PATHS -------------------------------------------------------------------

# library for OS-agnostic file paths and file operations
from pathlib import Path


Path.cwd() # →  "/Users/max/Desktop"
Path.home() # →  "/Users/max"

# casting to string
str( Path.cwd() ) # → for Windows \, for Unix/Linux /

# constructing paths
Path.cwd() / "foo" / "bar" # → /Users/max/Desktop/foo/bar
Path.cwd().joinpath("foo", "bar") # → /Users/max/Desktop/foo/bar

# check if file exists
fn = Path.cwd() / "test.png"
fn.exists() # → False


"""
    .name:      filename and extension, without any directory
    .stem:      filename without extension
    .suffix:    file extension
    .anchor:    part of the path before the directories
    .parent:    directory containing the file, or the parent directory if the path is a directory
"""

path = Path("/users/gahjelle/realpython/test.md") 

path # → PosixPath("/users/gahjelle/realpython/test.md")
path.name # → 'test.md'
path.stem # → 'test'
path.suffix # → '.md'
path.anchor # → '/'
path.parent # → PosixPath("/users/gahjelle/realpython")
path.parent.parent # → PosixPath('/users/gahjelle')

# paths and strings
path.parent / f'new{path.suffix}' # → PosixPath('/users/gahjelle/realpython/new.md')


# opening files directly with pathlib; 
# NOTE: no need to specify cwd & closes files as well!
content = Path("list.md").read_text(encoding="utf-8")
groceries = [line for line in content.splitlines() if line.startswith("*")]
print("\n".join(groceries))

# write to file; NOTE: will overwrite existing file and contents!
Path("plain_list.md").write_text("Hello, world!", encoding="utf-8")
Path("plain_list.md").write_text("\n".join(groceries), encoding="utf-8")


# # renaming files
# txt_path = Path("/home/gahjelle/realpython/hello.txt")
# md_path  = txt_path.with_suffix(".md")   # NOTE: update file extension; returns new path
# md_path  = txt_path.with_stem("goodbye") # NOTE: update file name; returns new path
# txt_path.replace(md_path) # NOTE: commit renaming action


# # copying files 
# source = Path("shopping_list.md")
# destination = source.with_stem("shopping_list_02")
# destination.write_bytes(source.read_bytes())

# # NOTE: shutil is preferred method
# import shutil
# src = 'path/to/file.txt'
# dst = 'path/to/dest_dir'
# shutil.copy(src, dst)
# shutil.copy2(src, dst) # preserves meta data


# # moving files: dest will be overwritten, so check if exists
# source = Path("hello.py")
# destination = Path("goodbye.py")

# try: # avoid race conditions by opening dest for exclusive creation
#     with destination.open(mode="xb") as file:
#         file.write(source.read_bytes())
# except FileExistsError:
#     print(f"File {destination} exists already.")
# else:
#     source.unlink()


# create empty file
filename = Path("hello.txt")
filename.exists() # → False
filename.touch()
filename.exists() # → True


# counting files
from collections import Counter
Counter(path.suffix for path in Path.cwd().iterdir()) # → Counter({'.md': 2, '.txt': 4})
Counter(path.suffix for path in Path.cwd().glob("*.pdf")) # → Counter({'.pdf': 2})
# NOTE: globr/rglob for accessing sub-directories

# x = 
# print(x)



# OTHER ------------------------------------------------------------------------

print( type(1).__name__ )   # → int
print( type('a').__name__ ) # → str


# WALRUS -----------------------------------------------------------------------

# pre Python 3.8
number = int(input("Enter a number: "))
if number > 10:
    print("The number is greater than 10.")

# with the walrus operator → assignment inside an expression, no need to declare a variable
if (number := int(input("Enter a number: "))) > 10:
    print("The number is greater than 10.")


# READING FILES ----------------------------------------------------------------

"""
    'r' 	    Open for reading (default)
    'w' 	    Open for writing, overwriting the file
    'a'         append to file
    'rb', 'wb' 	read/write using byte data
"""

with open('dog_breeds.txt', 'r') as reader:
    # Read and print the entire file line by line
    for line in reader:
        print(line, end='')

    contents = reader.readlines()


with open('dog_breeds_reversed.txt', 'w') as writer:
    # Alternatively you could use
    # writer.writelines(reversed(contents))

    # Write the dog breeds to the file in reversed order
    for line in reversed(contents):
        writer.write(line)

with open('dog_breeds.txt', 'a') as a_writer:
    a_writer.write('\nBeagle')



import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# serialize object and write JSON to file
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

# import JSON
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)


import pandas

# reading and writing CSV files with pandas
df = pandas.read_csv('data.csv')
print(df)
df.to_csv('data2.csv')


# GENERATORS -------------------------------------------------------------------

"""
    Generators are a special kind of function that return a lazy iterator; they
    are great when working with memory intensive tasks!
"""

# example for reading files
def read_csv(file_name):
    for row in open(file_name, "r"):
        yield row

# defining an infinite sequence
def seq():
    counter = 0
    while True:
        yield counter
        counter += 1

gen = seq()
next(gen) # → 0
next(gen) # → 1
next(gen) # → 2



# TESTING ----------------------------------------------------------------------

"""
    run `pip install pytest`
    create file `test_##.py`
    call `pytest`
"""

import pytest

# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

