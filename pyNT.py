#!usr/bin/python3
#! -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
 
import Ui_pyencode
import hashlib
import binascii


app = QApplication(sys.argv)
MainWindow = QMainWindow() 
ui = Ui_pyencode.Ui_MainWindow()
ui.setupUi(MainWindow)


def NTML():
    str1 = ui.lineEdit.text()
    NTML_hash = hashlib.new('md4')
    NTML_hash.update(str1.encode('utf-16le'))
    res = str(binascii.hexlify(NTML_hash.digest()),encoding="utf-8")
    ui.textBrowser.setText(res)

def main():

    ui.pushButton_3.clicked.connect(lambda:NTML())
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    