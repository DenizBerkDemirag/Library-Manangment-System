from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from Database import Veritabani
from Window.Guncelle_python import Ui_Form


class GuncellePage(QWidget):
    guncellendi = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.GuncelleForm = Ui_Form()
        self.GuncelleForm.setupUi(self)

        self.db = Veritabani()

        self.GuncelleForm.pushButton_guncelle.clicked.connect(self.guncelle)

    def guncelle(self):

        self.kitap_id = self.GuncelleForm.lineEdit_guncelle_id.text().strip()
        self.kitap_adi = self.GuncelleForm.lineEdit_guncelle_kitao_ad.text().strip()
        self.kategori = self.GuncelleForm.lineEdit_guncelle_kategori_ad.text().strip()
        self.yazar = self.GuncelleForm.lineEdit_guncelle_yazar_ad.text().strip()
        self.yayinlanma = self.GuncelleForm.lineEdit_guncelle_yayinlanma.text().strip()
        self.stok = self.GuncelleForm.lineEdit_guncelle_stok.text().strip()

        if not all([self.kitap_id, self.kitap_adi, self.kategori, self.yazar, self.yayinlanma, self.stok]):
            QMessageBox.warning(self,"Hata","Bütün alanlar doldurulmalıdır.")
            return

        try:
            self.kitap_id = int(self.kitap_id)
            self.yayinlanma = int(self.yayinlanma)
        except ValueError:
            QMessageBox.warning(self, "Hatalı Giriş", "ID ve Yayınlanma Tarihi sayısal olmalıdır.")
            return

        basarili = self.db.guncelleme_yap(self.kitap_id, self.kitap_adi, self.kategori, self.yazar, self.yayinlanma, self.stok)

        if basarili:
            QMessageBox.information(self, "Başarılı", "Güncelleme başarılı.")
            self.guncellendi.emit()
        else:
            QMessageBox.warning(self, "Uyarı", "Güncelleme yapılmadı!")