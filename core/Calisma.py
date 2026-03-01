from PyQt5.QtWidgets import *

from LibraryPy.core.Database import Veritabani
from LibraryPy.Window.Calisma_python import Ui_Form

from PyQt5 import QtCore

class CalismaPage(QWidget):
    def __init__(self, is_admin=False):
        super().__init__()
        self.CalismaForm = Ui_Form()
        self.CalismaForm.setupUi(self)
        self.CalismaForm.pushButton.clicked.connect(self.calisma_cikis)
        self.db = Veritabani()
        self.is_admin = is_admin
        self.load_masa_durumlari()
        self.update_occupancy_status()

        if self.is_admin:
            self.enable_admin_access()
        else:
            self.disable_checkbox_interaction()

    def load_masa_durumlari(self):
        dolu_masalar = self.db.get_dolu_masalar()

        for i in range(1, 101):
            chk = getattr(
                self.CalismaForm,
                "checkBox" if i == 1 else f"checkBox_{i}"
            )

            chk.blockSignals(True)
            chk.setChecked(i in dolu_masalar)
            chk.blockSignals(False)

    def enable_admin_access(self):
        for i in range(1, 101):
            chk = getattr(
                self.CalismaForm,
                "checkBox" if i == 1 else f"checkBox_{i}"
            )

            chk.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, False)
            chk.setFocusPolicy(QtCore.Qt.StrongFocus)

            chk.toggled.connect(
                lambda checked, masa_id=i: self.masa_toggled(masa_id, checked)
            )
    def disable_checkbox_interaction(self):
        for i in range(1, 101):
            chk = getattr(
                self.CalismaForm,
                "checkBox" if i == 1 else f"checkBox_{i}"
            )
            chk.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
            chk.setFocusPolicy(QtCore.Qt.NoFocus)

    def masa_toggled(self, masa_id: int, checked: bool):
        self.db.update_masa_durumu(masa_id, checked)
        self.update_occupancy_status()

    def update_occupancy_status(self):
        total, occupied = self.db.get_occupancy_counts()
        percent = int((occupied / total) * 100) if total else 0

        pb = self.CalismaForm.progressBar_occupancy
        pb.setValue(percent)

        if percent < 50:
            color = "#2ecc71"
        elif percent < 80:
            color = "#f39c12"
        else:
            color = "#e74c3c"

        pb.setStyleSheet(f"""
            QProgressBar {{
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }}
            QProgressBar::chunk {{
                background-color: {color};
            }}
        """)

    def calisma_cikis(self):
        self.close()