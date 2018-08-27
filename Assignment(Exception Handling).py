#Question 1
#Name and handle the exception occured in the following program
#The Exception in the Code is Zero Division Error

try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("You Cannot Deivide By Zero")


#Question 2
# Name and handle the exception occurred in the following program:
# The Error in The Code is INDEX ERROR

try:
    l=[1,2,3]
    print(l[3])
except:
    print("Please Enter an Index which is less than {}".format(len(l)))


#Question 3
# Tell The output
#The output Of the Following Code is An Exception


#Question 4
#Output of The FolloWing Code
#The Result is
#-5.0
#a/b result in 0


#Question 5
# Write a program to show and handle following exceptions:
#1. Import Error
#2. Value Error
#3. Index Error
#The Following Code is for Import Error
try:
    import nmb
except ImportError:
    print("Please Import Valid Module")
#The Following Code is for showing and handling Value Error
try:
    a=int(input("Enter a Number "))
    #We Encounter an Indexerrorif we enter an string va;ue in the variable
except:
    print("Please Enter a valid Number")
#The Following code is for handling IndexError
try:
    l=[4,5,6]
    print(l[4])
except:
    print("Please Enter A valid Index")