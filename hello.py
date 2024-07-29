print("Hello World!")  # Print command
print(" ")

age = float(input("Enter age: "))  # User assigned value to variabe

num_age = 22  # Integer value
float_pi = 3.14  # Float value
print(num_age, float_pi)
print(" ")
print(" ")

if age >= 18:
    print("You can vote")
elif age < 18:  # If-elif-else
    print("You cannot vote")
else:
    print("Enter correct age")

print(" ")
print(" ")


my_location = [1, 2, 3, "Kanishk", 4.4]  # List
print(my_location)
print(" ")
print(" ")

my_tuple = (1, 2, 3, "21BCS10520", 4.4)  # Tuple
print(my_tuple)
print(" ")
print(" ")

iterable = [1, 2, 3, 4, 5]
for item in iterable:  # For loop
    print(item)
print(" ")
print(" ")

while iterable:  # While Loop
    print(iterable.pop())
print(" ")
print(" ")


def greet(name="Kanishk"):
    print("Hello " + name + "!")


print(" ")
print(" ")


greet("Kanishk")  # Function call
greet()
print(" ")
print(" ")


def add(a, b=20):  # Default parameter
    return a + b


print(" ")
print(" ")
print(add(2, 3))
print(add(2))


# class Dog:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# ozzy = Dog("Ozzy", 8)

# print(ozzy.name, ozzy.age)
