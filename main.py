import os
import re
import shutil
import sys
import folderSearch

from PyQt5 import uic
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
                             QTextEdit, QMessageBox)

form_class = uic.loadUiType("pyqtUI.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.findButton.clicked.connect(self.findButtonClick)
        self.searchButton.clicked.connect(self.searchButtonClick)
        self.clearButton.clicked.connect(self.clearButtonClick)
        self.mergeButton.clicked.connect(self.mergeButtonClick)
    def findButtonClick(self):
        print("findButtonClick 클릭됨.")
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        print(fname)
        self.targetFolderAddress.setText(fname)
        self.saveFolderAddress.setText(fname+"/Result")

    def searchButtonClick(self):
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.saveFolderAddress.setText(fname)
        pass

    def clearButtonClick(self):
        self.saveFolderAddress.setText("")
    def mergeButtonClick(self):
        folderSearch.count = 0
        rootAddress = self.targetFolderAddress.toPlainText()
        saveAddress = self.saveFolderAddress.toPlainText()

        if rootAddress == "":
            print("Empty address")
            QMessageBox.question(self, 'Alert', 'Target folder를 찾아주세요.', QMessageBox.Yes, QMessageBox.NoButton)
            return
    
        if "Result" not in os.listdir(rootAddress):
            os.mkdir(rootAddress+"/"+"Result")
        else:
            pass #good
        
        print("rootAddress:", rootAddress)
        print("saveAddress:",saveAddress)
        folderSearch.merge(rootAddress,saveAddress)
        

        QMessageBox.about(self, 'Process Complete', '작업 완료 했습니다.')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

    #folderSearch.folderSearch(rootfolder="E:\Entertainment\만화\[미나모토 아키라] 여왕 폐하의 이세계 전략")
    #folderSearch(rootfolder="E:\Entertainment\만화\[미나모토 아키라] 여왕 폐하의 이세계 전략")
