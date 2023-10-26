from PyQt6.QtWidgets import QApplication, QLabel, QWidget, \
    QGridLayout, QLineEdit, QPushButton, QComboBox
import sys
from datetime import datetime


class Speed_Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()
        # creating a label widget

        self.distance = QLabel("Distance")
        self.distance_line_edit = QLineEdit()
        self.combo_box = QComboBox(self)
        # adding list of items to combo box
        self.combo_box.addItems(['Metric(km)', 'Mertric(m)'])
        self.time = QLabel("Time(Hours)")
        self.time_line_edit = QLineEdit()
        push_button = QPushButton("Calculate")
        push_button.clicked.connect(self.calculate)

        self.output_label = QLabel("")

        grid.addWidget(self.distance, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo_box, 0, 2)
        grid.addWidget(self.time, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(push_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        measurement = self.combo_box.currentText()
        if measurement == 'Metric(km)':
            distance = int(self.distance_line_edit.text())
            time_s = int(self.time_line_edit.text())
            speed = distance / time_s
            self.output_label.setText(f"{distance} per {time_s}  is {speed} km/H")
        else:
            distance = int(self.distance_line_edit.text())
            time_s = int(self.time_line_edit.text())
            speed = distance / time_s
            self.output_label.setText(f"{distance} per {time_s}  is {speed} m/H")



app = QApplication(sys.argv)
speed_calculator = Speed_Calculator()
speed_calculator.show()
sys.exit(app.exec())
