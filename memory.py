from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel)
from random import shuffle, randint
from PyQt5.QtGui import *

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])

btn_OK = QPushButton('Ответить')  # кнопка ответа
btn_OK.setStyleSheet(
    "width: 70px;"
    "height: 30px;"
    "font-size: 20px;"
    "background-color: black;"
    "border: 2px solid white;"
    "color: white;"
);
