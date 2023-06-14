# class A:
#     def __init__(self):
#         self.name = "Ram"
#         self.age = 45
#         self.add = "KTM"

# class B(A):
#     def info(self):
#         print(f"Hello world, I am {self.name}. I am from { self.age}. I am from {self.add}")
# obj = B()
# obj.info()

# class A:
#     def __init__(self,name,age,add):
#         self.name = name 
#         self.age = age 
#         self.add = add

# class B(A):
#     def info(self):
#         print(f"Hello world i am {self.name}. I am from {self.add}. I am {self.age}. Years old")

# obj = B("Ram", '45', 'Kathmandu')
# obj.info()

# class A:
#     def __init__(self,age,add):
        
#         self.age = age 
#         self.add = add



# class B(A):
#     def __init__(self,name,age,add):
#         self.name = name
#         A.__init__(self,age,add)
#     def info(self):
#         print(f"Hello world i am {self.name}. I am from {self.add}. I am {self.age}. Years old")

# obj = B("Ram", '45', 'Kathmandu')
# obj.info()


# Wrong try again 
# r
# class A:
#     def __init__(self,age,add):
        
#         self.age = age 
#         self.add = add
        

# class C(A):
#     def __init__(self,name,age,add,email):
#         self.email = email

# class B(C):
#     def __init__(self,name,age,add):
#         self.name = name
#         C.__init__(self,age,add)
#     def info(self):
#         print(f"Hello world i am {self.name}. I am from {self.add}. I am {self.age}. Years old. My email address is {self.email}")

# obj = B("Ram", '45', 'Kathmandu')
# obj.info()

# Multi-level
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# obj = C()




# class A:
#     def __init__(self,add):
#         self.add = add

# class B(A):
#     def __init__(self,age,add):
#         self.age = age
#         A.__init__(self,add)

# class C(A):
#     def __init__(self,name,age,add):
#         self.name = name
#         B.__init__(self,age,add)
#     def info(self):
#         print(f"Hello world, I am python multiple inheritanc {self.name}. i am number {self.age}. I am from {self.add}. ")


# obj = C("Ram ", "34", "ktm")
# obj.info()


# Multiple Inheritance VVI
# class A:
#     def __init__(self,add):
#         self.add = add

# class B:
#     def __init__(self,age,add):
#         self.age = age
        

# class C(A,B):
#     def __init__(self,name,age,add):
#         self.name = name
#         B.__init__(self,age,add)
#         A.__init__(self,add)
#     def info(self):
#         print(f"Hello world, I am  inheritanc {self.name}. i am number {self.age}. I am from {self.add}. ")


# obj = C("Ram ", "34", "ktm")
# obj.info()

# class A:
#     def __init__(self,name):
#         self.name = name 
# class B:
#     def __init__(self,name,age):
#         self.age = age
        
# class C(A,B):
#     def __init__(self, name, age, add):
#         self.add = add
#         A.__init__(self,name)
#         B.__init__(self,name,age)

#     def info(self):
#         print(f"Hello world, I am {self.name}. I am from {self.add}. I am {self.age}. years old. ")



obj = C("Ram ", "23" "ktm")
obj.info()