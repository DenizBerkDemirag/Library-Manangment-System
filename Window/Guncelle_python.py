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
        self.groupBox.setTitle("Kitap Bilgilerini Güncelle")
        self.groupBox.setObjectName("groupBox")
        
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setContentsMargins(20, 30, 20, 30)
        self.formLayout.setSpacing(15)
        self.formLayout.setObjectName("formLayout")
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        
        self.lineEdit_guncelle_id = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_guncelle_id.setPlaceholderText("ID")
        self.lineEdit_guncelle_id.setObjectName("lineEdit_guncelle_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_guncelle_id)
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        
        self.lineEdit_guncelle_kitao_ad = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_guncelle_kitao_ad.setPlaceholderText("Kitap Adı")
        self.lineEdit_guncelle_kitao_ad.setObjectName("lineEdit_guncelle_kitao_ad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_guncelle_kitao_ad)
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        
        self.lineEdit_guncelle_kategori_ad = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_guncelle_kategori_ad.setPlaceholderText("Kategori")
        self.lineEdit_guncelle_kategori_ad.setObjectName("lineEdit_guncelle_kategori_ad")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_guncelle_kategori_ad)
        
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        
        self.lineEdit_guncelle_yazar_ad = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_guncelle_yazar_ad.setPlaceholderText("Yazar")
        self.lineEdit_guncelle_yazar_ad.setObjectName("lineEdit_guncelle_yazar_ad")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_guncelle_yazar_ad)
        
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        
        self.lineEdit_guncelle_yayinlanma = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_guncelle_yayinlanma.setPlaceholderText("Yayınlanma Tarihi (YYYY)")
        self.lineEdit_guncelle_yayinlanma.setObjectName("lineEdit_guncelle_yayinlanma")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_guncelle_yayinlanma)
        
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        
        self.lineEdit_guncelle_stok = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_guncelle_stok.setPlaceholderText("Stok Adedi")
        self.lineEdit_guncelle_stok.setObjectName("lineEdit_guncelle_stok")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_guncelle_stok)
        
        self.pushButton_guncelle = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_guncelle.setMinimumHeight(40)
        self.pushButton_guncelle.setStyleSheet("background-color: #f39c12; font-weight: bold;")
        self.pushButton_guncelle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_guncelle.setObjectName("pushButton_guncelle")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.pushButton_guncelle)
        
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kitap Güncelle"))
        self.label.setText(_translate("Form", "Kitap ID:"))
        self.label_2.setText(_translate("Form", "Kitap Adı:"))
        self.label_3.setText(_translate("Form", "Kategori:"))
        self.label_4.setText(_translate("Form", "Yazar:"))
        self.label_5.setText(_translate("Form", "Yıl:"))
        self.label_6.setText(_translate("Form", "Stok:"))
        self.pushButton_guncelle.setText(_translate("Form", "Güncelle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
