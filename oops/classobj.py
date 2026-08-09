# class student:
#   pass
# student1=student()
# print(student1)
# class jash:
#   name=name.self
#   age=age.self
# st1=jas
# class student:
#   pass
# student1=student()
# student1.name="jashwanth"
# student1.age=22
# print(student1.name)
# print(student1.age)
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# student1=student("jash",22)
# print(student1.name)
# print(student1.age)
# class nani:
#   def __init__(self,salary,bonus):
#     self.salary=salary
#     self.bonus=bonus
# employee1=nani(50000,5000)
# print(employee1.salary)
# print(employee1.bonus)
# class cars:
#   def __init__(self,make,model,year):
#     self.make=make
#     self.model=model
#     self.year=year
# car1=cars("Toyota","Camry",2020)
# print(car1.make)
# print(car1.model)
# print(car1.year)
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# student1=student("jash",22)
# student2=student("nani",21)
# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# student1=student("jash",22)
# student2=student("nani",21)
# student1.greet()
# student2.greet()
# class car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#     def display_info(self):
#         print(f"Car Make: {self.make}")
#         print(f"Car Model: {self.model}")
#         print(f"Car Year: {self.year}")
# car1=car("Toyota","Camry",2020)
# car1.display_info()
class bike:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(f"bike make:{self.make}")
        print(f"bike mode:{self.model}")
        print(f"bike year:{self.year}")
bike1=bike("pulsur",220,2018)
bike1.display()