# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 350)
        Form.setStyleSheet(Style.style_sheet)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout.setSpacing(15)

        self.label_title = QtWidgets.QLabel(Form)
        font_title = QtGui.QFont()
        font_title.setPointSize(16)
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(12)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight)

        self.label_kitap_id = QtWidgets.QLabel(Form)
        self.label_kitap_id.setObjectName("label_kitap_id")
        self.lineEdit_kitap_id = QtWidgets.QLineEdit(Form)
        self.lineEdit_kitap_id.setMinimumHeight(30)
        self.lineEdit_kitap_id.setPlaceholderText("Kitap ID giriniz")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_kitap_id)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_kitap_id)

        self.label_kullanici_id = QtWidgets.QLabel(Form)
        self.label_kullanici_id.setObjectName("label_kullanici_id")
        self.lineEdit_kullanici_id = QtWidgets.QLineEdit(Form)
        self.lineEdit_kullanici_id.setMinimumHeight(30)
        self.lineEdit_kullanici_id.setPlaceholderText("Kullanıcı ID giriniz")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_kullanici_id)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_kullanici_id)

        self.label_tarih = QtWidgets.QLabel(Form)
        self.label_tarih.setObjectName("label_tarih")
        self.dateEdit_tarih = QtWidgets.QDateEdit(Form)
        self.dateEdit_tarih.setMinimumHeight(30)
        self.dateEdit_tarih.setDate(QtCore.QDate.currentDate())
        self.dateEdit_tarih.setCalendarPopup(True)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_tarih)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit_tarih)

        self.label_adres = QtWidgets.QLabel(Form)
        self.label_adres.setObjectName("label_adres")
        self.textEdit_adres = QtWidgets.QTextEdit(Form)
        self.textEdit_adres.setMaximumHeight(80)
        self.textEdit_adres.setPlaceholderText("Teslimat adresi...")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_adres)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_adres)

        self.verticalLayout.addLayout(self.formLayout)

        self.pushButton_onayla = QtWidgets.QPushButton(Form)
        self.pushButton_onayla.setMinimumHeight(40)
        self.pushButton_onayla.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_onayla.setObjectName("pushButton_onayla")
        self.verticalLayout.addWidget(self.pushButton_onayla)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _t = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_t("Form", "Sipariş Ver"))
        self.label_title.setText(_t("Form", "Yeni Sipariş Oluştur"))
        self.label_kitap_id.setText(_t("Form", "Kitap ID:"))
        self.label_kullanici_id.setText(_t("Form", "Kullanıcı ID:"))
        self.label_tarih.setText(_t("Form", "İade Tarihi:"))
        self.label_adres.setText(_t("Form", "Teslimat Adresi:"))
        self.pushButton_onayla.setText(_t("Form", "Siparişi Onayla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
