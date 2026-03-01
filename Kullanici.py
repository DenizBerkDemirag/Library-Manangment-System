from PyQt5.QtWidgets import *

from Database import Veritabani
from Window.Kullanici_python import Ui_Form

class KullaniciPage(QWidget):
    def __init__(self):
        super().__init__()
        self.KullaniciForm = Ui_Form()
        self.KullaniciForm.setupUi(self)
        self.db = Veritabani()
        self.kullanici_yukle()
        self.KullaniciForm.pushButton_kullanici_ara.clicked.connect(self.kullanici_arama)
        self.KullaniciForm.pushButton_kullanici_sil.clicked.connect(self.sil)
        self.KullaniciForm.pushButton_cikis.clicked.connect(self.cikis)
        self.KullaniciForm.pushButton_engelle.clicked.connect(self.engelle)
        self.KullaniciForm.pushButton_engel_ac.clicked.connect(self.engel_ac)

        self.KullaniciForm.tableWidget_kullanici.setHorizontalHeaderLabels([
            "Kullanıcı\nID","Şifre","Engel\nDurumu"
        ])

        header = self.KullaniciForm.tableWidget_kullanici.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.KullaniciForm.tableWidget_kullanici.verticalHeader().setVisible(False)

    def kullanici_yukle(self):
        kullanicilar = self.db.kullanici_yükle()
        self.tabloyu_doldur(kullanicilar)

    def tabloyu_doldur(self, kullanicilar):
        self.KullaniciForm.tableWidget_kullanici.blockSignals(True)

        self.KullaniciForm.tableWidget_kullanici.clearContents()

        if not kullanicilar:
            self.KullaniciForm.tableWidget_kullanici.setRowCount(0)
            return

        self.KullaniciForm.tableWidget_kullanici.setRowCount(len(kullanicilar))
        self.KullaniciForm.tableWidget_kullanici.setColumnCount(len(kullanicilar[0]))

        for i, row in enumerate(kullanicilar):
            for j, value in enumerate(row):
                self.KullaniciForm.tableWidget_kullanici.setItem(
                    i, j, QTableWidgetItem(str(value))
                )

        self.KullaniciForm.tableWidget_kullanici.blockSignals(False)

    def kullanici_arama(self):
        arama = self.KullaniciForm.lineEdit_kullanici_arama.text().strip()
        sonuc = self.db.kullanici_arama(arama)

        if not arama:
            self.kullanici_yukle()
            return

        self.tabloyu_doldur(sonuc)


    def sil(self):
        self.row = self.KullaniciForm.tableWidget_kullanici.currentRow()

        if self.row == -1:
            QMessageBox.warning(self,"Hata","Kullanıcı seçilmedi!")
            return

        self.silinecek_id = self.KullaniciForm.tableWidget_kullanici.item(self.row,0)
        id = self.silinecek_id.text().strip()

        basarili = self.db.kullanici_sil(id)

        if basarili:
            QMessageBox.information(self,"Başarılı","Silme işlemi gerçekleşti.")
            self.kullanici_yukle()

    def engelle(self):
        self.row = self.KullaniciForm.tableWidget_kullanici.currentRow()

        if self.row == -1:
            QMessageBox.warning(self,"Hata","Kullanıcı seçilmedi!")
            return

        self.engellenecek_id = self.KullaniciForm.tableWidget_kullanici.item(self.row,0)
        id = self.engellenecek_id.text().strip()

        basarili = self.db.engelle(id)

        if basarili:
            QMessageBox.information(self,"Başarılı","Kullanıcı engelleme başarılı.")
            self.kullanici_yukle()
            return

    def engel_ac(self):
        self.row = self.KullaniciForm.tableWidget_kullanici.currentRow()

        if self.row == -1:
            QMessageBox.warning(self, "Hata", "Kullanıcı seçilmedi!")
            return

        self.engellenecek_id = self.KullaniciForm.tableWidget_kullanici.item(self.row, 0)
        id = self.engellenecek_id.text().strip()

        basarili = self.db.engel_ac(id)

        if basarili:
            QMessageBox.information(self,"Başarılı","Kullanıcı engel kaldırıldı.")
            self.kullanici_yukle()
            return

    def cikis(self):
        self.close()