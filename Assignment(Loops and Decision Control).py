#Question 1
#Take an input year from user and decide whether it is a leap year or not.
Yr=int(input("Please Enter an year "))
if(Yr%4==0):
    print("The Entered year is a leap Year")
else:
    print("The Entered year is not a leap Year")


#Question 2
#Take length and breadth input from user and check whether the dimensions are of square or rectangle.
lnt=int(input("Please Enter The Length of the shape"))
brd=int(input("Please Enter The Breadth of the shape"))
if(lnt==brd):
    print("The Shape is a Square ")
else:
    print("The Shappe is a Rectangle ")


#Question 3
#Take the input age of 3 people and determine oldest and youngest among them.
age=[]
age.append(int(input("Enter The age of the First person ")))
age.append(int(input("Enter The age of the Second person ")))
age.append(int(input("Enter The age of the Third person ")))
max=0
min1=100
for i in range (0,len(age)):
    if (age[i]>=max):
        max=age[i]
    else:
        if (age[i]<min1):
            min1=age[i]
print("The Maximum Age is %d"%(max))
print("The Minimum Age is %d"%(min1))


#Question 4
#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#1. if employee is female, then she will work only in urban areas.
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#4. And any other input of age should print "ERROR".

sex=['M','F']
mar_Stat=['Y','N']
age=int(input("PLease Enter Your Age"))
Sx=input("Please Enter Your Sex (M/F)")
sx1=Sx.upper()
MS=input("Please Enter Your Marital Status (Y/N)")
MS.upper()
if(sx1 in sex):
    if(sx1=='M'):
        if(age>=20 and age<=40):
            print("You Can Work Anywhere")
        elif(age>40 and age<=60):
            print("You Will Work in Urban Areas only")
        else:
            print("ERROR")
    else:
        print("You Will Work in Urban Areas")
else:
    print("Please Enter Valid Sex")


#Question 5
#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity Suppose, one unit will cost 100.
#Judge and print total cost for user.

quant=int(input("Please Enter Quantity of the Item "))
prc=quant*100
if(prc>1000):
    print("The Total Cost for You is %d"%(0.9*prc))
else:
    print("The Total Cost for You is %d"%(prc))


#Question 6
#Take 10 integers from user and print it on screen.

inte=list()
for i in range(0,10):
    num=int(input("Enter A Integer Please "))
    inte.append(num)
print("The added numbers are: ")
for i in range(0,10):
    print(inte[i])


#Question 7
#Write An Infinite Loop

while True:
    print("INFINITE")


#Question 8
#Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
int2=[]
int3=list()
for i in range (0,10):
    int2.append(int(input("Enter A Number ")))
    int3.append(int2[i]*int2[i])
print("The Squares of numbers are ")
for i in range (0,10):
    print(int3[i])



#Question 9
#From a list containing ints, strings and floats, make three lists to store them separately
list1=[1,2,3,4,'ajish','kalia',2.20,'wassap',5]
list_int=list()
list_string=list()
list_float=list()
a=list()
for i in range(0,len(list1)):
    a.append(str(list1[i]))
for i in range(0,len(a)):
    if(a[i].isdigit()):
        list_int.append(int(a[i]))
    else:
        if(a[i].isalpha()):
            list_string.append(a[i])
        else:
            list_float.append(float(a[i]))
print("The Float Elements are:-")
print(list_float)
print("The Integer Elements are :-")
print(list_int)
print("The String Elements are :-")
print(list_string)



#Question 10
#Using range(1,101), make a list containing only prime numbers.
prime=list()
prime.append(1)
for i in range (2,100):
    for j in range(2,i-1):
        if(i%j==0):
            break
    else:
        prime.append(i)
prime.append(101)
print(prime)



#Question 11
#Print the following patterns:
for i in range(1,5):
    print("*"*i)



#Question 12
#Take inputs from user to make a list.
#Again take one input from user and search it in the list and delete that element, if found.
#Iterate over list using for loop.
inpu=list()
for i in range(0,10):
    num=input("Enter The Element")
    inpu.append(num)
srch=input("Enter The Elemet to Delete from the List")
for i in range(0,len(inpu)-1):
    if(inpu[i]==srch):
        inpu.remove(srch)
else:
    print("Element not found")
print(inpu)