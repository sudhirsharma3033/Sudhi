#TYPE CONVERSION
# Implicit Type Conversion



a = 2
b = 4.25


sum = a + b # 2 + 4.25 => 6.25
print(sum)  # Output: 6.25
print(type(sum))  # Output: <class 'float'>


a = int("2")
b = 4.25


print(type(a))  # Output: <class 'int'>
print(a + b)  # Output: 6.25
print(type(a + b))  # Output: <class 'float'>


a = 3.14
a = str(a)  # Convert float to string
print(type(a))  # Output: <class 'str'>



