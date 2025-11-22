# strings in python
name = "atif salim"
print("the name is:" + name)

apple = "he said, \"i want to eat an apple"
print(apple)

banana = 'she said, "i want to eat a banana'
print(banana)

mango = '''he said, "i want to eat a mango"'''
print(mango)

name = "atif"
surname = "salim"
full_name = name + " " + surname
print("the full name is:", full_name)

# string functions in python
name = "atif salim"
print("the length of name is:", len(name))
print("the uppercase of name is:", name.upper())
print("the lowercase of name is:", name.lower())
print("the replace function in name is:", name.replace("atif", "shaikh"))
print("the index of s in name is:", name.index("s"))
print("the count of a in name is:", name.count("a"))
print("the split function in name is:", name.split(" "))
print("the capitalize function in name is:", name.capitalize())

somthing = '''Python is a versatile, high-level programming language
 widely adopted across technology, data analytics, automation,
   and application development. Its clean syntax and extensive
     libraries enable rapid prototyping, scalable solution design, 
     and seamless integration with modern workflows.
       Organizations leverage Python to enhance operational efficiency,
         drive data-driven decision-making,
           and streamline complex processes through automation and machine learning.
             Its strong ecosystem, community support,
               and cross-platform capability make Python a strategic 
               asset for both individual developers and enterprise environments seeking agility
                 and innovation'''
print(somthing)   

N = "ATIF SALIM"
print(N[0])
print(N[1])
print(N[2])
print(N[3])
print(N[4])
print(N[5])
print(N[6])
print(N[7])
print(N[8])
print(N[9])
# print(N[10]) #this is inex error because stringa ends
# 9th degit thats why the 10th no is index error



print("lets use a for loop\n")

for character in N:
    print(character)

print("string slicing in python\n")

# string slicing
name = "atif, salim"
print(name[0:4])
print(name[6:11])

# length of string slicing

x = "catterpillar"
ans = len(x)
print("catterpiller is a", ans, "letter word.")

y = "hippopotamus"
len1 = len(y)
print(len1)

z = "elephant"
n = len(z)
print(n)
print(z[0:4])
print(z[4:8])
print(z[0:8])
print(z[2:6])

nm = "harry"
print(nm[-4:-2])

msg = "hello world"
print(len(msg))
print(msg[:])
# print(msg[3:-5]) #ans is lo 
# print(msg[-4:-3])

# wap to find a even or odd number by take input 
num = int(input("enter a number:"))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")  

# string methods in python upper()
str1 = "ADFJDFHsdjffjnfjSDHsdk"
print(str1.upper())

# string methods in python lower() 
print(str1.lower())
# string are immutable

# rstrip() method
a = "hello!!!!!!"
print(a.rstrip("!"))

#replace() method
b = "silver spoon "
print (b.replace("sp", "m"))
print(b.replace("silver", "golden"))

#split() method
c = "hello world welcome to python"
print(c.split(" "))
print(c.split("o"))

# capitalize() method
d = "hello world" 
print(d.capitalize()) 

#center() method
e = "the art of not overthining"
print(e.center(100))

# count() method
f = "atif salim atif salim atif"
print(f.count("atif"))
print(f.count("salim"))

# endswith() methods
g = "welcome to python programme"
print(g.endswith("to", 4, 10))

# find() method
h = " he's name is dan. he is an honest man."
print(h.find("is"))
k = " he's name is dan. he is an honest man."
print(k.find("ishh"))

# index() method
i = "ragib is multispeciality randi" 
print(i.index("is"))










      







