from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from Database import Veritabani
from Kitap import KitapPage
from Kullanici import KullaniciPage
from SiparisGoruntule import SiparisGoruntulePage
from Siparis_ver import SiparisVerPage
from Tum_Kitaplar import TumKitaplarPage
from Window.Kitaplik_python import Ui_Form

class KitaplikPage(QWidget):
    yanlisgiris = pyqtSignal()
    def __init__(self, is_admin=False):
        super().__init__()
        self.KitaplikForm = Ui_Form()
        self.KitaplikForm.setupUi(self)
        self.db = Veritabani()
        self.NesneKullanici = KullaniciPage()
        self.NesneSiparis = SiparisVerPage()
        self.NesneSiparisGoruntule = SiparisGoruntulePage()
        self.KitaplikForm.pushButton_kitaplik_cikis.clicked.connect(self.kitaplik_cikis)
        self.KitaplikForm.pushButton_tum_kitaplar.clicked.connect(self.tum_kitaplar)
        self.KitaplikForm.pushButton_kullanici_goruntule.clicked.connect(self.kullanici_goruntule)
        self.KitaplikForm.pushButton_siparis.clicked.connect(self.siparis_sayfasi)
        self.KitaplikForm.pushButton_siparis_goruntule.clicked.connect(self.siparis_goruntule_sayfasi)
        self.is_admin = is_admin

        for btn in self.findChildren(QCommandLinkButton):
            btn.clicked.connect(self.kategoriye_gore_getir)

        if not is_admin:
            self.KitaplikForm.pushButton_kullanici_goruntule.hide()
            self.KitaplikForm.pushButton_siparis_goruntule.hide()

    def kategoriye_gore_getir(self):
        btn = self.sender()
        if not btn:
            return

        # Buton metni "📜 Tarih" formatında; emoji ve baştaki boşlukları at
        raw = btn.text()
        # Emoji olmayan ilk kelimeyi/metni bul: boşluktan sonrasını al
        parts = raw.strip().split()
        # İlk parça emoji ise geri kalanını birleştir, değilse tümünü kullan
        if parts and not parts[0].isascii():
            self.kategori = " ".join(parts[1:])
        else:
            self.kategori = raw.strip()

        self.NesneKitap = KitapPage(self.is_admin, self.kategori)
        self.NesneKitap.show()

    def tum_kitaplar(self):
        self.NesneTumKitaplar = TumKitaplarPage(self.is_admin)
        self.NesneTumKitaplar.show()

    def kullanici_goruntule(self):
        self.NesneKullanici.show()

    def siparis_sayfasi(self):
        self.NesneSiparis.show()

    def siparis_goruntule_sayfasi(self):
        self.NesneSiparisGoruntule.show()

    def kitaplik_cikis(self):
        self.yanlisgiris.emit()
        self.close()