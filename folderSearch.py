import os
import re
import shutil
import sys


count = 0

def  merge (rootfolder, targetfolder):
    global count
    print(targetfolder)

    fileList = []
    for filename in os.listdir(rootfolder):
        

        temp = []
        if temp == [] :
            temp = re.findall("\d+-\d+",filename)
            
            if temp != []:
                temptemp = re.findall("\d+",str(temp))
                print("temptemp",temptemp)
                temp = [float(temptemp[0]) + float(temptemp[1])*0.0001]


        if temp == []:
            temp = re.findall("\d+~\d+",filename)
            if temp != []:
                temptemp = re.findall("\d+",str(temp))
                print("temptemp",temptemp)
                temp = temptemp[0]
        if temp == [] :
            temp = re.findall("\d+.\d+",filename)
            
        if temp == []:
            temp = re.findall("\d+",filename)

        if temp == [] :
            temp = [-1]
        fileList.append((filename, float(temp[0])))
    fileList.sort(key=lambda x : x[1])
   

    for fileName , fileNum in fileList:

        if fileNum == -1:
            continue

        fileAddress = rootfolder + "\\" + fileName
        
        if os.path.isfile(fileAddress):
            print("[FILE]"+fileAddress)
            name, extension = os.path.splitext(fileAddress)
            try: 
                shutil.copyfile(fileAddress,targetfolder+"\\"+str(count).zfill(6)+extension)
            except shutil.SameFileError :
                pass
            count += 1

        elif os.path.isdir(fileAddress):
            merge(fileAddress,targetfolder)
        else:
            print("RAISE ERROR")

if __name__ == "__main__":

    pass
