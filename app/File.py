import sys
from PyQt5.QtCore import  pyqtSlot ,Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QWidget, QLabel, QInputDialog, QLineEdit, QFileDialog,QPushButton,
QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox)


class File(QWidget):


    def __init__(self):
        super().__init__()
        self.title = 'Select a file:'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 480
        self.openFileNameDialog()
    

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        self.openFileNameDialog()

        
        self.show()
    
    def openFileNameDialog(self):
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
           self.fileName = fileName


