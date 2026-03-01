# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        Form.setStyleSheet(Style.style_sheet)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEdit_kullanici_arama = QtWidgets.QLineEdit(Form)
        self.lineEdit_kullanici_arama.setMinimumHeight(35)
        self.lineEdit_kullanici_arama.setPlaceholderText("Kullanıcı adı veya ID ara...")
        self.lineEdit_kullanici_arama.setObjectName("lineEdit_kullanici_arama")
        self.verticalLayout.addWidget(self.lineEdit_kullanici_arama)

        # Butonlar için yatay yerleşim
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout()
        self.pushButton_kullanici_ara = QtWidgets.QPushButton(Form)
        self.pushButton_kullanici_ara.setMinimumHeight(35)
        self.horizontalLayout_buttons.addWidget(self.pushButton_kullanici_ara)

        self.pushButton_kullanici_sil = QtWidgets.QPushButton(Form)
        self.pushButton_kullanici_sil.setMinimumHeight(35)
        self.horizontalLayout_buttons.addWidget(self.pushButton_kullanici_sil)
        self.verticalLayout.addLayout(self.horizontalLayout_buttons)

        self.tableWidget_kullanici = QtWidgets.QTableWidget(Form)
        self.tableWidget_kullanici.setObjectName("tableWidget_kullanici")
        self.tableWidget_kullanici.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_kullanici.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalLayout.addWidget(self.tableWidget_kullanici)

        self.horizontalLayout_actions = QtWidgets.QHBoxLayout()
        self.pushButton_engelle = QtWidgets.QPushButton(Form)
        self.pushButton_engelle.setMinimumHeight(35)
        self.horizontalLayout_actions.addWidget(self.pushButton_engelle)

        self.pushButton_engel_ac = QtWidgets.QPushButton(Form)
        self.pushButton_engel_ac.setMinimumHeight(35)
        self.horizontalLayout_actions.addWidget(self.pushButton_engel_ac)
        self.verticalLayout.addLayout(self.horizontalLayout_actions)

        self.pushButton_cikis = QtWidgets.QPushButton(Form)
        self.pushButton_cikis.setMinimumHeight(35)
        self.pushButton_cikis.setObjectName("pushButton_cikis")
        self.verticalLayout.addWidget(self.pushButton_cikis)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _t = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_t("Form", "Form"))
        self.pushButton_kullanici_ara.setText(_t("Form", "Ara"))
        self.pushButton_kullanici_sil.setText(_t("Form", "Sil"))
        self.pushButton_engelle.setText(_t("Form", "Kullanıcı engelle"))
        self.pushButton_engel_ac.setText(_t("Form", "Kullanıcı engel aç"))
        self.pushButton_cikis.setText(_t("Form", "Çıkış"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
