from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from win32api import GetSystemMetrics
from math import floor
from otherArchives.conexaoBd import ConnectionClass

monitorSizes = [GetSystemMetrics(0), GetSystemMetrics(1)]

class Window (QMainWindow):
    idText = ""
    dbObject = ConnectionClass()
    receiptText = ""
    productsNames = []
    productsPrices = []
    totalPrice = 0.00
    def __init__(self):
        super(Window, self).__init__()
        self.setStyleSheet("QMainWindow{background-color:rgb(0,0,100)} QScrollBar{background-color: green; border-radius: 10px; color:yellow}")
        #section of the screen that will show all the products bought (also works as a preview of the receipt), will be updated after every new product inserted
        global scannedProducts
        scannedProducts = QTextEdit(self)
        scannedProducts.verticalScrollBar().setEnabled(True)
        scannedProducts.horizontalScrollBar().setEnabled(False)
        scannedProducts.setGeometry(0,0,floor((monitorSizes[0]/1.7)),floor(monitorSizes[1]/1.2))
        scannedProducts.setText(self.receiptText)
        scannedProducts.setReadOnly(True)
        scannedProducts.setStyleSheet("QTextEdit{background-color:rgb(100,100,100); color:yellow; font-size:20px; line-height:50px}")
        #inserted code of the product
        global insertedId
        insertedId = QLineEdit(self)
        insertedId.setGeometry(floor((monitorSizes[0]/1.45)), floor((monitorSizes[1]/4.5)), 300, 120)
        insertedId.setStyleSheet("QLineEdit{background-color:rgb(100,100,100); color:yellow; font-size:100px; font-family:Impact; border-style:solid; border-width:1px; border-color: white;}")
        insertedId.setAlignment(Qt.AlignCenter)
        insertedId.setText(self.idText)
        insertedId.setReadOnly(True)
        #label that will show the total price of the purchase, will be updated after every new product inserted
        global totalPriceLabel
        totalPriceLabel = QLabel(self)
        totalPriceLabel.setGeometry(10, floor((monitorSizes[1]/1.2)), (scannedProducts.width() - 10), 80)
        totalPriceLabel.setText(str("Total Price: R$0,00"))
        totalPriceLabel.setStyleSheet("QLabel{color: yellow; font-size:60px; font-family:'Franklin Gothic Medium'}")
        #button that will finish the purchase and generate the receipt as a image
        finishButton = QPushButton(self)
        finishButton.setGeometry(floor(monitorSizes[0]/1.45), floor(monitorSizes[1]/2), 300, 120)
        finishButton.setText("Finish Purchase")
        finishButton.setStyleSheet("QPushButton{background-color: rgb(100, 100, 100); color:yellow; font-size:40px; font-family:'Gill Sans'; border-style:solid; border-width:1px; border-color: white; border-radius:10px;} QPushButton:pressed{background-color:rgb(50,50,50); border-color: rgb(150,150,150)}")
        #finishButton.clicked.connect()
        #button that will close the application
        closeButton = QPushButton(self)
        closeButton.setGeometry(floor(monitorSizes[0]/1.046), 0, 60, 60)
        closeButton.setText("X")
        closeButton.setStyleSheet("QPushButton{background-color:red; color:black; font-family:Arial; font-size:50px;} QPushButton:pressed{background-color:rgb(150,0,0);}")
        def closeApplication():
            closeButton.move(floor(monitorSizes[0]/1.046),10)
            exit()
        closeButton.clicked.connect(closeApplication) 
        self.showFullScreen()

    #update the inserted id inside of the QTextEdit. If the string already has 4 characters, it will erase the first one so newest number can be inserted.
    def updateId(self, newNumber):
        if(len(self.idText) == 4):self.idText = self.idText[1:]
        self.idText = self.idText + newNumber
        insertedId.setText(self.idText)
    #search for the product on the database
    def searchForItem(self):
        requestedProduct = self.dbObject.searchById(self.idText)
        if(requestedProduct != None): 
            self.productsNames.append(requestedProduct[1])
            self.productsPrices.append(requestedProduct[2])
            self.receiptText = self.receiptText + "\n" + str(self.productsNames[-1]) + " - R$" + str(self.productsPrices[-1])
            self.totalPrice = self.totalPrice + float(self.productsPrices[-1])
            scannedProducts.setText(self.receiptText)
            totalPriceLabel.setText("Total Price: R$" + str(self.totalPrice).replace(".", ","))
    #erase last character in string
    def eraseLast(self):
        self.idText = self.idText[:len(self.idText)-1]
        insertedId.setText(self.idText)
    #reset everything for the next purchase
    def reset(self):
        self.idText = ""
        self.receiptText = ""
        self.productsNames = []
        self.productsPrices = []
        self.totalPrice = 0.00
        insertedId.setText(self.idText)
        scannedProducts.setText(self.receiptText)
        totalPriceLabel.setText("Total Price: R$0,00")
    #keyboard actions
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1: self.updateId("1")
        elif event.key() == Qt.Key_2: self.updateId("2")
        elif event.key() == Qt.Key_3: self.updateId("3")
        elif event.key() == Qt.Key_4: self.updateId("4")
        elif event.key() == Qt.Key_5: self.updateId("5")
        elif event.key() == Qt.Key_6: self.updateId("6")
        elif event.key() == Qt.Key_7: self.updateId("7")
        elif event.key() == Qt.Key_8: self.updateId("8")
        elif event.key() == Qt.Key_9: self.updateId("9")
        elif event.key() == Qt.Key_0: self.updateId("0")
        elif event.key() == Qt.Key_Return: self.searchForItem()
        elif event.key() == Qt.Key_Backspace: self.eraseLast()
        elif event.key() == Qt.Key_End:
            print('s')
        elif event.key() == Qt.Key_R: self.reset()
