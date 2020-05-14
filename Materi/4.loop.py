dognames = ["Fido", "Sean", "Sally", "Mark"]
print('==>',dognames[2])

for dog in dognames: 
  print(dog)

print('=========================================')

for x in range(1,2):
  print(x)

print('=========================================')
age = 0
while age < 10:
  print(age)
  age += 1


# Print Array using index
words = ["PoGo","Spange","Lie-Fi"]
for index, val in enumerate(words):
  print(index,'==', val)