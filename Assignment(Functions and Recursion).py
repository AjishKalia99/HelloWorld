#Question 1
#Create a function to calculate the area of a sphere by taking radius from user.

def Area(rad):
    ar=4*3.14*(rad**2)
    return ar

rad=float(input("PLease Enter The radius of the Sphere "))
print(Area(rad))


#Question 2
#Write a function “perfect()” that determines if parameter number is a perfect number.
#Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.

def perfect(num):
    fact=list()
    sum=0
    for i in range (1,num-1):
        if(num%i==0):
            fact.append(i)
        else:
            continue
    for i in range(0,len(fact)):
        sum=sum+fact[i]
    if(sum==num):
        return True
    else:
        return False
perf=list()
for i in range(1,1000):
    if(perfect(i)):
        perf.append(i)
print(perf)


#Question 3
#Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
i=1
def Table(n,i):
    if(i==10):
        print("{} X {} = {}".format(n,i,n*i))
    else:
        print("{} X {} = {}".format(n,i,n*i))
        return Table(n,i+1)
num=int(input("Enter The Number You Wanna Know the Table of :- "))
Table(num,1)


#Question 4
#Write a function to calculate power of a number raised to other ( a^b ) using recursion.
i=1
pro=1

def Pow(a,b,i):
    global pro
    if(i==b):
        return pro*a
    else:
        pro=pro*a
        return Pow(a,b,i+1)
a=int(input("Enter The Number A:-"))
b=int(input("Enter The Number B:-"))
print("The Value of A^B is : %d"%Pow(a,b,i))