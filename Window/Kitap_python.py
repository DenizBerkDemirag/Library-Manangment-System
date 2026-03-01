# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 700)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setStyleSheet(Style.style_sheet)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Toolbar Container
        self.groupBox_toolbar = QtWidgets.QGroupBox(Form)
        self.groupBox_toolbar.setTitle("")
        self.groupBox_toolbar.setFlat(True)
        self.groupBox_toolbar.setStyleSheet("QGroupBox { border: none; background: transparent; margin: 0; }")
        self.groupBox_toolbar.setObjectName("groupBox_toolbar")
        
        self.horizontalLayout_toolbar = QtWidgets.QHBoxLayout(self.groupBox_toolbar)
        self.horizontalLayout_toolbar.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_toolbar.setSpacing(10)
        self.horizontalLayout_toolbar.setObjectName("horizontalLayout_toolbar")
        
        # Search Area
        self.lineEdit_arama = QtWidgets.QLineEdit(self.groupBox_toolbar)
        self.lineEdit_arama.setMinimumHeight(35)
        self.lineEdit_arama.setPlaceholderText("Kitap Ara...")
        self.lineEdit_arama.setObjectName("lineEdit_arama")
        self.horizontalLayout_toolbar.addWidget(self.lineEdit_arama)
        
        self.pushButton_ara = QtWidgets.QPushButton(self.groupBox_toolbar)
        self.pushButton_ara.setMinimumHeight(35)
        self.pushButton_ara.setObjectName("pushButton_ara")
        self.horizontalLayout_toolbar.addWidget(self.pushButton_ara)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_toolbar.addItem(spacerItem)
        
        # Action Buttons
        self.pushButton_kayit = QtWidgets.QPushButton(self.groupBox_toolbar)
        self.pushButton_kayit.setMinimumHeight(35)
        self.pushButton_kayit.setStyleSheet("background-color: #27ae60;")
        self.pushButton_kayit.setObjectName("pushButton_kayit")
        self.horizontalLayout_toolbar.addWidget(self.pushButton_kayit)
        
        self.pushButton_guncelle = QtWidgets.QPushButton(self.groupBox_toolbar)
        self.pushButton_guncelle.setMinimumHeight(35)
        self.pushButton_guncelle.setStyleSheet("background-color: #f39c12;")
        self.pushButton_guncelle.setObjectName("pushButton_guncelle")
        self.horizontalLayout_toolbar.addWidget(self.pushButton_guncelle)
        
        self.pushButton_sil = QtWidgets.QPushButton(self.groupBox_toolbar)
        self.pushButton_sil.setMinimumHeight(35)
        self.pushButton_sil.setStyleSheet("background-color: #c0392b;")
        self.pushButton_sil.setObjectName("pushButton_sil")
        self.horizontalLayout_toolbar.addWidget(self.pushButton_sil)
        
        self.verticalLayout.addWidget(self.groupBox_toolbar)
        
        # Table
        self.tableWidget_Kitap = QtWidgets.QTableWidget(Form)
        self.tableWidget_Kitap.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Kitap.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_Kitap.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_Kitap.setAlternatingRowColors(True)
        self.tableWidget_Kitap.setShowGrid(False)
        self.tableWidget_Kitap.setObjectName("tableWidget_Kitap")
        self.tableWidget_Kitap.setColumnCount(0)
        self.tableWidget_Kitap.setRowCount(0)
        self.tableWidget_Kitap.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Kitap.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalLayout.addWidget(self.tableWidget_Kitap)
        
        # Bottom Bar
        self.horizontalLayout_bottom = QtWidgets.QHBoxLayout()
        self.horizontalLayout_bottom.setObjectName("horizontalLayout_bottom")
        
        self.pushButton_cikis = QtWidgets.QPushButton(Form)
        self.pushButton_cikis.setMinimumHeight(35)
        self.pushButton_cikis.setObjectName("pushButton_cikis")
        self.horizontalLayout_bottom.addWidget(self.pushButton_cikis)
        
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_bottom.addItem(spacerItem2)
        
        self.verticalLayout.addLayout(self.horizontalLayout_bottom)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def icon_from_theme(self, name):
        return QtGui.QIcon()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kitap Yönetimi"))
        self.pushButton_ara.setText(_translate("Form", "Ara"))
        self.pushButton_kayit.setText(_translate("Form", "Yeni Kitap Ekle"))
        self.pushButton_guncelle.setText(_translate("Form", "Güncelle"))
        self.pushButton_sil.setText(_translate("Form", "Seçileni Sil"))
        self.pushButton_cikis.setText(_translate("Form", "Geri Dön"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
