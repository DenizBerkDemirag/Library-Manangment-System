from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *


from LibraryPy.core.Database import Veritabani
from LibraryPy.Window.Siparis_goruntule_python import Ui_Form

class SiparisGoruntulePage(QWidget):
    def __init__(self):
        super().__init__()
        self.SiparisGoruntuleForm = Ui_Form()
        self.SiparisGoruntuleForm.setupUi(self)
        self.db = Veritabani()
        self.tabloyu_yukle()
        self.SiparisGoruntuleForm.pushButton_siparis_tamamlandi.clicked.connect(self.tamamla)

        self.SiparisGoruntuleForm.tableWidget.setHorizontalHeaderLabels([
            "Sipariş\nID","Kullanıcı\nID","Kitap\nID","Adres","Verilme\nTarihi","İade\nTarihi","Durum"
        ])

        header = self.SiparisGoruntuleForm.tableWidget.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        self.SiparisGoruntuleForm.tableWidget.verticalHeader().setVisible(False)

    def tabloyu_yukle(self):
        veriler = self.db.siparis_doldur()
        self.tabloyu_doldur(veriler)

    def tabloyu_doldur(self, veriler):
        table = self.SiparisGoruntuleForm.tableWidget
        table.blockSignals(True)
        table.clearContents()

        if not veriler:
            table.setRowCount(0)
            table.blockSignals(False)
            return

        table.setRowCount(len(veriler))
        table.setColumnCount(len(veriler[0]))

        for i, row in enumerate(veriler):
            tarih_ver = QDate.fromString(row[5], "yyyy-MM-dd")
            bugun = QDate.currentDate()
            sure_gecti = tarih_ver < bugun

            for j, value in enumerate(row):

                if j == 6:
                    if value == "Tamamlandı":
                        item = QTableWidgetItem("Tamamlandı")
                    elif sure_gecti:
                        item = QTableWidgetItem("SÜRE GEÇTİ")
                    else:
                        item = QTableWidgetItem(str(value))
                else:
                    item = QTableWidgetItem(str(value))

                table.setItem(i, j, item)

        table.blockSignals(False)


    def tamamla(self):
        row = self.SiparisGoruntuleForm.tableWidget.currentRow()

        if row == -1:
            QMessageBox.warning(self,"Hata","Sipariş Seçilmedi!")
            return

        tamamlanacak_id = self.SiparisGoruntuleForm.tableWidget.item(row , 0)
        id_siparis = int(tamamlanacak_id.text().strip())

        basarili = self.db.siparis_tamamla(id_siparis)

        if basarili:
            QMessageBox.information(self,"Başarılı","Sipariş tamamlandı!")
            self.tabloyu_yukle()