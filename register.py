from sys import argv, exit
from otherArchives.registerScreen import Window
from PyQt5.QtWidgets import QMainWindow, QApplication
app = QApplication(argv)
window = Window()
window.show()
exit(app.exec_())
