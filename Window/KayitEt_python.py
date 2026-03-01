# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setMinimumSize(QtCore.QSize(350, 450))
        Form.setStyleSheet(Style.style_sheet)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("Yeni Kitap Kaydı")
        self.groupBox.setObjectName("groupBox")
        
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setContentsMargins(20, 30, 20, 30)
        self.formLayout.setSpacing(15)
        self.formLayout.setObjectName("formLayout")
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        
        self.lineEdit_kitap_ad = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_kitap_ad.setPlaceholderText("Kitap Adı")
        self.lineEdit_kitap_ad.setObjectName("lineEdit_kitap_ad")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_kitap_ad)
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        
        self.lineEdit_kategori_ad = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_kategori_ad.setPlaceholderText("Kategori")
        self.lineEdit_kategori_ad.setObjectName("lineEdit_kategori_ad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_kategori_ad)
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        
        self.lineEdit_yazar = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_yazar.setPlaceholderText("Yazar")
        self.lineEdit_yazar.setObjectName("lineEdit_yazar")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_yazar)
        
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        
        self.lineEdit_yayinlanma = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_yayinlanma.setPlaceholderText("Yayınlanma Tarihi (YYYY)")
        self.lineEdit_yayinlanma.setObjectName("lineEdit_yayinlanma")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_yayinlanma)
        
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        
        self.lineEdit_stok = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_stok.setPlaceholderText("Stok Adedi")
        self.lineEdit_stok.setObjectName("lineEdit_stok")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_stok)
        
        self.pushButton_kayit_et = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_kayit_et.setMinimumHeight(40)
        self.pushButton_kayit_et.setStyleSheet("background-color: #27ae60; font-weight: bold;")
        self.pushButton_kayit_et.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_kayit_et.setObjectName("pushButton_kayit_et")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.pushButton_kayit_et)
        
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kitap Ekle"))
        self.label.setText(_translate("Form", "Kitap Adı:"))
        self.label_2.setText(_translate("Form", "Kategori:"))
        self.label_3.setText(_translate("Form", "Yazar:"))
        self.label_4.setText(_translate("Form", "Yıl:"))
        self.label_5.setText(_translate("Form", "Stok:"))
        self.pushButton_kayit_et.setText(_translate("Form", "Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
