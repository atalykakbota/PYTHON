#Example
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#1
message = "beautiful"

def show():
    print("Life is " + message)

show()

#2
city = "Almaty"

def print_city():
    print("I live in " + city)

print_city()

#3
food = "pizza"

def favorite_food():
    print("My favorite food is " + food)

favorite_food()

#4
language = "Kazakh"

def speak():
    print("I speak " + language)

speak()

#5
hobby = "coding"

def show_hobby():
    print("My hobby is " + hobby)

show_hobby()

#Example
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#1
color = "blue"

def show_color():
    color = "red"
    print("Inside function:", color)

show_color()
print("Outside function:", color)

#2
name = "Alice"

def change_name():
    name = "Bob"
    print("Inside function:", name)

change_name()
print("Outside function:", name)

#3
mood = "happy"

def set_mood():
    mood = "excited"
    print("Inside function:", mood)

set_mood()
print("Outside function:", mood)

#4
number = 10

def change_number():
    number = 20
    print("Inside function:", number)

change_number()
print("Outside function:", number)

#5
city = "Almaty"

def update_city():
    city = "Astana"
    print("Inside function:", city)

update_city()
print("Outside function:", city)

#Example
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#1
def change():
    global color
    color = "red"

change()
print("Color is " + color)

#2
def set_name():
    global name
    name = "Alice"

set_name()
print("My name is " + name)

#3
def update_city():
    global city
    city = "Almaty"

update_city()
print("City is " + city)

#4
def set_status():
    global status
    status = "active"

set_status()
print("Status is " + status)

#5
def change_number():
    global num
    num = 100

change_number()
print("Number is", num)

#Example
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#1
status = "offline"

def set_status():
    global status
    status = "online"

set_status()

print("User is " + status)

#2
color = "blue"

def change_color():
    global color
    color = "red"

change_color()

print("Color is " + color)

#3
language = "Kazakh"

def update_language():
    global language
    language = "English"

update_language()

print("The language is " + language)

#4
mode = "normal"

def set_mode():
    global mode
    mode = "advanced"

set_mode()

print("Mode is " + mode)

#5
level = "beginner"

def upgrade_level():
    global level
    level = "expert"

upgrade_level()

print("User level is " + level)

