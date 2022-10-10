# class Employee():
#     name = "Praveen"
#     employee_id = 356
#     branch = "Hyderabad"

#     def printObj(self):
#         print(f"the name of the employee is {self.name}")
#         return
# praveen = Employee()
# print(praveen.name)
# praveen.printObj()

#que-1
# class programmer():
#     def __init__(self,name,language):
#         self.name = name
#         self.language = language

# microsoft = programmer("praveen","python")
# print(microsoft.name)

#que-2
# class calculator:
#     def __init__(self,number):
#         self.number = number
#        #method 1
#         print(f"the square of the number is {number*number}")
#         print(f"the cube of the number is {number*number*number}") 
#         print(f"the squareroot of the number is {number**(1/2)}") 
#     #method-2
#     def square(self):
#         return self.number* self.number
# required_number = calculator(9)
# print(required_number.square())

#que-3
# class calculator:
#     a = 30

# object = calculator()
# object.a = 0
# print(object.a)    


class Train:
    def __init__(self,seats,fare):
        self.seats = seats 
        self.fare = fare
    def booktickets(self):
        print("Your ticket is booked")
        self.seats -= 1
    def getstatus(self):
        print(f"seats remaining are {self.seats}")
    def getfare(self):
        print(f"cost of the ticket is {self.fare}") 

rajdhani = Train(100,1800)
rajdhani.booktickets()
rajdhani.getstatus()
rajdhani.getfare()
