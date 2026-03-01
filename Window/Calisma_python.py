# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.Style import Style

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 700)
        Form.setMinimumSize(QtCore.QSize(600, 600))
        Form.setStyleSheet(Style.style_sheet)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Header
        self.label_header = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        self.label_header.setFont(font)
        self.label_header.setAlignment(QtCore.Qt.AlignCenter)
        self.label_header.setText("Çalışma Salonu / Masa Durumu")
        self.label_header.setObjectName("label_header")
        self.verticalLayout.addWidget(self.label_header)
        
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout.addWidget(self.line)

        # Grid of Desks
        self.groupBox_grid = QtWidgets.QGroupBox(Form)
        self.groupBox_grid.setTitle("")
        self.groupBox_grid.setFlat(True)
        self.groupBox_grid.setStyleSheet("border: none; background: transparent;")
        self.groupBox_grid.setObjectName("groupBox_grid")
        
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_grid)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")

        desk_style = """
            QCheckBox {
                spacing: 0px;
            }
            QCheckBox::indicator {
                width: 40px;
                height: 40px;
                background-color: #2ecc71; /* Green for Available */
                border-radius: 4px;
                border: 1px solid #27ae60;
            }
            QCheckBox::indicator:checked {
                background-color: #e74c3c; /* Red for Occupied */
                border: 1px solid #c0392b;
                image: url(:/icons/user.png); /* Placeholder if needed */
            }
            QCheckBox::indicator:hover {
                border: 2px solid #2c3e50;
            }
        """
        
        # Create 100 checkboxes
        cols = 10
        
        for i in range(1, 101):
            if i == 1:
                obj_name = "checkBox"
            else:
                obj_name = f"checkBox_{i}"
                
            cb = QtWidgets.QCheckBox(self.groupBox_grid)
            cb.setText(str(i))
            cb.setObjectName(obj_name)
            cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            cb.setStyleSheet(desk_style)
            cb.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
            cb.setFocusPolicy(QtCore.Qt.NoFocus)

            
            row = (i - 1) // cols
            col = (i - 1) % cols
            
            self.gridLayout.addWidget(cb, row, col)
            
            # Save to self
            setattr(self, obj_name, cb)

        self.verticalLayout.addWidget(self.groupBox_grid)
        
        # Occupancy Status
        self.frame_occupancy = QtWidgets.QFrame(Form)
        self.frame_occupancy.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_occupancy.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_occupancy.setObjectName("frame_occupancy")
        self.horizontalLayout_occupancy = QtWidgets.QHBoxLayout(self.frame_occupancy)
        self.horizontalLayout_occupancy.setObjectName("horizontalLayout_occupancy")
        
        self.label_occupancy_title = QtWidgets.QLabel(self.frame_occupancy)
        font_occ = QtGui.QFont()
        font_occ.setBold(True)
        self.label_occupancy_title.setFont(font_occ)
        self.label_occupancy_title.setText("Doluluk Oranı:")
        self.label_occupancy_title.setObjectName("label_occupancy_title")
        self.horizontalLayout_occupancy.addWidget(self.label_occupancy_title)
        
        self.progressBar_occupancy = QtWidgets.QProgressBar(self.frame_occupancy)
        self.progressBar_occupancy.setProperty("value", 0)
        self.progressBar_occupancy.setTextVisible(True)
        self.progressBar_occupancy.setFormat("%p%")
        self.progressBar_occupancy.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #e74c3c;
                width: 20px;
            }
        """)
        self.progressBar_occupancy.setObjectName("progressBar_occupancy")
        self.horizontalLayout_occupancy.addWidget(self.progressBar_occupancy)
        
        self.verticalLayout.addWidget(self.frame_occupancy)

        # Legend
        self.horizontalLayout_legend = QtWidgets.QHBoxLayout()
        self.horizontalLayout_legend.setAlignment(QtCore.Qt.AlignCenter)
        
        lbl_avail = QtWidgets.QLabel("Yeşil: Müsait")
        lbl_avail.setStyleSheet("color: #2ecc71; font-weight: bold; margin-right: 20px;")
        self.horizontalLayout_legend.addWidget(lbl_avail)
        
        lbl_occ = QtWidgets.QLabel("Kırmızı: Dolu")
        lbl_occ.setStyleSheet("color: #e74c3c; font-weight: bold;")
        self.horizontalLayout_legend.addWidget(lbl_occ)
        
        self.verticalLayout.addLayout(self.horizontalLayout_legend)

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        # Exit Button
        self.pushButton = QtWidgets.QPushButton(Form) # Was pushButton in original
        self.pushButton.setMinimumHeight(40)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Çalışma Salonu"))
        self.pushButton.setText(_translate("Form", "Çıkış"))



    def update_occupancy_status(self):
        total_desks = 100
        occupied_count = 0
        
        # Iterate through all checkboxes
        for i in range(1, 101):
            if i == 1:
                chk = getattr(self, "checkBox", None)
            else:
                chk = getattr(self, f"checkBox_{i}", None)
                
            if chk and chk.isChecked():
                occupied_count += 1
                
        percent = int((occupied_count / total_desks) * 100)
        self.progressBar_occupancy.setValue(percent)
        

        if percent < 50:
             self.progressBar_occupancy.setStyleSheet("""
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #2ecc71; 
                }
            """)
        elif percent < 80:
             self.progressBar_occupancy.setStyleSheet("""
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #f39c12; 
                }
            """)
        else:
             self.progressBar_occupancy.setStyleSheet("""
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #e74c3c; 
                }
            """)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    
    # Test occupancy manually
    import random
    for i in range(1, 101):
        if random.random() > 0.7:
            if i == 1:
                ui.checkBox.setChecked(True)
            else:
                getattr(ui, f"checkBox_{i}").setChecked(True)
    ui.update_occupancy_status()
    
    Form.show()
    sys.exit(app.exec_())
