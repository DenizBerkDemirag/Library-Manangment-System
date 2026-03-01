from PyQt5.QtWidgets import *

from Database import Veritabani
from Window.Uye_Kayit_python import Ui_Form

class UyeKayitPage(QWidget):
    def __init__(self):
        super().__init__()
        self.UyeForm = Ui_Form()
        self.UyeForm.setupUi(self)
        self.db = Veritabani()

        self.UyeForm.commandLinkButton.clicked.connect(self.cikis)
        self.UyeForm.pushButton_ogrenci_giris.clicked.connect(self.kayit)

    def cikis(self):
        self.close()

    def kayit(self):
        id = self.UyeForm.lineEdit_ogrenci_id.text().strip()
        sifre = self.UyeForm.lineEdit_ogrenci_sifre.text().strip()
        if not id or not sifre:
            QMessageBox.warning(self,"Hata","ID veya şifre boş bırakılamaz!")
            return
        if self.db.Id_kontrol(id):
            QMessageBox.warning(self,"Hata","Bu ID kullanılıyor.")
            return

        basarili = self.db.uye_kayit_yap(id, sifre)

        self.UyeForm.lineEdit_ogrenci_id.clear()
        self.UyeForm.lineEdit_ogrenci_sifre.clear()
        if basarili:
            QMessageBox.information(self, "Başarılı", "Kayıt oldunuz.")
        else:
            QMessageBox.warning(self,"Hata","Kayıt Başarısız!")
