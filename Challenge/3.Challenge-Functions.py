# Functions
# Create a function named tripleprint  that takes a string as a parameter and prints that string 3 times in a row. So if I passed in the string hello  it would print hellohellohello

# *Be sure to only create the function, don't call it. For example, don't write tripleprint("hello")  The exercise will do this for you.

# =============Solution=============

def tripleprint(text):
  print('{}{}{}'.format(text,text,text))

tripleprint('Hello')



def tripleprint2(word):
  print(word*3)

tripleprint2('Hello')