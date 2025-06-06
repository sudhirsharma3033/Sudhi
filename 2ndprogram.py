#arithmetic operations
a = 5
b = 2

print(a+b)  # Addition
print(a-b)  # Subtraction
print(a*b)  # Multiplication
print(a/b)  # Division
print(a % b)  # Modulus   # Remainder
print(a ** b)  # Exponentiation   #a^b
print(a // b)  # Floor Division   # Quotient



#relational operations
a = 50
b = 20

print(a == b)  # Equal to     #False
print(a != b)  # Not equal to    #True
print(a >= b)  # Greater than   #True
print(a <= b)  # Less than   #False
print(a >= b)  # Greater than   #True
print(a <= b)  # Less than   #False



#assignment operations
num = 10
num = num + 10  #10+10 => 20 
num += 10  #10+10 => 20    #it's same in + , - , * , / , % , ** , //
num -= 5  #20-5 => 15
num *= 2  #15*2 => 30
num /= 3  #30/3 => 10.0
num %= 4  #10.0%4 => 2.0
num **= 3  #2.0**3 => 8.0
num //= 2  #8.0//2 => 4.0  

print("num : ", num)




#logical operations

print(not True)  # False
print(not False)  # True

a = 50
b = 30
print(not False)
print(a > b)

val1 = True
val2 = True
print("ans operator : ", val1 and val2)  # True

val1 = True
val2 = False
print("ans operator : ", val1 and val2)  # False

val1 = False
val2 = True
print("ans operator : ", val1 and val2)  # False

print("OR operator : ", (a == b) or (a > b))  # True
print("OR operator : ", (a == b) or (a < b))  # False


