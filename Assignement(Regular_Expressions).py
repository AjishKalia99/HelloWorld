#Question1
#Find a Valid Email Address From a Text

import re
Text=input("Please Enter The Text ")
M=Text.split(' ')
count=0
for i in range(0,len(M)):
    match=re.finditer('^[a-zA-z0-9][a-zA-Z0-9_.]*@(gmail.com|yahoo.com)',M[i])
    for m in match:
        print("Match Found: {} after Word {}".format(m.group(),i))
        count=count+1
if count==0:
    print("Match Not Found")


#Question2
#Find a Valid Indian Phone Number From a Text

import re
Text=input("Please Enter The Text ")
M=Text.split(' ')
count=0
for i in range(0,len(M)):
    match=re.finditer('^[+][9][1][6789][0-9]{9}',M[i])
    for m in match:
        print("Match Found: {} as after Word {}".format(m.group(),i))
        count=count+1
if count==0:
    print("Match Not Found")