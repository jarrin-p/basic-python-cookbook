''' general reference sheet for syntax and showing basic functionality '''
''' @author: jarrin-p '''

# imports are usually placed at the top so the reader can
# see what is being used in the program at a glance.

# see `some_package.py` in this directory
import some_package

# you can also import specific functions or classes from packages
# this lets you directly access it by saying `SomeClass()` opposed 
# to `some_package.SomeClass()`
from some_package import SomeClass

# you can append `as alias` to import something and rename it.
# if a package isn't found, run `pip install package_name`
import pandas as pd

# some basics
print("some basics")

# string concatenation
print("string1, " + "string2")

# assigning a variable
some_variable = 20
print(some_variable)

# creating a function
# functions often have `return` statements.
# when using `return` the function will end immediately
# at that location. you can return any type.
def add_numbers(param_1, param_2):
    return param_1 + param_2

# the return value can be used in place of variables,
# as long as the returned data type matches the expected
# data type.
print("ways to use functions")

print(add_numbers(5, 10))
x = add_numbers(1, 2)
print(x)

# since add_numbers returns a number, we can use the result
# of one add_numbers as an argument for another.
# we can do this with assignment
y = add_numbers(add_numbers(10, 20), 30)
print(y)
# or just print the result directly
print(add_numbers(add_numbers(10, 20), 30))
print("\n\n") # two lines for separating output

# lists and looping
print('looping')

# this assignment will be overwritten
some_variable = 20

# in python, lists can contain different data types.
# this can be a gift and a curse. pay close attention to what's in your list.
some_variable = ['x', 'y', 1, 2]
for variable in some_variable: # see that some_variable is no longer 20
    print(variable)

# checking the type of something
type(some_variable)
for variable in some_variable:
    # NOTE: the return value of the `type` function needs to be
    # cast to a string in order to print it.
    print("type of " + str(variable) + ": " + str(type(variable)))
    # uncomment the line below to see the error output
    # print("type of " + variable + ": " + type(variable))

# indexing an array
sample_array = ['alpha', 'beta', 'gamma']
print("arrays start at zero.")
print(sample_array)
print("values of sample_array[1] = " + str(sample_array[1]))
print("\n\n") # two lines for separating output

# arrays can store any data type you can nest as many arrays as you want
# recall that we imported `SomeClass` at the top, see `some_package.py` to 
# see how it works
some_class = SomeClass('x', 'y', 'z')
nested_array = [
        [1, 2, 3],
        sample_array,
        ['delta', 'epsilon', 'zeta'],
        some_class.get_set_params()
]
print('nested arrays')
print(nested_array)
print(nested_array[0])
print(nested_array[1])
print(nested_array[2])
print(nested_array[3])
print(nested_array[3][0]) # accessing the array inside
print("\n\n") # two lines for separating output

print('objects in arrays')
# we can also store objects themselves in lists
object_array = [
        SomeClass('a', 'b', 'c'),
        SomeClass('d', 'e', 'f'),
        SomeClass('g', 'h', 'i')
]
for obj in object_array:
    print('type of `obj`: ' + str(type(obj)))
    print(obj.get_set_params())

print("\n\n") # two lines for separating output

# dictionaries
print('dictionaries')

# making a dictionary.
# dictionaries require what's called a `key` to access them.
# the format is `{ 'unique_key' : object , ... }
some_dict = {'x' : 5, 'y' : 100}

# accessing a dictionary.
print(some_dict['x'])

# notice that the key is a string, so we can actually assign `key`
# values to variables to access the dictionary.
key_y = 'y'
print(some_dict[key_y])

# we can use the values stored at keys similar to how we use variables.
print(add_numbers(some_dict['x'], some_dict['y']))

# you can also create new keys by directly assign to them.
new_key = 'z'
some_dict[new_key] = 50
print(some_dict['z'])
