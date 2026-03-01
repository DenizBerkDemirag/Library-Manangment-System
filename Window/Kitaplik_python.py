# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style

# Kategori emojileri
KATEGORILER = [
    ("📜 Tarih",           "commandLinkButton_tarih"),
    ("💼 İş-Kariyer",      "commandLinkButton_is_kariyer"),
    ("👶 Çocuk",           "commandLinkButton_cocuk"),
    ("🔭 Bilim Kurgu",     "commandLinkButton_bilim_kurgu"),
    ("🎨 Sanat",           "commandLinkButton_sanat"),
    ("🎓 Eğitim",          "commandLinkButton_egitim"),
    ("✍️ Şiir",            "commandLinkButton_siir"),
    ("💻 Yazılım",         "commandLinkButton_yazilim"),
    ("🌌 Bilim",           "commandLinkButton_bilim"),
    ("🧒 Gençlik",         "commandLinkButton_genclik"),
    ("📖 Roman",           "commandLinkButton_roman"),
    ("🧠 Psikoloji",       "commandLinkButton_psikoloji"),
    ("🏰 Fantastik",       "commandLinkButton_fantastik"),
    ("📰 Biyografi",       "commandLinkButton_biyografi"),
    ("🕵️ Polisiye",        "commandLinkButton_polisiye"),
    ("🌱 Kişisel Gelişim", "commandLinkButton_kisisel_gelisim"),
    ("💰 Ekonomi",         "commandLinkButton_ekonomi"),
    ("⚙️ Teknoloji",       "commandLinkButton_teknoloji"),
    ("☪️ Din-Tasavvuf",    "commandLinkButton_din_tasavvuf"),
    ("🧘 Felsefe",         "commandLinkButton_felsefe"),
]

COLS = 5


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 640)
        Form.setMinimumSize(QtCore.QSize(700, 500))
        Form.setWindowTitle("Kitaplık")
        Form.setStyleSheet(Style.style_sheet)

        root = QtWidgets.QVBoxLayout(Form)
        root.setSpacing(16)
        root.setContentsMargins(20, 20, 20, 16)

        # Başlık
        lbl_title = QtWidgets.QLabel("Kitaplık — Kategori Seç")
        font_t = QtGui.QFont("Segoe UI", 18, QtGui.QFont.Bold)
        lbl_title.setFont(font_t)
        lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        root.addWidget(lbl_title)

        # Kategori grid
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)

        for idx, (label, obj_name) in enumerate(KATEGORILER):
            row = idx // COLS
            col = idx % COLS
            btn = QtWidgets.QCommandLinkButton(label)
            btn.setObjectName(obj_name)
            btn.setMinimumSize(QtCore.QSize(130, 64))
            btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.setIconSize(QtCore.QSize(0, 0))
            font = QtGui.QFont("Segoe UI", 10)
            btn.setFont(font)
            self.gridLayout.addWidget(btn, row, col)
            setattr(self, obj_name, btn)

        root.addLayout(self.gridLayout)

        # Ayırıcı
        sep = QtWidgets.QFrame()
        sep.setFrameShape(QtWidgets.QFrame.HLine)
        sep.setStyleSheet("border: 1px solid #e1e4e8;")
        root.addWidget(sep)

        # Alt eylem butonları
        action_row = QtWidgets.QHBoxLayout()
        action_row.setSpacing(10)

        self.pushButton_tum_kitaplar = QtWidgets.QPushButton("Tüm Kitapları Görüntüle")
        self.pushButton_tum_kitaplar.setObjectName("pushButton_tum_kitaplar")
        self.pushButton_tum_kitaplar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.pushButton_kullanici_goruntule = QtWidgets.QPushButton("Kullanıcıları Görüntüle")
        self.pushButton_kullanici_goruntule.setObjectName("pushButton_kullanici_goruntule")
        self.pushButton_kullanici_goruntule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.pushButton_siparis_goruntule = QtWidgets.QPushButton("Sipariş Görüntüle")
        self.pushButton_siparis_goruntule.setObjectName("pushButton_siparis_goruntule")
        self.pushButton_siparis_goruntule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.pushButton_siparis = QtWidgets.QPushButton("Sipariş Ver")
        self.pushButton_siparis.setObjectName("pushButton_siparis")
        self.pushButton_siparis.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.pushButton_kitaplik_cikis = QtWidgets.QPushButton("Çıkış")
        self.pushButton_kitaplik_cikis.setObjectName("pushButton_kitaplik_cikis")
        self.pushButton_kitaplik_cikis.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        for btn in [
            self.pushButton_tum_kitaplar,
            self.pushButton_kullanici_goruntule,
            self.pushButton_siparis_goruntule,
            self.pushButton_siparis,
            self.pushButton_kitaplik_cikis,
        ]:
            btn.setMinimumHeight(36)
            action_row.addWidget(btn)

        root.addLayout(action_row)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _t = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_t("Form", "Kitaplık"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
