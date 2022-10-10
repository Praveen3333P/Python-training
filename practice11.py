
# class Vector2d:
#     def __init__(self,x,y) -> None:
#         self.x = x
#         self.y = y
#     def MainVector(self):
#         print(f"{self.x}i + {self.y}j")    
# class Vector3d(Vector2d):
#     def __init__(self,x,y,z) -> None:
#         super().__init__(x,y)
#         self.z = z
#     def MainVector(self):
#         print(f"{self.x}i + {self.y}j + {self.z}k")

# vector = Vector2d(1,2)
# vector = Vector3d(1,2,3)
# vector.MainVector()     

#Que-2
# class Animals:
#     def __init__(self) -> None:
#         print("This is the animals group")
# class Pets(Animals):
#     def __init__(self) -> None:
#         print("This the pets grp derived from the animals")
# class Dog(Pets):
#     def __init__(self) -> None:
#         print("Dog is one of the pet")
#     def bark():
#         print("The dog barks")

# bulldog = Dog()
# Dog.bark()

#Que-3

# class Employee:
#     def __init__(self,salary,increment):
#         self.salary = salary
#         self.increment = increment
#     @property    
#     def SalaryAfterIncrement(self):
#         return self.salary * (1 + self.increment)
#     @SalaryAfterIncrement.setter
#     def SalaryAfterIncrement(self):
#         self.salary =  self.salary * (1 + self.increment)

# employee1 = Employee(30000,0.2)
# print(employee1.SalaryAfterIncrement)
# employee1.SalaryAfterIncrement = 36000

print("kodta ra reyyy..")

