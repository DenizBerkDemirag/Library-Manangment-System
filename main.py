from PyQt5.QtWidgets import QApplication
from Ana_Login import AnaLoginPage

app = QApplication([])
pencere = AnaLoginPage()
pencere.show()
app.exec_()