#jojo os kernel v0.2 
input2 = input (password:)
if is not (input2 == 1889): exit
if (input2 == 1889):
open("banner.sh")
print("hello user this is anonymously os")
print("jojo os version: gold experience")
print("versione kernel: 0.1")
print("state: root")
input1 = input ("chose a fictures:1.hacking,2.music,3.internet,4.update")
if (input1 == '1'):
    print("[1]attacco bizzarro")
    input3 = input ("~>"):
        if (input3 == '1'):
            open("hack.sh")
if (input1 == '3'):
    import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())
app = QApplication(sys.argv)
QApplication.setApplicationName('Safe Browser')
window = MainWindow()
app.exec_().
if (input1 == '4'):
    apt update wireshark
    apt upgrade wireshark
    apt update aircrack-ng
    apt upgrade aircrack-ng
    apt update sqlmap
    apt upgrade sqlmap 
    apt update nmap 
    apt upgrade nmap 
    apt update commix 
    apt upgrade commix
    print("finish updating all of pakets!")
    print("resrart the kernel!")