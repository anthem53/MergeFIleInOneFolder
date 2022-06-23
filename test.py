from fileinput import filename
import os
import re


list = []

rootfolder=  "E:\\Entertainment\\TEST\\testfolder3"



for filename in os.listdir(rootfolder):
    print(filename)

    check =0

    temp = []

    if temp == [] :
        temp = re.findall("\d+-\d+",filename)
        
        if temp != []:
            temptemp = re.findall("\d+",str(temp))
            print("temptemp",temptemp)
            temp = [float(temptemp[0]) + float(temptemp[1])*0.0001]


    if temp == []:
        temp = re.findall("\d+~\d+",filename)
        check = 0
        if temp != []:
            temptemp = re.findall("\d+",str(temp))
            print("temptemp",temptemp)
            temp = temptemp[0]
    if temp == [] :
        temp = re.findall("\d+.\d+",filename)
        

        
    if temp == []:
        temp = re.findall("\d+",filename)
        check = 2




    print(check)
    print("temp",temp, end="\n\n")
    7
    list.append((filename, float(temp[0])))


list.sort(key=lambda x : x[1])
print(list)
print()