# Question 1
# Create a user defined dictionary and get keys corresponding to the value using for loop.
#{'K1':'C','K2':'C++','K3':'Java','K4':'Python','K5':'Ruby'}
Dict=eval(input("Please Enter a Dictionary"))
print(Dict)
for key in Dict:
    print("The Key for the Value {} is {}".format(Dict[key],key))
# Question 1
# Create a user defined dictionary and get keys corresponding to the value using for loop.
#{'K1':'C','K2':'C++','K3':'Java','K4':'Python','K5':'Ruby'}
Dict=eval(input("Please Enter a Dictionary"))
print(Dict)
for key in Dict:
    print("The Key for the Value {} is {}".format(Dict[key],key))


#Question 2
# Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.
# Print the marks of a given student from that dictionary for every subject.
D=dict()
marks=dict()
Mks=list()
Final=list()
n=int(input("Enter The Total Number of Students"))
for i in range (0,n):
    Name=input("Please Enter Students Name ")
    Python=int(input("Please Enter Students Marks in Python "))
    Java=int(input("Please Enter Students Marks in Java "))
    Cpp=int(input("Please Enter Students Marks in C++ "))
    D={'Name':Name.upper(),'Marks':{'Python':Python,'Java':Java,'C++':Cpp}}
    Final.append(D)
print(Final)
N_Find=input("Enter The Name of the student to find Marks ")
N_Find=N_Find.upper()
for i in range (0,len(Final)):
    if(N_Find==Final[i]['Name']):
        print("The name of the student is : %s" %Final[i]['Name'])
        print("The marks of the student in Python are : %d" %(Final[i]['Marks']['Python']))
        print("The marks of the student in Java are : %d" %(Final[i]['Marks']['Java']))
        print("The marks of the student in C++ are : %d" %(Final[i]['Marks']['C++']))
        break
    else:
        continue
else:
    print("Student Not Found")