import sys
import setUp
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
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.openFileNameDialog()
        self.openFileNamesDialog()
        self.saveFileDialog()
        
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            setUp.FileName = fileName
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
    
    def saveFileDialog(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
           setUp.FileName = fileName
            




class App(QWidget):


    def __init__(self):
        super().__init__()
        self.title = 'Data loader'
        self.left = 10
        self.top = 10
        self.width = 900
        self.height = 600
        self.setStyleSheet("QWidget{background-color: white;}")
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        
        self.show()
    
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Data Builder")
        layout = QGridLayout()
        layout.setColumnStretch(2, 2)   
        layout.setColumnStretch(2, 2)   
        

        buttonBlue = QPushButton('Load Image', self)
        buttonBlue.clicked.connect(self.on_click)
        buttonBlue.setStyleSheet("padding: 43px;background-color: blue;")
        layout.addWidget(buttonBlue,0,0)

        if setUp.FileName != "":

            labelOr = QLabel(self)
            pixmap = QPixmap(setUp.FileName)
            print(setUp.FileName)
            labelOr.setPixmap(pixmap)
            labelOr.setMinimumSize(1,1)
            labelOr.setStyleSheet("margin-left: 150px;margin-top: 20px");
            labelOr.setAlignment(Qt.AlignCenter)
            layout.addWidget(labelOr,0,1)


        labelS = QLabel(self)
        pixmap = QPixmap('/home/masoud/Desktop/sub.jpg')
        labelS.setPixmap(pixmap)
        labelS.setMinimumSize(1,1)
        labelS.setStyleSheet("margin-left: 150px;margin-top: 20px;")
        labelS.setAlignment(Qt.AlignCenter)
        layout.addWidget(labelS,1,1)



        buttonRed = QPushButton('Predict', self)
        buttonRed.clicked.connect(self.clicked)
        buttonRed.setStyleSheet("padding: 43px;background-color:blue;")
        layout.addWidget(buttonRed,2,0)

       
        textbox = QLabel(self)
        textbox.move(20, 120)
        textbox.setText("OutPut")
        textbox.resize(380,60)
        textbox.setAlignment(Qt.AlignCenter)
        textbox.setStyleSheet("QLabel { background-color : gray; color : black; } ")
        layout.addWidget(textbox,2,1)
        
        self.horizontalGroupBox.setLayout(layout)




    @pyqtSlot()
    def on_click(self):

        app = QApplication(sys.argv)
        ex = File()
        sys.stderr(app.exec_())


    @pyqtSlot()

    def clicked(self):
        print("run App !!!!!!!!!")


        





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())