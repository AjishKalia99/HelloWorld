#Question 1
L1=[]
L1.append(input("Enter First Element "))
L1.append(input("Enter Second Element "))
L1.append(input("Enter Third Element "))
L1.append(input("Enter Fourth Element "))
L1.append(input("Enter Fifth Element "))

#Question 2
L2=['google','apple','facebook','micrososft','Tesla']
L3=L1+L2
print(L3)

#Question 3
find=input("Enter to find the occurence of the element ")
print(L1.count(find))

#Question 4
L4=[4,8,9,7,65,64,68,2,5,2,5]
L4.sort()
print(L4)

#Question 5
L5=[1,2,3,5,5,9]
L6=[1,4,6,9,12,54,68,98]
L5.extend(L6)
L5.sort()
print(L5)

#Question 6
#If else and iterators have not been covered yet but this questions has been attempted from the helpof the internet at the resources from the previous class
even=0
odd=0
for i in range(0,len(L5)):
    if L5[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)

#Question 7 and 8
#Question 7 and 8 could not be attempted as the topic TUPLES has not been covered in class

#Question 9
a="Hi my name is ajish kalia"
a.upper()

#Question 10
ab=input("Enter a string ")
print(ab.isdigit())

#Question11
abc="Hello World"
L7=abc.split()
L7[1]=input("Enter Your name ")
print(" ".join(L7))


