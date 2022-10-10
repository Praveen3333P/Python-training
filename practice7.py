# i = 1
# while(i<=50):
#     print(i)
#     i += 1

#question-1
# a = int(input("Enter the number"))
# i = 1
# while(i<11):
#     print(a*i)
#     i += 1
    
#question-8
n = int(input("Enter a number: "))
k = 1
for i in range(0,n):
    for j in range(0,k):
        print("* ",end="") 
    k += 1 
    print() 

#question-9
# n = int(input('Enter the number: '))
# for i in range(0,n):
#     for j in range(0,n):
#         if(i ==0 or j==0 or i==n-1 or j==n-1):
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print("\n", end="")        