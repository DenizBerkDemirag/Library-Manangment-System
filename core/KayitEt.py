from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from LibraryPy.core.Database import Veritabani
from LibraryPy.Window.KayitEt_python import Ui_Form


class KayitEtPage(QWidget):
    kayitedildi = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.KayitEtForm = Ui_Form()
        self.KayitEtForm.setupUi(self)

        self.db = Veritabani()

        self.KayitEtForm.pushButton_kayit_et.clicked.connect(self.Kaydet)

    def Kaydet(self):
        self.kitap_ad = self.KayitEtForm.lineEdit_kitap_ad.text().strip()
        self.kategori_ad = self.KayitEtForm.lineEdit_kategori_ad.text().strip()
        self.yazar = self.KayitEtForm.lineEdit_yazar.text().strip()
        self.yayinlanma = self.KayitEtForm.lineEdit_yayinlanma.text().strip()
        self.stok = self.KayitEtForm.lineEdit_stok.text().strip()

        if not all([self.kitap_ad, self.kategori_ad, self.yazar, self.yayinlanma, self.stok]):
            QMessageBox.warning(self, "Hata", "Tüm alanlar doldurulmalıdır.")
            return

        try:
            self.yayinlanma = int(self.yayinlanma)
        except ValueError:
            QMessageBox.warning(self, "Hata", "Yayınlanma tarihi sayısal olmalıdır.")
            return

        basarili = self.db.kayit_yap( self.kitap_ad, self.kategori_ad, self.yazar, self.yayinlanma, self.stok)

        if basarili:
            QMessageBox.information(self, "Başarılı", "Kayıt başarılı.")
            self.kayitedildi.emit()
