# Dictionaries
# I have provided you with two lists. words and definitions

# Create a dictionary called cooldictionary where you use words for keys and definitions for values

# Hint: See if you can do this with a loop!

# words = ["PoGo","Spange","Lie-Fi"]
# definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]


# =================Solution=================
# My Solution:
words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = {}
for index, val in enumerate(words):
  cooldictionary[val] = definitions[index]

print(cooldictionary)

print('=========================================')

# zappycode SOLUTION
cooldictionary1 = {}
for i in range(0,3):
    cooldictionary1[words[i]] = definitions[i]

print(cooldictionary1)


