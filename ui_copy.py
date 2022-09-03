# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'copy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_maincopy(object):
    def setupUi(self, maincopy):
        if not maincopy.objectName():
            maincopy.setObjectName(u"maincopy")
        maincopy.resize(697, 364)
        self.centralwidget = QWidget(maincopy)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.copyn = QPushButton(self.centralwidget)
        self.copyn.setObjectName(u"copyn")

        self.verticalLayout.addWidget(self.copyn)

        self.showtimea = QPushButton(self.centralwidget)
        self.showtimea.setObjectName(u"showtimea")

        self.verticalLayout.addWidget(self.showtimea)

        self.pastelabel = QLabel(self.centralwidget)
        self.pastelabel.setObjectName(u"pastelabel")
        font = QFont()
        font.setPointSize(12)
        self.pastelabel.setFont(font)
        self.pastelabel.setAlignment(Qt.AlignCenter)
        self.pastelabel.setWordWrap(False)

        self.verticalLayout.addWidget(self.pastelabel)

        self.getcopy = QPlainTextEdit(self.centralwidget)
        self.getcopy.setObjectName(u"getcopy")
        self.getcopy.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout.addWidget(self.getcopy)

        maincopy.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(maincopy)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 697, 21))
        maincopy.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(maincopy)
        self.statusbar.setObjectName(u"statusbar")
        maincopy.setStatusBar(self.statusbar)

        self.retranslateUi(maincopy)

        QMetaObject.connectSlotsByName(maincopy)
    # setupUi

    def retranslateUi(self, maincopy):
        maincopy.setWindowTitle(QCoreApplication.translate("maincopy", u"\u590d\u5236", None))
        self.copyn.setText(QCoreApplication.translate("maincopy", u"\u590d\u5236", None))
        self.showtimea.setText(QCoreApplication.translate("maincopy", u"\u663e\u793a\u65f6\u95f4", None))
        self.pastelabel.setText(QCoreApplication.translate("maincopy", u"\u7c98\u8d34\u677f\u5185\u5bb9", None))
    # retranslateUi

