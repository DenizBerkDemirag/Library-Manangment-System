# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 450)
        Form.setMinimumSize(QtCore.QSize(400, 400))
        Form.setStyleSheet(Style.style_sheet)

        self.verticalLayout_main = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        
        # Center Container
        self.verticalLayout_center = QtWidgets.QVBoxLayout()
        self.verticalLayout_center.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_center.setContentsMargins(40, 40, 40, 40)
        
        # Login GroupBox
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(320, 320))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.verticalLayout_box = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_box.setSpacing(20)
        self.verticalLayout_box.setContentsMargins(30, 40, 30, 40)
        
        # Title
        self.label_title = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("Hoş Geldiniz")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_box.addWidget(self.label_title)
        
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_box.addItem(spacerItem)

        # Username Field
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("Kullanıcı Adı")
        self.verticalLayout_box.addWidget(self.label)
        
        self.lineEdit_ogrenci_id = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ogrenci_id.setMinimumHeight(35)
        self.lineEdit_ogrenci_id.setPlaceholderText("Kullanıcı adınızı giriniz")
        self.lineEdit_ogrenci_id.setObjectName("lineEdit_ogrenci_id")
        self.verticalLayout_box.addWidget(self.lineEdit_ogrenci_id)

        # Password Field
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setText("Şifre")
        self.verticalLayout_box.addWidget(self.label_2)
        
        self.lineEdit_ogrenci_sifre = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ogrenci_sifre.setMinimumHeight(35)
        self.lineEdit_ogrenci_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_ogrenci_sifre.setPlaceholderText("Şifrenizi giriniz")
        self.lineEdit_ogrenci_sifre.setObjectName("lineEdit_ogrenci_sifre")
        self.verticalLayout_box.addWidget(self.lineEdit_ogrenci_sifre)

        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_box.addItem(spacerItem2)

        # Buttons
        self.horizontalLayout_btns = QtWidgets.QHBoxLayout()
        self.horizontalLayout_btns.setSpacing(15)
        
        self.pushButton_ogrenci_giris = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ogrenci_giris.setMinimumHeight(40)
        self.pushButton_ogrenci_giris.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_ogrenci_giris.setObjectName("pushButton_ogrenci_giris")
        self.horizontalLayout_btns.addWidget(self.pushButton_ogrenci_giris)
        
        self.pushButton_cikis = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cikis.setMinimumHeight(40)
        self.pushButton_cikis.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cikis.setObjectName("pushButton_cikis")
        self.horizontalLayout_btns.addWidget(self.pushButton_cikis)
        
        self.verticalLayout_box.addLayout(self.horizontalLayout_btns)
        
        self.verticalLayout_center.addWidget(self.groupBox)
        self.verticalLayout_main.addLayout(self.verticalLayout_center)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kullanıcı Girişi"))
        self.label_title.setText(_translate("Form", "Hoş Geldiniz"))
        self.label.setText(_translate("Form", "Kullanıcı Adı"))
        self.label_2.setText(_translate("Form", "Şifre"))
        self.pushButton_ogrenci_giris.setText(_translate("Form", "Giriş Yap"))
        self.pushButton_cikis.setText(_translate("Form", "Çıkış"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
