# In Python, all characters after a '#' symbol are ignored
# These are called comments

# Consider f(x) = x + 4
# f is a function, x is a variable

# The "def" keyword is how you define functions in python
# Note that you have to name the parameters that the function takes in
def f(x):
    return x + 4

# To use this function, call it by name without the "def"
# You need to supply a value for each parameter
f(5) # This returns 9

# In python, not everything needs to be contained in a funciton
# All code in your file will run

# This is how variables are declared in Python
# Simply give it a name and a value
y = 12

# Variables are useful because they can be passed into a function
f(y) # This returns 16

# You can also store the result of a function in a variable
result = f(y) # Now result is equal to 16

# Print statements are very useful
# Anything printed will be visible in your terminal
print "Hello, world!"

# Print many things by separating them with commas
print "Hello,", "world!"

# You can also print variables
print "Result is:", result

# You can use raw_input to get input from the user
data = raw_input("Type something: ")
print data

# This doesn't need to take any arguments
def pizza_pudding():
    return True

# Conditional statements are structured such that the condition comes first
if pizza_pudding():
    print "I don't like it"
# else runs whenever the condition is not met
else:
    print "I do like it"

# You can also string conditionals together
if f(y) > 0:
    print "f(y) is positive"
elif f(y) < 0:
    print "f(y) is negative"
else:
    print "f(y) is zero"

# Lists are denoted by square brackets
a_list = ["this", "is", "a"]

# You can add items to a list
a_list.append("lizt")

# Or change items
a_list[3] = "list"

# Lists  can be generated with the range() function
b_list = range(10)
print b_list

# Dictionaries use curly braces and map keys to values
a_dictionary = {
    "this": "is",
    "a":    "dictionary",
}

# Tuples are immutable
a_tuple = ("this", "is", "a", "tuple")

# You access the data in these containers with square brackets
print a_list[0], a_dictionary["this"], a_tuple[2], "fun time"

# The in keyword has two uses

# In conditionals
if 10 in b_list:
    print "Somehow 10 got into b_list"

# In loops (we'll get to it)

# Here is a for loop
# For loops are (mostly) used to iterate over a container
for i in range(10):
    print i, # A trailing comma after your print statement means "no new line"

print "Done counting!"

# Loops can be stopped early with the "break" keyword
for i in range(10):
    if i == 8:
        break
    print i,

print "Done counting!"

# Certain items can be skipped with the "continue" keyword
for i in range(10):
    if i == 3:
        continue
    print i,

print "Done counting!"

# Here is a while loop
# We don't know how many times the loop needs to run
while True:
    text = raw_input("Give me a command: ")
    if text == "done":
        break
    else:
        print text
