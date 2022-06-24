import os
import re
import shutil
import sys
import folderSearch

from PyQt5 import uic
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
                             QTextEdit, QMessageBox,QListView,QTreeView,QFileSystemModel,QAbstractItemView)

address = "E:\\Entertainment\\만화\\[미나모토 아키라] 여왕 폐하의 이세계 전략"

dirList = address.split("\\")

for e in dirList:
    print(e)

address = "/".join(dirList[0:-1])
print(address)