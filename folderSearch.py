import os
import re
import shutil
import sys


count = 0
def  merge (rootfolder, targetfolder=os.getcwd()+"\\test"):
    global count
    print(targetfolder)

    fileList = []
    for filename in os.listdir(rootfolder):
        if filename == "Result":
            continue
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
        fileList.append((filename, float(temp[0])))
    fileList.sort(key=lambda x : x[1])
    print(fileList)

    for fileName , fileNum in fileList:
        fileAddress = rootfolder + "\\" + fileName
        
        if os.path.isfile(fileAddress):
            print("[FILE]"+fileAddress)
            name, extension = os.path.splitext(fileAddress)
            shutil.copyfile(fileAddress,targetfolder+"\\"+str(count)+extension)
            count += 1

        elif os.path.isdir(fileAddress):
            merge(fileAddress,targetfolder)
        else:
            print("RAISE ERROR")

if __name__ == "__main__":

    merge(rootfolder="E:\Entertainment\만화\[미나모토 아키라] 여왕 폐하의 이세계 전략")
