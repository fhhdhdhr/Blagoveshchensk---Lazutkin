
import sys
import sqlite3


from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QPixmap


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Chemistry')

        self.btn = QPushButton('Найти', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText("Привет, ведите ваш элемент")
        self.label.move(40, 30)
        self.label.resize(300, 400)

        self.image = QPixmap("download.png")
        self.label.setPixmap(self.image)
        self.name_input = QLineEdit(self)
        self.name_input.move(150, 90)


        self.chek_label = QLabel(self)
        self.chek_label.setText(f"Атомная масса")
        self.chek_label.move(40, 50)
        self.chek_label.resize(300, 20)


        self.number_label = QLabel(self)
        self.number_label.setText(f"Порядковый номер")
        self.number_label.move(40, 70)
        self.number_label.resize(300, 20)


        self.name_label = QLabel(self)
        self.name_label.setText("Введите элемент:  ")
        self.name_label.move(40, 90)



        self.DB_label = Qlabel(self)
        self.


    def hello(self):
        name = self.name_input.text()
        self.label.setText(f"Характеристика: {name}")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM database
                    WHERE name = ? """, (name,)).fetchone()
        if result is not None:
            print(result)
            a = result[1]
            b = result[2]
            self.chek_label.setText(f"Атомная масса: {result[1]}")
            print(self.chek_label.text())
            self.number_label.setText(f"Порядковый номер: {result[2]}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    con = sqlite3.connect("BD/database")
    sys.exit(app.exec())