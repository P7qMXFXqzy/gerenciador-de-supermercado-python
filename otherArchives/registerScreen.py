from PyQt5.QtWidgets import QMainWindow, QTextEdit, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
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
        #section of the screen that will show all the products bought (also works as a preview of the receipt), will be updated after every new product inserted
        scannedProducts = QTextEdit(self)
        scannedProducts.verticalScrollBar().setEnabled(True)
        scannedProducts.horizontalScrollBar().setEnabled(False)
        scannedProducts.setGeometry(0,0,floor((monitorSizes[0]/1.7)),floor(monitorSizes[1]/1.2))
        scannedProducts.setText(text)
        scannedProducts.setReadOnly(True)
        scannedProducts.setStyleSheet("QTextEdit{background-color:rgb(100,100,100); color:yellow; font-size:15px; line-height:50px}")
        #inserted code of the product
        insertedId = QLineEdit(self)
        insertedId.setGeometry(floor((monitorSizes[0]/1.45)), floor((monitorSizes[1]/4.5)), 300, 120)
        insertedId.setStyleSheet("QLineEdit{background-color:rgb(100,100,100); color:yellow; font-size:100px; font-family:Impact;}")
        insertedId.setAlignment(Qt.AlignCenter)
        insertedId.setText("1432")
        insertedId.setReadOnly(True)
        #label that will show the total price of the purchase, will be updated after every new product inserted
        totalPriceLabel = QLabel(self)
        totalPriceLabel.setGeometry(10, floor((monitorSizes[1]/1.2)), (scannedProducts.width() - 10), 80)
        totalPriceLabel.setText("Valor total: R$0000,00")
        totalPriceLabel.setStyleSheet("QLabel{color: yellow; font-size:60px; font-family:'Franklin Gothic Medium'}")
        #button that will finish the purchase and generate the receipt as a image
        finishButton = QPushButton(self)
        finishButton.setGeometry(floor(monitorSizes[0]/1.45), floor(monitorSizes[1]/2), 300, 120)
        finishButton.setText("Finish Purchase")
        finishButton.setStyleSheet("QPushButton{background-color: rgb(100, 100, 100); color:yellow; font-size:40px; font-family:'Gill Sans'; border:3px; border-color: white; border-radius:10px;}")
        finishButton.clicked.connect(printar)
        self.showFullScreen()
    
