from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from LibraryPy.core.Database import Veritabani
from LibraryPy.Window.Login_python import Ui_Form
from LibraryPy.core.Yönlendirme import YönlendirmePage


class LoginPage(QWidget):
    LoginCikisSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.LoginForm = Ui_Form()
        self.LoginForm.setupUi(self)
        self.db = Veritabani()
        self.NesneYonlendirme = YönlendirmePage(is_admin=False)
        self.LoginForm.pushButton_ogrenci_giris.clicked.connect(self.ogrenci_giris)
        self.LoginForm.pushButton_cikis.clicked.connect(self.ana_login)

    def ogrenci_giris(self):
        kullanici_id = self.LoginForm.lineEdit_ogrenci_id.text().strip()
        sifre = self.LoginForm.lineEdit_ogrenci_sifre.text().strip()

        if self.db.giris_kontrol(kullanici_id,sifre):
            if self.db.engel_kontrol(kullanici_id):
                QMessageBox.warning(self,"Hata","Hesabınız engellendi!")
                return
            else:
                self.NesneYonlendirme = YönlendirmePage(is_admin=False)
                self.NesneYonlendirme.show()
        elif self.db.admin_giris_kontrol(kullanici_id,sifre):
            self.NesneYonlendirme = YönlendirmePage(is_admin=True)
            self.NesneYonlendirme.show()
        else:
            QMessageBox.warning(self, "Hata", "ID veya şifre hatalı")
            return
        self.close()

    def ana_login(self):
        self.LoginCikisSignal.emit()
        self.close()
