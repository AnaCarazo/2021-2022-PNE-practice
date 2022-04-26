#extracted from: https://www.w3schools.com/python/python_json.asp
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
print("x content: ", x)
print("x type: ", type(x))

# parse x:
y = json.loads(x)
print("y content: ", y)
print("y type: ", type(y))

# the result is a Python dictionary:
print(y["age"])