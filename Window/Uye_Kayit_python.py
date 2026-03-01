# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 450)
        Form.setMinimumSize(QtCore.QSize(350, 400))
        Form.setStyleSheet(Style.style_sheet)
        
        self.verticalLayout_form = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_form.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_form.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_form.setObjectName("verticalLayout_form")
        
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 350))
        self.groupBox.setMaximumSize(QtCore.QSize(350, 400))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(30, 40, 30, 40)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label_title = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("Üye Kayıt")
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        
        self.lineEdit_ogrenci_id = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ogrenci_id.setMinimumHeight(40)
        self.lineEdit_ogrenci_id.setPlaceholderText("Kullanıcı Adı")
        self.lineEdit_ogrenci_id.setObjectName("lineEdit_ogrenci_id")
        self.verticalLayout.addWidget(self.lineEdit_ogrenci_id)
        
        self.lineEdit_ogrenci_sifre = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ogrenci_sifre.setMinimumHeight(40)
        self.lineEdit_ogrenci_sifre.setPlaceholderText("Şifre")
        self.lineEdit_ogrenci_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_ogrenci_sifre.setObjectName("lineEdit_ogrenci_sifre")
        self.verticalLayout.addWidget(self.lineEdit_ogrenci_sifre)
        
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        
        self.pushButton_ogrenci_giris = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ogrenci_giris.setMinimumHeight(45)
        self.pushButton_ogrenci_giris.setStyleSheet("background-color: #3498db; font-weight: bold; font-size: 16px;")
        self.pushButton_ogrenci_giris.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_ogrenci_giris.setObjectName("pushButton_ogrenci_giris")
        self.verticalLayout.addWidget(self.pushButton_ogrenci_giris)
        
        self.commandLinkButton = QtWidgets.QPushButton(self.groupBox)
        self.commandLinkButton.setFlat(True)
        self.commandLinkButton.setStyleSheet("color: #3498db; font-weight: bold; background: transparent;")
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        
        self.verticalLayout_form.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Üye Kayıt"))
        self.pushButton_ogrenci_giris.setText(_translate("Form", "Kayıt Ol"))
        self.commandLinkButton.setText(_translate("Form", "Giriş Ekranına Dön"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
