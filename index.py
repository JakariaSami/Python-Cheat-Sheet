# print "Hello World"
print("Hello World")

# Python program showing a use of input()
val = input("Enter your value: ")
print(val)

#=============================================================
# Examples of Arithmetic Operator
a = 9
b = 4

# Addition of numbers
add = a + b

# Subtraction of numbers
sub = a - b

# Multiplication of number
mul = a * b

# Modulo of both number
mod = a % b

# Power
p = a ** b


#=============================================================
# Examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)


#=============================================================
# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)


#=============================================================
# DataType Output: str
x = "Hello World"

# DataType Output: int
x = 50

# DataType Output: float
x = 60.5

# DataType Output: complex
x = 3j

# DataType Output: list
x = ["geeks", "for", "geeks"]

# DataType Output: tuple
x = ("geeks", "for", "geeks")

# DataType Output: range
x = range(10)

# DataType Output: dict
x = {"name": "Suraj", "age": 24}

# DataType Output: set
x = {"geeks", "for", "geeks"}

# DataType Output: frozenset
x = frozenset({"geeks", "for", "geeks"})

# DataType Output: bool
x = True

# DataType Output: bytes
x = b"Geeks"

# DataType Output: memoryview
x = memoryview(bytes(6))

# DataType Output: NoneType
x = None


#=============================================================
# Tuples
# Tuple is a list-like collection of Python objects. A tuple stores a succession of values of any kind, which are indexed by integers.
var = ("Geeks", "for", "Geeks")

# Python Set is an unordered collection of data types that can be iterated, mutated and contains no duplicate elements. The order of the elements in a set is unknown, yet it may contain several elements.
var = {"Geeks", "for", "Geeks"}

#==============================================================
# If-Else
i = 20
if i < 15:
    print("i is smaller than 15")
else:
    print("i is greater than 15")
print("i'm not in if and not in else Block") # This block will run after the conditionals

#==============================================================
# For loop
l = ["geeks", "for", "geeks"]

for i in l:
    print(i)

# While loop
count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")

#===============================================================
# Functions
def evenOdd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

# Lambda Functions
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

#===============================================================
# range() Funciton
# print first 5 integers
for i in range(5):
    print(i, end=" ")
print()

#===============================================================
# OOP
class Car:
    def __init__(self, make, model, year):
        self._make = make  # protected attribute
        self.__model = model  # private attribute
        self.year = year  # public attribute

    def get_make(self):
        return self._make

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model


my_car = Car("Toyota", "Corolla", 2022)

print(my_car.get_make())  # Accessing protected attribute
my_car.set_model("Camry")  # Modifying private attribute
print(my_car.get_model())  # Accessing modified private attribute
print(my_car.year)  # Accessing public attribute

# Output:
# Toyota
# Camry
# 2022

