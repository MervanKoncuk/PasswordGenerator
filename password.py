# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PassWordGenerator(object):
    def setupUi(self, PassWordGenerator):
        PassWordGenerator.setObjectName("PassWordGenerator")
        PassWordGenerator.setWindowModality(QtCore.Qt.NonModal)
        PassWordGenerator.resize(675, 564)
        PassWordGenerator.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        PassWordGenerator.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PassWordGenerator.setWindowIcon(icon)
        PassWordGenerator.setWindowOpacity(1.0)
        PassWordGenerator.setToolTip("")
        PassWordGenerator.setAutoFillBackground(False)
        PassWordGenerator.setStyleSheet("")
        PassWordGenerator.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(PassWordGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_olustur = QtWidgets.QPushButton(self.centralwidget)
        self.btn_olustur.setGeometry(QtCore.QRect(10, 230, 151, 41))
        self.btn_olustur.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_olustur.setObjectName("btn_olustur")
        self.btn_yaz = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yaz.setGeometry(QtCore.QRect(490, 30, 131, 41))
        self.btn_yaz.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);")
        self.btn_yaz.setObjectName("btn_yaz")
        self.list_yaz = QtWidgets.QListWidget(self.centralwidget)
        self.list_yaz.setGeometry(QtCore.QRect(290, 30, 181, 481))
        self.list_yaz.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"")
        self.list_yaz.setObjectName("list_yaz")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 251, 155))
        self.layoutWidget.setStyleSheet("")
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.txt_hesap = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_hesap.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_hesap.setObjectName("txt_hesap")
        self.verticalLayout.addWidget(self.txt_hesap)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txt_email = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_email.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_email.setObjectName("txt_email")
        self.verticalLayout.addWidget(self.txt_email)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txt_sifre = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_sifre.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_sifre.setObjectName("txt_sifre")
        self.verticalLayout.addWidget(self.txt_sifre)
        self.uzunluk = QtWidgets.QSpinBox(self.centralwidget)
        self.uzunluk.setGeometry(QtCore.QRect(190, 230, 51, 41))
        self.uzunluk.setObjectName("uzunluk")
        PassWordGenerator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PassWordGenerator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 21))
        self.menubar.setObjectName("menubar")
        PassWordGenerator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PassWordGenerator)
        self.statusbar.setObjectName("statusbar")
        PassWordGenerator.setStatusBar(self.statusbar)

        self.retranslateUi(PassWordGenerator)
        QtCore.QMetaObject.connectSlotsByName(PassWordGenerator)

    def retranslateUi(self, PassWordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PassWordGenerator.setWindowTitle(_translate("PassWordGenerator", "PassWordsOfDsm"))
        self.btn_olustur.setText(_translate("PassWordGenerator", "Oluştur"))
        self.btn_yaz.setText(_translate("PassWordGenerator", "Yazdır"))
        self.label_3.setText(_translate("PassWordGenerator", "Hesap "))
        self.label.setText(_translate("PassWordGenerator", "Email"))
        self.label_2.setText(_translate("PassWordGenerator", "Şifre"))
