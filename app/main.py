import sys
import setUp
import File
from PyQt5.QtCore import  pyqtSlot ,Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QWidget, QLabel, QInputDialog, QLineEdit, QFileDialog,QPushButton,
QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox)


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
        layout.setColumnStretch(1, 2)   
        layout.setColumnStretch(1, 2)   

     

        buttonBlue = QPushButton('Load Image', self)
        buttonBlue.clicked.connect(self.on_click)
        buttonBlue.setStyleSheet("padding: 43px;background-color: blue;")
        layout.addWidget(buttonBlue,0,0)

        
        
        labelOr = QLabel(self)
        pixmap = QPixmap(setUp.PATH)
        labelOr.setPixmap(pixmap)
        labelOr.setMinimumSize(1,1)
        pixmap.scaled(20, 20)
        labelOr.setStyleSheet("margin-left: 150px;margin-top: 20px");
        labelOr.setAlignment(Qt.AlignCenter)
        layout.addWidget(labelOr,0,1)


        labelS = QLabel(self)
        pixmap = QPixmap(setUp.PATH)
        labelS.setPixmap(pixmap)
        labelS.setMinimumSize(1,1)
        labelS.setStyleSheet("margin-left: 150px;margin-top: 20px")
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

        ex = File.File()
        
        try:

            if ex.fileName:

                fileName = ex.fileName
                print(fileName)
                return fileName

        except AttributeError:
            print("please select a file")



    @pyqtSlot()

    def clicked(self):
        print("run App !!!!!!!!!")


        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())