# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'copyVeUXnF.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_maincopy(object):
    def setupUi(self, maincopy):
        if not maincopy.objectName():
            maincopy.setObjectName(u"maincopy")
        maincopy.resize(422, 221)
        self.centralwidget = QWidget(maincopy)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.copyn = QPushButton(self.centralwidget)
        self.copyn.setObjectName(u"copyn")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.copyn.setFont(font)

        self.verticalLayout.addWidget(self.copyn)

        self.showtimea = QPushButton(self.centralwidget)
        self.showtimea.setObjectName(u"showtimea")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.showtimea.setFont(font1)

        self.verticalLayout.addWidget(self.showtimea)

        self.pastelabel = QLabel(self.centralwidget)
        self.pastelabel.setObjectName(u"pastelabel")
        font2 = QFont()
        font2.setPointSize(13)
        self.pastelabel.setFont(font2)
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
        self.menubar.setGeometry(QRect(0, 0, 422, 22))
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

