#Example
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)

print(y)

#1
import json

x = ["apple", "banana", "cherry"]

y = json.dumps(x)

print(y)

#2
import json

x = {
    "a": 10,
    "b": 20,
    "c": 30
}

y = json.dumps(x)

print(y)

#3
import json

x = {
    "price": 19.99,
    "in_stock": True
}

y = json.dumps(x)

print(y)

#4
import json

x = {
    "name": "Akbota",
    "age": 18,
    "city": "Almaty"
}

y = json.dumps(x, indent=4)

print(y)

#5

import json

x = {
    "student": "Bota",
    "scores": [90, 85, 88],
    "passed": True
}

y = json.dumps(x)

print(y)

#Example
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#1

import json

text = '{"name": "Ayana", "age": 18, "city": "Almaty"}'
data = json.loads(text)

print(type(data))      
print(data["name"])   

#2
import json

text = '["apple", "banana", "cherry"]'
data = json.loads(text)

print(type(data))  
for item in data:
    print(item)

#3
import json

text = '''
{
  "student": {
    "name": "Gulvira",
    "scores": [92, 97, 91],
        "passed": true
  },
  "group": "C2"
}
'''
data = json.loads(text)

print(data["student"]["name"])     
print(data["student"]["scores"][1])
print(data["student"]["passed"])   

#4

import json

text = '{"name": "Algida", "city": "Kyzylorda"}'
data = json.loads(text)

print(data["name"])  
print(data["city"])  

#5
import json


bad_text = '{ "ok": true, "nums": [1, 2, ], }'

try:
    data = json.loads(bad_text)
except json.JSONDecodeError as e:
    print("JSON wrong:", e)

#Example
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#1
import json

data = {
    "name": "Aigerim",
    "age": 22,
    "languages": ["Kazakh", "English"]
}

print(json.dumps(data, indent=4))

#2   
import json

data = {
    "value1": 123,
    "value2": 45.67,
    "online": True,
    "status": None
}

print(json.dumps(data))

#3
import json

data = {
    "students": [
        {"name": "Aiym", "grade": 92},
        {"name": "Imangali", "grade": 72}
    ],
    "group": "Dos1"
}

print(json.dumps(data, indent=2))

#5
import json

text = '{"product": "Laptop", "price": 250000, "in_stock": true}'

obj = json.loads(text)

json_text = json.dumps(obj, indent=4)

print(json_text)
