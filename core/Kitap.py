from PyQt5.QtWidgets import *
from LibraryPy.core.Guncelle import GuncellePage
from LibraryPy.core.KayitEt import KayitEtPage
from LibraryPy.Window.Kitap_python import Ui_Form
from LibraryPy.core.Database import Veritabani

class KitapPage(QWidget):
    def __init__(self, is_admin=False, kategori=None):
        super().__init__()
        self.KitapForm = Ui_Form()
        self.KitapForm.setupUi(self)

        self.db = Veritabani()
        self.kategori_adi = kategori

        self.kitaplari_yukle()
        self.KitapForm.pushButton_cikis.clicked.connect(self.cikis)

        self.KitapForm.pushButton_ara.clicked.connect(self.kitap_arama)

        self.NesneKayit = KayitEtPage()
        self.KitapForm.pushButton_kayit.clicked.connect(self.kitap_kayit_ekrani)
        self.NesneKayit.kayitedildi.connect(self.kitaplari_yukle)

        self.NesneGuncelle = GuncellePage()
        self.KitapForm.pushButton_guncelle.clicked.connect(self.guncelle_ekrani)
        self.NesneGuncelle.guncellendi.connect(self.kitaplari_yukle)

        self.KitapForm.pushButton_sil.clicked.connect(self.sil)

        self.KitapForm.tableWidget_Kitap.setHorizontalHeaderLabels([
            "ID","Kitap Adı","Kategori","Yazar","Yayınlanma \n Tarihi","Stok"
        ])
        header = self.KitapForm.tableWidget_Kitap.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        self.KitapForm.tableWidget_Kitap.verticalHeader().setVisible(False)

        if not is_admin:
            self.KitapForm.pushButton_kayit.hide()
            self.KitapForm.pushButton_guncelle.hide()
            self.KitapForm.pushButton_sil.hide()

        if is_admin:
            self.KitapForm.tableWidget_Kitap.setSelectionMode(QTableWidget.SingleSelection)


    def cikis(self):
        self.close()

    def kitaplari_yukle(self):
        kitaplar = self.db.kategori_yazdir(self.kategori_adi)
        self.tabloyu_doldur(kitaplar)

    def tabloyu_doldur(self, veriler):
        self.KitapForm.tableWidget_Kitap.blockSignals(True)

        self.KitapForm.tableWidget_Kitap.clearContents()

        if not veriler:
            self.KitapForm.tableWidget_Kitap.setRowCount(0)
            return

        self.KitapForm.tableWidget_Kitap.setRowCount(len(veriler))
        self.KitapForm.tableWidget_Kitap.setColumnCount(len(veriler[0]))

        for i, row in enumerate(veriler):
            for j, value in enumerate(row):
                self.KitapForm.tableWidget_Kitap.setItem(
                    i, j, QTableWidgetItem(str(value))
                )

        self.KitapForm.tableWidget_Kitap.blockSignals(False)

    def kitap_arama(self):
        arama = self.KitapForm.lineEdit_arama.text().strip()

        if not arama:
            self.kitaplari_yukle()
            return

        sonuc = self.db.kategori_arama_yap(self.kategori_adi, arama)
        self.tabloyu_doldur(sonuc)


    def kitap_kayit_ekrani(self):
        self.NesneKayit.show()

    def guncelle_ekrani(self):
        self.NesneGuncelle.show()

    def sil(self):
        self.row = self.KitapForm.tableWidget_Kitap.currentRow()

        if self.row == -1:
            QMessageBox.warning(self,"Hata","Kitap Seçilmedi!")
            return

        self.silinecek_id = self.KitapForm.tableWidget_Kitap.item(self.row , 0)
        id = int(self.silinecek_id.text().strip())

        basarili = self.db.kayit_sil(id)

        if basarili:
            QMessageBox.information(self,"Başarılı","Silme işlemi gerçekleşti.")
            self.kitaplari_yukle()