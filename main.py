import os
import re
import shutil
import sys
import folderSearch
import math

from PyQt5 import uic
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
                             QTextEdit, QMessageBox,QListView,QTreeView,QFileSystemModel,QAbstractItemView)


form_class = uic.loadUiType("dialogui - 복사본.ui")[0]


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
        self.findButton.clicked.connect(self.findButtonClick3)
        self.mergeButton.clicked.connect(self.mergeButtonClick)
        self.clearButton.clicked.connect(self.clearButtonClick)

        self.progressBar.setValue(0)
        
    def findButtonClick(self):
        print("findButtonClick 클릭됨.")
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        print(fname)
        self.targetFolderAddress.setText(fname)
        if fname != "":
            self.saveFolderAddress.setText(fname+"/Result")
    def findButtonClick2(self):
        files = self.fileDialog.getOpenFileNames(self)

        for file in files[0] :
            print(file,type(file))
            self.targetFolderList.addItem(file)

        for i in range(self.targetFolderList.count()):
            print(self.targetFolderList.item(i).text())

        pass
        pass

    def findButtonClick3(self):
        self.fileDialog.show()
        self.fileDialog.exec_()
        
        for file in self.fileDialog.selectedFiles():
            print(type(file),file)
            self.targetFolderList.addItem(file)

    def mergeButtonClick(self):

        for i in range(self.targetFolderList.count()):
            currentRootAddress = self.targetFolderList.item(i).text()

            if currentRootAddress == "":
                continue
            if "Result" not in os.listdir(currentRootAddress):
                os.mkdir(currentRootAddress+"/"+"Result")
                
            self.logText.setText(currentRootAddress)
            currentSaveFolder = currentRootAddress + "/Result"
            folderSearch.count = 0 
            folderSearch.merge(currentRootAddress,currentSaveFolder)
            progressValue = math.ceil((i+1)/self.targetFolderList.count()*100)
            self.progressBar.setValue(progressValue)
        QMessageBox.about(self, 'Process Complete', '작업 완료 했습니다.')
        print('작업 완료 했습니다.')
        self.logText.setText('작업 완료 했습니다.')
    def clearButtonClick(self):
        self.targetFolderList.clear()
    def updatePbar(self, value):
        self.progressBar.setValue(value)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

    #folderSearch.folderSearch(rootfolder="E:\Entertainment\만화\[미나모토 아키라] 여왕 폐하의 이세계 전략")
    #folderSearch(rootfolder="E:\Entertainment\만화\[미나모토 아키라] 여왕 폐하의 이세계 전략")
