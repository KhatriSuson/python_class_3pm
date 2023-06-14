# class Hello:
#     pass
# obj = Hello()

# call method through object
# class Hello:  # Class

#     # static method
#     def hello():  # method
#         print("Hello World")
#     obj = hello()   # object
#     obj.hello()


# class Hello:
#     def hello(self):
#         print("hello i am self parameter")
# obj = Hello()
# obj.hello()


# class Hello:
#     def hello(self):
#         print("I am self Parameter")
# obj = Hello()
# obj.hello()



# Use of static method
# class Cal:
#     @staticmethod
#     def cal():
#         l =10
#         b=3
#         a=l*b
#         print(a)
# obj = Cal()
# obj.cal()


# use self method
# class Cal:
#     def cal(self):
#         a = 34
#         b = 34
#         sum = a + b
#         print("sum of two number = ", sum)
# ob = Cal()
# ob.cal()


# class Cal:
#     def cal(self,l,b):
#         area = l * b
#         print(area)
# l = 23
# b = 21
# ob = Cal()
# ob.cal(l,b)       



# class Cal:
#     def __init__(self,l,b,h):
#         self.l = l
#         self.b = b
#         self.h = h

#     def cal(self):
#         a = self.l * self.b
#         print(a)
        
#     def vol(self):
#         v = self.l * self.b * self.h
#         print("The volume of given no is = ", v)

# l = 12
# b = 10
# h = 3
# obj = Cal(l,b,h)
# obj.cal()
# obj.vol()



class Info:
    def __init__(self):
        self.name = input("Enter Your Name = ")
        self.age = int(input("Enter Your Age = "))
        self.address = input("Enter Your Address = ")
    def info(self):
        print(f"My name is {self.name}. I am from {self.address}. and I am {self.age}. years old.")

obj = Info()
obj.info()
print(obj.name)
print(obj.age)
print(obj.address)


