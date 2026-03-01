
class Style:
    style_sheet = """
    QWidget {
        background-color: #f4f6f9;
        font-family: 'Segoe UI', sans-serif;
        font-size: 14px;
        color: #333333;
    }

    QGroupBox {
        background-color: #ffffff;
        border: 1px solid #e1e4e8;
        border-radius: 8px;
        margin-top: 20px;
        font-weight: bold;
        color: #2c3e50;
    }

    QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top center;
        padding: 0 10px;
        color: #2c3e50;
    }

    QPushButton {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
        font-weight: 600;
    }

    QPushButton:hover {
        background-color: #2980b9;
    }

    QPushButton:pressed {
        background-color: #1f618d;
    }

    QPushButton#pushButton_cikis, QPushButton#pushButton_iptal {
        background-color: #e74c3c;
    }

    QPushButton#pushButton_cikis:hover, QPushButton#pushButton_iptal:hover {
        background-color: #c0392b;
    }

    QLineEdit {
        background-color: #ffffff;
        border: 1px solid #ced4da;
        border-radius: 4px;
        padding: 5px;
        selection-background-color: #3498db;
    }

    QLineEdit:focus {
        border: 1px solid #3498db;
    }

    QLabel {
        color: #2c3e50;
        font-weight: 500;
    }

    QCommandLinkButton {
        background-color: #ffffff;
        border: 1px solid #e1e4e8;
        border-radius: 6px;
        padding: 5px;
        color: #2c3e50;
        font-weight: bold;
    }

    QCommandLinkButton:hover {
        background-color: #e8f6fc;
        border-color: #3498db;
    }
    """
