# print("practice start for 10 days study ")

print("first number", 
 5, 6, 7, 
      sep="-", end="\n")
print("second number",
       8, 9, 10, sep="*", end="king ") 
print("third number", 11, 12, 13, sep="&", end=
      "jis college of engineering")

# variables and data types practice
a = 123
b = "hello world"
c = 45.67
d = True
e = None
print("value of a:", a,
       "type of a:", type(a))
print("value of b:"
      , b, "type of b:", type(b))
print("value of c:", c, "type of c:", 
      type(c))
print("value of d:",
       d, "type of d:", type(d))
print("value of e:",
      e, "type of e:", type(e)
      )
# sequence data types list and tuple
list = [123, 34, 34,
         "hello",
           34, 1234, 
           "world",
             True]
print(list)

list = ["name: atif", "age:", 20,
        "can_vote:", True]
print(list) 

list = [8, 2.3,[-4, 5], 
        ["list,py", "python devloper"]]
print(list) 

tuple = (123, 34, 34,
         "hello python developer",
         34, 1234,
         "world is great",
         True)
print(tuple)

tuple = (("name: atif", "age:", 20,
          "can_vote:", False))
print(tuple)

#mapped data type dictionary
dict = {"name": "python",
         "age": 26,
           "high level lngauge": 
           True}
print(dict)

# typecasting practice
# implicit typecasting
a = 2000
b = 34.56
print ("the value of a + b =",(a + b))

a = 1000345.234224
b = 123345678453
print ("the value of a+b =", (a+b))

# explicit typecasting
a = "100"
b = 200
print("the value of a + b =", (int(a) + b))

a = 123.456
b = 345
print("the value of a +b =", a + float(b))

a = 345
b = "456.789"
print("the value of a + b =", str(a) + b)

# input function practice
variable = input("enter your name:")
print("my name is:", variable)

py = input("language name:")
print("I love", py)

num1 = input("enter first number:")
num2 = input("enter second number:")
print("the sum of two number is:",
       (num1 + num2))

num1 = input("enter first number:")
num2 = input("enter second number:")
print("the sum of two number is:",
       int(num1) + int(num2))

x = (input("name is:"))
print("i love you ",
       x)

l = int(input("length:"))
b = int(input("breadth:"))
area = l * b
print("the area of rectangle is:", area)

r = float(input("radius of circle:"))
pi = 3.14
area = pi * r * r
print("the area of circle is:", area)

# end of practice.py file





