import os
import re
import shutil
import sys
import folderSearch

from PyQt5 import uic
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
                             QTextEdit, QMessageBox,QListView,QTreeView,QFileSystemModel,QAbstractItemView)

dirname = os.getcwd().split('\\')[-1]

print("dirname", dirname )