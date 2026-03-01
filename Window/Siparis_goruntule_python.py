# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(792, 621)
        Form.setStyleSheet(Style.style_sheet)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(12)

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalLayout.addWidget(self.tableWidget)

        bot = QtWidgets.QHBoxLayout()
        self.pushButton_siparis_tamamlandi = QtWidgets.QPushButton(Form)
        self.pushButton_siparis_tamamlandi.setObjectName("pushButton_siparis_tamamlandi")
        self.pushButton_siparis_tamamlandi.setMinimumHeight(36)
        self.pushButton_siparis_tamamlandi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        bot.addWidget(self.pushButton_siparis_tamamlandi)
        bot.addStretch()
        self.verticalLayout.addLayout(bot)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _t = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_t("Form", "Sipariş Görüntüle"))
        self.pushButton_siparis_tamamlandi.setText(_t("Form", "Siparişi Tamamla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
