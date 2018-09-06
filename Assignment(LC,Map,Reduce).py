
#Question 1
#Write a python program to print the cube of each value of a list using list comprehension.
list=[1,2,3,4,5,6,7,8]
New_List=[x**3 for x in list]
print(New_List)



#Question 2
#Write a python program to get all the prime numbers in a specific range using list comprehension.
def IsPrime(x):
    for i in range(2,x-1):
        if(x%i==0):
            return False
    else:
        return True
num=int(input("Enter A Starting Number "))
nume=int(input("Enter A Ending Number Number "))
Ls=[]
for i in range(num,nume+1):
    Ls.append(i)
Primes=[i for i in Ls if IsPrime(i)]
print(Primes)



#Question 3
#Write the main differences between List Comprehension and Generator Expression.
#List Comprehension
#i) Returns A List.
#ii) Enclosed in []
#iii) Takes More Size
#iv) Can Access Elements by index.
#Generator Exppressons
#i) Returns a Generator Iterator which can be iterated over
#ii) Enclosed in ()
#iii) Takes Much Less Size
#iv) Cannot Access Element By Index



#Question 4
#Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
Celsius = [39.2, 36.5, 37.3, 37.8]
Farh=list(map(lambda x: (9/5)*x + 32, Celsius))
print(Farh)



#Question 5
#Apply an anonymous function to square all the elements of a list using map and lambda.
Nlist=[32,65,78,98,52,8,2,58,4,54,69]
Squares=list(map(lambda x:x**2,Nlist))
print(Squares)



#Question 6
#Filter out all the primes from a list.
def IsPrime(x):
    for i in range(2,x-1):
        if(x%i==0):
            return False
    else:
        return True
listN=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list1=list(filter(IsPrime,listN))
print(list1)



# Question 7
# Write a python program to multiply all the elements of a list using reduce.
from functools import reduce
listN=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Mul=reduce(lambda x,y:x*y,listN)
print(Mul)