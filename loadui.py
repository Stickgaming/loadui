import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6 import uic


class windowthing(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("thing")
        self.resize(150,100)

        cwidget = QWidget()
        self.setCentralWidget(cwidget)
        layout = QVBoxLayout(cwidget)

        self.label = QLabel("view a .ui file", self)
        layout.addWidget(self.label)

        self.button = QPushButton("Open File", self)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "UI (*.ui)"
        )

        if file_path:
            uic.loadUi(f"{file_path}", self)


app = QApplication(sys.argv)
window = windowthing()
window.show()
sys.exit(app.exec())