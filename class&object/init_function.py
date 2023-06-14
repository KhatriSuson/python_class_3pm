# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("Ram", 45)
# print(p1.name)
# print(p1.age)



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return(f"{self.name}.\n {self.age}")

# p1 = Person("shyam", 34)
# print(p1)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello My nai is " + self.nameA)

p1 = Person("Ram", "34")
p1.myfunc()

