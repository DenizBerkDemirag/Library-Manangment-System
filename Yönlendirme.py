from PyQt5.QtWidgets import *


from Window.Yönlendirme_python import Ui_Form
from Kitaplik import KitaplikPage
from Calisma import CalismaPage

class YönlendirmePage(QWidget):
    def __init__(self, is_admin=False):
        super().__init__()
        self.YönlendirmeForm = Ui_Form()
        self.YönlendirmeForm.setupUi(self)
        self.NesneKitaplik = KitaplikPage(is_admin)
        self.NesneCalisma = CalismaPage(is_admin)
        self.YönlendirmeForm.pushButton_kitaplik.clicked.connect(self.kitaplik)
        self.YönlendirmeForm.pushButton_calisma.clicked.connect(self.calisma)
        self.NesneKitaplik.yanlisgiris.connect(self.geri_don)
    def kitaplik(self):
        self.NesneKitaplik.show()
        self.close()
    def calisma(self):
        self.NesneCalisma.show()
    def geri_don(self):
        self.show()