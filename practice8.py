class takemyarguments():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Display(self):
        print("Name is: ",self.name)
        print("Age is: ",self.age)
Student = takemyarguments("Praveen",20)
Student.Display()           
#
# def greeting():
#     print("Good Morning ")

# greeting()

# def average(a,b,c):
#     return(a+b+c)/3

# avg = average(3,6,3)
# print(avg)    

# def greet(name):
#     gr = "Hello" + name
#     return gr
# a =greet("Praveen")    
# print(a)

#que-1
# def greatest(a,b,c):
#     if(a>b and a>c ):
#         return a
#     elif(a<b and c<b ):
#         return b
#     elif( c>a and c>b):
#         return c
                
# largest_number = greatest(5555,6,235425)   
# print(largest_number)  
# 2nd method    
# def greatest(a,b,c):
#     if(a>b):
#         greater = a
#     else:
#         greater = b
#     if(c>greater):
#         greater = c
#     return greater 
# largest_number = greatest(3,6,4)
# print(largest_number)              
#question-2
# def conversion(temp):
#     farenheit = (temp * 9/5) + 32
#     return farenheit

# celsius = conversion(40)
# print(celsius)
#que-4
# def sum(n):
#     return (n*(n+1))/2
# a = sum(4)
# print(a)
# 
# def print_pattern(n):
#     for i in range(n):
#         print("*"*(n-i))
#     i+=1    
# print_pattern(6)
#que-7
# def process(list,word):
#     word = word.strip()
#     list.remove(word)
#     return list
# l1= ["apple","banana","praveen"]
# a = process(l1,"praveen")
# print(a)
#que-8
# def multiplication_table(n):
#     for i in range(1,11):
#         print(n,"X",i,"=",n*i)

# multiplication_table(6)       
# from math import*
# print(sin(45))



