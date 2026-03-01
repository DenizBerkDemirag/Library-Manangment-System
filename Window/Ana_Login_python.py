# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        Form.setMinimumSize(QtCore.QSize(400, 350))
        Form.setStyleSheet(Style.style_sheet)
        
        self.verticalLayout_main = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        
        # Center the content
        self.verticalLayout_center = QtWidgets.QVBoxLayout()
        self.verticalLayout_center.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_center.setContentsMargins(50, 50, 50, 50)
        
        # Card Container
        self.groupBox_card = QtWidgets.QGroupBox(Form)
        self.groupBox_card.setMinimumSize(QtCore.QSize(300, 250))
        self.groupBox_card.setTitle("")
        self.groupBox_card.setObjectName("groupBox_card")
        
        self.verticalLayout_card = QtWidgets.QVBoxLayout(self.groupBox_card)
        self.verticalLayout_card.setSpacing(15)
        self.verticalLayout_card.setContentsMargins(30, 30, 30, 30)
        
        # Title Label
        self.label_title = QtWidgets.QLabel(self.groupBox_card)
        font_title = QtGui.QFont()
        font_title.setFamily("Segoe UI")
        font_title.setPointSize(16)
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("Kütüphane Sistemi")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_card.addWidget(self.label_title)
        
        # Subtitle/Description
        self.label_subtitle = QtWidgets.QLabel(self.groupBox_card)
        font_sub = QtGui.QFont()
        font_sub.setPointSize(10)
        font_sub.setItalic(True)
        self.label_subtitle.setFont(font_sub)
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setText("Hoş geldiniz, lütfen işlem seçiniz")
        self.label_subtitle.setObjectName("label_subtitle")
        self.verticalLayout_card.addWidget(self.label_subtitle)
        
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_card.addItem(spacerItem)

        # Login Button
        self.pushButton = QtWidgets.QPushButton(self.groupBox_card)
        self.pushButton.setMinimumHeight(40)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_card.addWidget(self.pushButton)

        # Register Button
        self.commandLinkButton = QtWidgets.QPushButton(self.groupBox_card)
        self.commandLinkButton.setMinimumHeight(35)
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setFlat(True)
        self.commandLinkButton.setStyleSheet("color: #3498db; font-weight: bold; background: transparent;")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout_card.addWidget(self.commandLinkButton)

        self.verticalLayout_center.addWidget(self.groupBox_card)
        self.verticalLayout_main.addLayout(self.verticalLayout_center)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kütüphane Yönetim Sistemi"))
        self.pushButton.setText(_translate("Form", "Giriş Yap"))
        self.commandLinkButton.setText(_translate("Form", "Hesap Oluştur"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
