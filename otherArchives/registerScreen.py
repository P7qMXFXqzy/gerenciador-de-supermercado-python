from PyQt5.QtWidgets import QMainWindow, QTextEdit, QLabel, QLineEdit
from win32api import GetSystemMetrics
from math import floor

monitorSizes = [GetSystemMetrics(0), GetSystemMetrics(1)]

class Window (QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setStyleSheet("QMainWindow{background-color:rgb(0,0,100)} QScrollBar{background-color: green; border-radius: 10px; color:yellow}")
        receipt = QLabel(self)
        text = ""
        for x in range(100):
            text = text + '\n' + str(x)
            receipt.setText(text)
        #section of the screen that will show all the products bought (also works as a preview of the receipt)
        scannedProducts = QTextEdit(self)
        scannedProducts.verticalScrollBar().setEnabled(True)
        scannedProducts.horizontalScrollBar().setEnabled(False)
        scannedProducts.setGeometry(0,0,floor((monitorSizes[0]/1.7)),monitorSizes[1])
        scannedProducts.setText(text)
        scannedProducts.setReadOnly(True)
        scannedProducts.setStyleSheet("QTextEdit{background-color:rgb(100,100,100); color:yellow; font-size:15px; line-height:50px}")
        #inserted code of the product
        idInserido = QLineEdit(self)
        idInserido.setGeometry(floor((monitorSizes[0]/1.45)), floor((monitorSizes[1]/4.5)), 300, 120)
        idInserido.setStyleSheet("QLineEdit{background-color:rgb(100,100,100); color:yellow; font-size:50px;}")
        self.showFullScreen()
        
