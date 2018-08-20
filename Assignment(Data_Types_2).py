#Question 1
# Reverse a List using List Functions
list1=[1,2,3,4]
list1.reverse()
print(list1)

#Question 2
#Print the Uppercase Letters from a String
str1="A Boy is STANDING"
a=len(str1)
for i in range(0,a):
    if str1[i].isupper():
        print(str1[i])


#Question 3
#Split the user input on comma's and store the values in a list as integers.
str1="123,2,3,4,5,6"
list1=str1.split(",")
list2=[]
for i in range(0,len(list1)):
    list2.append(int(list1[i]))
print(list2)


#Question 4
#Check whether a string is palindromic or not.
str1="12321"
str2=str1[::-1]
if(str2==str1):
    print("Palindrome")
else:
    print("Not Palindrme")


#Question 5
#Make a deepcopy of a list and write the difference between shallow copy and deep copy.
import copy as cpy
list1=[1,2,3,[4,5],6]
list2=[1,3,4,5,[6,7],8]
list3=cpy.copy(list1)
list4=cpy.deepcopy(list2)
print("List 1 :")
print(list1)
print("List 2 :")
print(list2)
print("List 3 :")
print(list3)
print("List 4 :")
print(list4)
list1[3][0]='Hello'
list2[4][0]="hi"
print("List 1 :")
print(list1)
print("List 2 :")
print(list2)
print(" Shallow copied List 3 :")
print(list3)
print("Deep Copied List 4 :")
print(list4)

#This Example Shows us that:
#Shallow Copy:
# It is a bit-eise copy of the object, that is, if The object contains a refrence to some other object
# The refrence of the object is also copied, that is,The Memory Addresses are also copied
#Deep Copy:
# It Copies all the fields of the object, That is,if the object contains a refrence to some other object
# A new copy of the referred object is also created.