from PyQt5 import  QtWidgets
from PyQt5.QtGui import  QFont

fontTitle = QFont('Arial',24)
fontText = QFont('Times',14)

class Help(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Haqqimizda')
        self.setGeometry(200,250,450,250)
        self.UI()
    
    def UI(self):
        vbox = QtWidgets.QVBoxLayout()
        ################################################################
        textTitle = QtWidgets.QLabel('Haqqimizda')
        textHaqqimizda = QtWidgets.QLabel('Bu seyfe haqqimizda seyfesidir')
        ################################################################
        textTitle.setFont(fontTitle)
        textHaqqimizda.setFont(fontText)
        ################################################################
        vbox.addWidget(textTitle)
        vbox.addWidget(textHaqqimizda)
        ################################################################
        self.setLayout(vbox)
        