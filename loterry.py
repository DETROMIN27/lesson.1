from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QWidget 
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
win = QWidget ()
win.resize (500,400)
win.move (200, 200)
win.setWindowTitle("Loterey")

main_l = QHBoxLayout()

lbl_mes = QLabel("Press to start")
lbl_num1 = QLabel ("'")
lbl_num2 = QLabel("?")
btn = QPushButton("Start")

main_l.addWidget (lbl_mes, alignment=Qt.AlignCenter) 
main_l.addWidget (lbl_num1, alignment=Qt.AlignCenter) 
main_l.addWidget (lbl_num2, alignment=Qt.AlignCenter) 
main_l.addWidget (btn, alignment=Qt.AlignCenter)


def start():
    num1 = randint(0,9)
    num2 = randint (0,9)
    lbl_num1. setText (str (num1))
    lbl_num2. setText (str (num2))
    if num1==num2:
        lbl_mes. setText ("Win!!!")
    else:
        lbl_mes.setText("Try again!")

win.setLayout (main_l)
win.show()
app.exec()

