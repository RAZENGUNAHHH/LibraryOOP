from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QInputDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library")
        self.setFixedSize(QSize(1600, 800))

        # กำหนดพื้นหลังเป็นรูปภาพ
        palette = self.palette()
        image = QImage("thumb-1920-1339726.png")
        palette.setBrush(QPalette.ColorRole.Window, QBrush(image))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # สร้าง QVBoxLayout และ QHBoxLayout สำหรับปุ่มและ Label
        vbox = QVBoxLayout(self)
        vbox.setAlignment(Qt.AlignmentFlag.AlignTop)

        label_layout = QHBoxLayout()
        label_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_layout.setContentsMargins(0, 20, 0, 20)  # กำหนดระยะห่างด้านบนและด้านล่าง

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.setSpacing(20)

        vbox.addLayout(label_layout)
        vbox.addLayout(button_layout)

        # เพิ่ม QLabel ด้านบน
        label = QLabel("Library")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: white; background-color: rgba(0, 0, 0, 0.5);")
        label_layout.addWidget(label)

        # สร้างและแสดงปุ่ม
        self.display_button("Add new member", button_layout)
        self.display_button("Search member", button_layout)
        self.display_button("Add new book", button_layout)
        self.display_button("Search book", button_layout)
        self.display_button("Borrow a book", button_layout)
        self.display_button("Return the book", button_layout)
        self.display_button("Check The book is overdue", button_layout)

    def display_button(self, text, layout):
        btn = QPushButton(text)
        btn.setFixedSize(QSize(150, 50))
        layout.addWidget(btn)
        if text == "Add new member":
            btn.clicked.connect(self.add_new_member)
        if text == "Search member":
            btn.clicked.connect(self.search_member)
        if text == "Add new book":
            btn.clicked.connect(self.add_new_book)
        if text == "Search book":
            btn.clicked.connect(self.search_book)

    def add_new_member(self):
        text, ok = QInputDialog.getText(self, "Add New Member", "Enter member name:")
        if ok:
            print(f"New member name: {text}")

    def search_member(self):
        text, ok = QInputDialog.getText(self, "Search Member", "Enter member name:")
        if ok:
            print(f"complete")

    def add_new_book(self):
        text, ok = QInputDialog.getText(self, "Add new book", "Enter book's name:")
        if ok:
            print(f"New book's name: {text}")

    def search_book(self):
        text, ok = QInputDialog.getText(self, "Search book", "Enter book's name:")
        if ok:
            print(f"complete")

# รันแอปพลิเคชัน
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
