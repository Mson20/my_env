from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)


        self.label1 = QLabel("Enter your IP:", self)
        self.text1 = QLineEdit(self)
        self.text1.move(10, 60)
        self.label1.move(10,40)


        self.label2 = QLabel("Enter your API Key:", self)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 120)
        self.label2.move(10,100)

        self.label3 = QLabel("Enter the hosname:", self)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 180)
        self.label3.move(10,160)

        self.button = QPushButton("Send:", self)
        self.button.move(150, 300)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()

        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname)
            if res:
                self.label2.setText("Answer%s" % (res))
                self.label2.adjustSize()
                self.show()

    def __query(self, hostname,api_key,ip):
        url = "http://%s" % (hostname,api_key,ip)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
    