# enumerate()
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

#zip()
names = ["Aruzhan", "Dana", "Tim"]
ages = [20, 22, 19]

for name, age in zip(names, ages):
    print(name, age)

#Demonstrate type checking and conversions
x = "123"
print(type(x))

y = int(x)
print(type(y))

z = float(x)
print(type(z))

