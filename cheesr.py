import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

class Vpn(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cheesr VPN")
        self.setWindowIcon(QIcon("source/icons/cheese.png"))

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cheesr Browser")
        self.setWindowIcon(QIcon("source/icons/cheese.png"))
        self.setGeometry(200,200, 900,600)


        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("source/icons/home.svg"))
        self.homeButton.setIconSize(QSize(36,36))
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)
        
        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("source/icons/back.png"))
        self.backButton.setIconSize(QSize(36,36))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("source/icons/cheese.png"))
        self.reloadButton.setIconSize(QSize(36,36))
        self.reloadButton.clicked.connect(self.reloadBtn) 
        toolbar.addWidget(self.reloadButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("source/icons/forward.png"))
        self.forwardButton.setIconSize(QSize(36,36))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Comic Sans MS", 18))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolbar.addWidget(self.addressLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("source/icons/search.png"))
        self.searchButton.setIconSize(QSize(36,36))
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'google.com'
        
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))

    def searchBtn(self):
        myurl = self.addressLineEdit.text()
        self.webEngineView.load(QUrl(myurl))

    def backBtn(self):
        self.webEngineView.back()

    def forwardBtn(self):
        self.webEngineView.forward()

    def reloadBtn(self):
        self.webEngineView.reload()

    def homeBtn(self):
        self.webEngineView.load(Qurl('google.com'))
        
        


app = QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec_())

    
