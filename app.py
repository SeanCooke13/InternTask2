# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Task2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from gen.ui_app import Ui_MainWindow

class Prime_Factorizer(object):
    def __init__(self):
        super(Prime_Factorizer, self).__init__()
        self.ui = Ui_MainWindow
        self.ui.setupUi(self, MainWindow)
        self.go_button.clicked.connect(self.receive_input)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Please insert any number you would like to see the prime factorizaton of!</span></p></body></html>", None))
        self.unser_input.setText("")
        self.go_button.setText(QCoreApplication.translate("MainWindow", u"Go!", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"  Prime Factorization :", None))
        self.prime_factors.setText("")
    def receive_input(self):
        self.prime_factors.setText(self.unser_input.text())
    


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Prime_Factorizer()
    MainWindow.show()
    sys.exit(app.exec_())
