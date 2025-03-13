#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class SquareApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # set up window
        self.setWindowTitle('Square Number Calculator')
        self.setGeometry(300, 300, 300, 150)
        
        layout = QVBoxLayout()
        
        # widgets
        self.label = QLabel('Enter a number:')
        self.input = QLineEdit()
        self.button = QPushButton('Calculate Square')
        self.result = QLabel('')

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        self.setLayout(layout)
        
        # Connect button to function
        self.button.clicked.connect(self.calculate_square)
        
    def calculate_square(self):
        try:
            num = float(self.input.text())
            square = num ** 2
            self.result.setText(f"The square of {num} is {square}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid number")

def main():
    app = QApplication(sys.argv)
    ex = SquareApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
