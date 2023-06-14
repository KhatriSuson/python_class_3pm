# # Public members
# # class Info:
# #     def __init__(self):
# #         self.name = "Ram"
# #         self.age = 34
# #         self.add = "Bhaktpur"

# # obj = Info()
# # print(obj.name)
# # print(obj.age)
# # print(obj.add)


# # # Protected members

# # class Info:
# #     def __init__(self):
# #         self._name = "Ram"
# #         self._age = 34
# #         self._add = "Bhaktpur"

# # obj = Info()
# # print(obj._name)
# # print(obj._age)
# # print(obj._add)




# class A:
#     def __init__(self):
#         self.name = "Ram"
#         self._age = 45
#         self.__add = "Ktm"

#     def infos(self):
#         print(f"Hello world i am {self.name}. I am {self._age}. I am from {self.__add}")


# class B(A):
#     def info(self):
#         print(f"Hello world I am {self.name}. I am {self._age}")


# obj = B()
# obj.info()
# obj.infos()



# Multiple Inheritance

# class A:
#     def __init__(self):
#         self.__add = "kathmandu"

#     def add(self):
#         return self.__add

# class B:
#     def __init__(self):
#         self._age = 69

# class C(A,B):
#     def __init__(self):
#         self.name = "Ram"
#         B.__init__(self)
#         A.__init__(self)

#     def info(self):
#         add = A.add(self)
#         print(f"Hello world i am {self.name}. I am {self._age}. I am from {add}")


# obj = C()
# obj.info()




class A:
    def __init__(self):
        self.__add = "ktm"

    def add(self):
        return self.__add
    
class B:
    def __init__(self):
        self._age = 56

class C(A,B):
    def __init__(self):
        self.name = "Ram"
        B.__init__(self)
        A.__init__(self)

    def info(self):
        add = A.__add(self)
        print(f"Hello World {self.name}. I am from {add}. I am {self._age}")

obj = C()
obj.info()