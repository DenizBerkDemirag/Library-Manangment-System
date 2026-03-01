from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from LibraryPy.core.Database import Veritabani
from LibraryPy.Window.Siparis_ver_python import Ui_Form

class SiparisVerPage(QWidget):
    def __init__(self):
        super().__init__()
        self.SiparisVerForm = Ui_Form()
        self.SiparisVerForm.setupUi(self)
        self.db = Veritabani()

        self.SiparisVerForm.dateEdit_tarih.setMinimumDate(QDate.currentDate())
        self.SiparisVerForm.dateEdit_tarih.setDate(QDate.currentDate())
        self.SiparisVerForm.pushButton_onayla.clicked.connect(self.onayla)


    def onayla(self):
        kullanici_id = self.SiparisVerForm.lineEdit_kullanici_id.text().strip()
        kitap_id = self.SiparisVerForm.lineEdit_kitap_id.text().strip()
        adres = self.SiparisVerForm.textEdit_adres.toPlainText().strip()
        tarih_str = self.SiparisVerForm.dateEdit_tarih.date().toString("yyyy-MM-dd")
        bugun = QDate.currentDate().toString("yyyy-MM-dd")
        durum = "Aktif"

        if not all ([kullanici_id, kitap_id, adres]):
            QMessageBox.warning(self, "Hata", "Bütün alanlar doldurulmalıdır.")
            return

        basarili = self.db.siparis_kontrol(kullanici_id,kitap_id)

        if not basarili:
            QMessageBox.warning(self, "Hata", "Girilen bilgiler yanlış!")
            return

        try:
            kitap_id = int(kitap_id)
        except ValueError:
            QMessageBox.warning(self, "Hata", "Kitap ID sayısal olmalıdır.")
            return


        basarili_mi = self.db.siparis_bilgiler(kullanici_id,kitap_id,adres,bugun,tarih_str,durum)
        if basarili_mi:
            QMessageBox.information(self, "Başarılı", "Sipariş başarılı.")