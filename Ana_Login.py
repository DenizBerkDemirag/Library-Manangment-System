from PyQt5.QtWidgets import *
from Login import LoginPage
from Uye_Kayit import UyeKayitPage
from Window.Ana_Login_python import Ui_Form

class AnaLoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.AnaLoginForm = Ui_Form()
        self.AnaLoginForm.setupUi(self)
        self.Nesneogrenci = LoginPage()
        self.Nesneogrenci.LoginCikisSignal.connect(self.goster)
        self.AnaLoginForm.pushButton.clicked.connect(self.giris)
        self.AnaLoginForm.commandLinkButton.clicked.connect(self.kayit)

    def giris(self):
        self.Nesneogrenci.show()
        self.close()

    def kayit(self):
        self.NesneUyeKayit = UyeKayitPage()
        self.NesneUyeKayit.show()

    def goster(self):
        self.show()