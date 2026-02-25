#Example
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)

#1
def odd_numbers(max):
    n = 1
    while n <= max:
        if n % 2 == 1:
            yield n
        n += 1

for num in odd_numbers(10):
    print(num)

#2
def even_numbers(max):
    n = 1
    while n <= max:
        if n % 2 == 0:
            yield n
        n += 1

for num in even_numbers(10):
    print(num)

#3

def reverse_count(start):
    while start > 0:
        yield start
        start -= 1

for n in reverse_count(5):
    print(n)

#4

def fib(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1

for x in fib(7):
    print(x)

#5

def squares(max):
    n = 1
    while n <= max:
        yield n * n
        n += 1

for s in squares(6):
    print(s)

#Example
def fun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for val in fun(): 
    print(val)

#1

def days():
    yield "Monday"
    yield "Tuesday"
    yield "Wednesday"

for d in days():
    print(d)

#2
def fruits():
    yield "apple"
    yield "cherry"
    yield "banana"

for f in fruits():
    print(f)

#3
def animals():
    yield "dog"
    yield "cat"
    yield "monkey"

for a in animals():
    print(a)

#4

def colors():
    yield "red"
    yield "green"
    yield "blue"

for c in colors():
    print(c)

#5

def squares():
    yield 1 * 1
    yield 2 * 2
    yield 3 * 3

for x in squares():
    print(x)

#Example
def fun():
    return 1 + 2 + 3

res = fun()
print(res)

#1
def fun():
    return 4 * 5 * 6

res = fun()
print(res)

#2
def greet():
    return "Hello Bota"

msg = greet()
print(msg)

#3
def square():
    return 6 ** 2

value = square()
print(value)

#4

def numbers():
    return [1, 2, 3]

lst = numbers()
print(lst)

#5
def words():
    return "Good" + " " + "Luck!"

word = words()
print(word)

#Example
sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)

#1
num = (x+1 for x in range(4,9))
for i in num:
    print(i)

#2

even = (x for x in range(1, 11) if x % 2 == 0)
for n in even:
    print(n)

#3

cubes = (x**3 for x in range(1, 6))
for c in cubes:
    print(c)

#4

greater = (x for x in range(1, 11) if x > 5)
for g in greater:
    print(g)

#5

words = ["apple", "banana", "kiwi"]
lengths = (len(w) for w in words)

for L in lengths:
    print(L)



