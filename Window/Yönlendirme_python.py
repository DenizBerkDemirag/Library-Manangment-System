# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        Form.setMinimumSize(QtCore.QSize(600, 400))
        Form.setStyleSheet(Style.style_sheet)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label_title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("Lütfen bir bölüm seçiniz")
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        
        self.horizontalLayout_cards = QtWidgets.QHBoxLayout()
        self.horizontalLayout_cards.setSpacing(40)
        self.horizontalLayout_cards.setObjectName("horizontalLayout_cards")
        
        # Library Button Wrapper
        self.pushButton_kitaplik = QtWidgets.QPushButton(Form)
        self.pushButton_kitaplik.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.pushButton_kitaplik.setMinimumSize(QtCore.QSize(250, 200))
        self.pushButton_kitaplik.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_kitaplik.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 20px;
                border-radius: 15px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980b9;
                margin-top: -5px; /* Lift effect */
            }
            QPushButton:pressed {
                background-color: #1abc9c;
                margin-top: 0px;
            }
        """)
        self.pushButton_kitaplik.setObjectName("pushButton_kitaplik")
        self.horizontalLayout_cards.addWidget(self.pushButton_kitaplik)
        
        # Study Room Button Wrapper
        self.pushButton_calisma = QtWidgets.QPushButton(Form)
        self.pushButton_calisma.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.pushButton_calisma.setMinimumSize(QtCore.QSize(250, 200))
        self.pushButton_calisma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_calisma.setStyleSheet("""
            QPushButton {
                background-color: #9b59b6;
                color: white;
                font-size: 20px;
                border-radius: 15px;
                border: none;
            }
            QPushButton:hover {
                background-color: #8e44ad;
                margin-top: -5px; /* Lift effect */
            }
            QPushButton:pressed {
                background-color: #1abc9c;
                margin-top: 0px;
            }
        """)
        self.pushButton_calisma.setObjectName("pushButton_calisma")
        self.horizontalLayout_cards.addWidget(self.pushButton_calisma)
        
        self.verticalLayout.addLayout(self.horizontalLayout_cards)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Odalar"))
        self.pushButton_kitaplik.setText(_translate("Form", "📚 Kitaplık"))
        self.pushButton_calisma.setText(_translate("Form", "🖥️ Çalışma Odası"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
