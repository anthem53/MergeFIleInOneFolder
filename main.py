from operator import truediv
import os
import re
import shutil
import sys
import folderSearch
import math

from PyQt5 import uic
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
                             QTextEdit, QMessageBox,QListView,QTreeView,QFileSystemModel,QAbstractItemView)


form_class = uic.loadUiType("pyqtUI.ui")[0]


class FileDialog(QFileDialog):
    def __init__(self, *args):
        QFileDialog.__init__(self, *args)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.DirectoryOnly)

        for view in self.findChildren((QListView, QTreeView)):
            if isinstance(view.model(), QFileSystemModel):
                view.setSelectionMode(QAbstractItemView.ExtendedSelection)

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.fileDialog = FileDialog()
        
        self.setupUi(self)
        self.findButton.clicked.connect(self.findButtonClick)
        self.mergeButton.clicked.connect(self.mergeButtonClick)
        self.clearButton.clicked.connect(self.clearButtonClick)
        self.testButton.clicked.connect(self.testButtonClick)
        self.targetFolderList.itemDoubleClicked.connect(self.targetFolderListDoubleClick)
        self.progressBar.setValue(0)
        

    def findButtonClick(self):
        self.fileDialog.show()
        self.fileDialog.exec_()
        
        for file in self.fileDialog.selectedFiles():
            print(type(file),file)
            isExisted = False
            for i in range(self.targetFolderList.count()):
                temp = self.targetFolderList.item(i).text()
                if  temp == file:
                    isExisted = True
                    break 
            if isExisted == False:
                self.targetFolderList.addItem(file)

    def mergeButtonClick(self):

        for i in range(self.targetFolderList.count()):
            currentRootAddress = self.targetFolderList.item(i).text()
            dirList = currentRootAddress.split("/")
            dirName = dirList[-1]
            rootfolder = "/".join(dirList[0:-1])
            savedfolderName = "(Merged)"+dirName

            if currentRootAddress == "":
                continue
            #if dirName not in os.listdir(currentRootAddress):
                #os.mkdir(currentRootAddress+"/"+dirName)
            if dirName + "(Merged)" not in os.listdir(rootfolder):
                try:
                    os.mkdir(rootfolder + "/"+ savedfolderName)
                except FileExistsError:
                    shutil.rmtree(os.path.join(rootfolder + "/"+ savedfolderName))
                    os.mkdir(rootfolder + "/"+ savedfolderName)
                
            self.logText.setText(currentRootAddress)

            

            currentSaveFolder = rootfolder + "/"+savedfolderName
            folderSearch.count = 0 
            folderSearch.merge(currentRootAddress,currentSaveFolder)
            progressValue = math.ceil((i+1)/self.targetFolderList.count()*100)
            self.progressBar.setValue(progressValue)
        QMessageBox.about(self, 'Process Complete', '작업 완료 했습니다.')
        print('작업 완료 했습니다.')
        self.logText.setText('작업 완료 했습니다.')
    def clearButtonClick(self):
        self.targetFolderList.clear()

    def testButtonClick(self):
        print("testButton Clicked")
        pass
        pass

    def targetFolderListDoubleClick(self):
        self.targetFolderList.takeItem(self.targetFolderList.currentRow())

    def updatePbar(self, value):
        self.progressBar.setValue(value)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

    #folderSearch.folderSearch(rootfolder="E:\Entertainment\만화\[미나모토 아키라] 여왕 폐하의 이세계 전략")
    #folderSearch(rootfolder="E:\Entertainment\만화\[미나모토 아키라] 여왕 폐하의 이세계 전략")
