from PyQt5.QtWidgets import *
from LibraryPy.Window.Tum_Kitaplar_python import Ui_Form
from LibraryPy.core.Database import Veritabani
from LibraryPy.core.Guncelle import GuncellePage
from LibraryPy.core.KayitEt import KayitEtPage

class TumKitaplarPage(QWidget):
    def __init__(self, is_admin:False):
        super().__init__()
        self.TumKitaplarForm = Ui_Form()
        self.TumKitaplarForm.setupUi(self)
        self.db = Veritabani()
        self.kitaplari_yukle()
        self.TumKitaplarForm.pushButton_ara.clicked.connect(self.kitap_arama)

        self.TumKitaplarForm.pushButton_cikis.clicked.connect(self.cikis)

        self.NesneKayit = KayitEtPage()
        self.TumKitaplarForm.pushButton_ekle.clicked.connect(self.kitap_kayit_ekrani)
        self.NesneKayit.kayitedildi.connect(self.kitaplari_yukle)

        self.NesneGuncelle = GuncellePage()
        self.TumKitaplarForm.pushButton_guncelle.clicked.connect(self.guncelle_ekrani)
        self.NesneGuncelle.guncellendi.connect(self.kitaplari_yukle)

        self.TumKitaplarForm.pushButton_sil.clicked.connect(self.sil)

        self.TumKitaplarForm.tableWidget_kitaplar.setHorizontalHeaderLabels([
            "ID","Kitap Adı","Kategori","Yazar","Yayınlanma \n Tarihi","Stok"
        ])
        header = self.TumKitaplarForm.tableWidget_kitaplar.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QHeaderView.Stretch)
        header.setSectionResizeMode(3,QHeaderView.Stretch)

        if not is_admin:
            self.TumKitaplarForm.pushButton_ekle.hide()
            self.TumKitaplarForm.pushButton_guncelle.hide()
            self.TumKitaplarForm.pushButton_sil.hide()

    def kitaplari_yukle(self):
        kitaplar = self.db.kitap_yazdir()
        self.tabloyu_doldur(kitaplar)

    def tabloyu_doldur(self, veriler):
        self.TumKitaplarForm.tableWidget_kitaplar.blockSignals(True)

        self.TumKitaplarForm.tableWidget_kitaplar.clearContents()

        if not veriler:
            self.TumKitaplarForm.tableWidget_kitaplar.setRowCount(0)
            return

        self.TumKitaplarForm.tableWidget_kitaplar.setRowCount(len(veriler))
        self.TumKitaplarForm.tableWidget_kitaplar.setColumnCount(len(veriler[0]))

        for i, row in enumerate(veriler):
            for j, value in enumerate(row):
                self.TumKitaplarForm.tableWidget_kitaplar.setItem(
                    i, j, QTableWidgetItem(str(value))
                )

        self.TumKitaplarForm.tableWidget_kitaplar.blockSignals(False)

    def kitap_arama(self):
        arama = self.TumKitaplarForm.lineEdit_arama.text().strip()
        sonuc = self.db.kitap_arama(arama)

        if not arama:
            self.kitaplari_yukle()
            return

        self.tabloyu_doldur(sonuc)

    def kitap_kayit_ekrani(self):
        self.NesneKayit.show()

    def guncelle_ekrani(self):
        self.NesneGuncelle.show()

    def cikis(self):
        self.close()

    def sil(self):
        self.row = self.TumKitaplarForm.tableWidget_kitaplar.currentRow()

        if self.row == -1:
            QMessageBox.warning(self,"Hata","Kitap Seçilmedi!")
            return

        self.silinecek_id = self.TumKitaplarForm.tableWidget_kitaplar.item(self.row , 0)
        id = int(self.silinecek_id.text().strip())

        basarili = self.db.kayit_sil(id)

        if basarili:
            QMessageBox.information(self,"Başarılı","Silme işlemi gerçekleşti.")
            self.kitaplari_yukle()
