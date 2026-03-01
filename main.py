from PyQt5.QtWidgets import QApplication
from LibraryPy.core.Ana_Login import AnaLoginPage

app = QApplication([])
pencere = AnaLoginPage()
pencere.show()
app.exec_()