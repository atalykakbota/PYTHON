#1.Create a generator that generates the squares of numbers up to some number N.

def generate_squares(N):
    for num in range(1, N + 1):
        yield num * num

for square in generate_squares(5):
    print(square)

#2.Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even_numbers(n):
    for x in range(0, n + 1, 2):
        yield x

try:
    n = int(input().strip())
    print(",".join(str(num) for num in even_numbers(n)))
except ValueError:
    print("Please enter an integer.")

#3.Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divisible_by_3_and_4(n):
    for num in range(0, n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input("Enter n: "))

for value in divisible_by_3_and_4(n):
    print(value)

#4Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values

def squares(a, b):
    for num in range(a, b + 1):
        yield num * num

a = int(input("Enter start number (a): "))
b = int(input("Enter end number (b): "))

for value in squares(a, b):
    print(value)

#5.Implement a generator that returns all numbers from (n) down to 0.

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter n: "))
for value in countdown(n):
    print(value)
