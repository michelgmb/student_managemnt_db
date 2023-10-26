from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, \
    QGridLayout, QLineEdit, QPushButton, QComboBox, QMainWindow, QTableWidget, QTableWidgetItem, QDialog
import sys
from datetime import datetime
from PyQt6.QtGui import QAction
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        pass
        super().__init__()
        # menu bar
        self.setWindowTitle("Student Database")
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False) # removing column number
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result   = connection.execute(("SELECT * FROM students"))
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.table.setItem(row_number, colum_number, QTableWidgetItem(str(data)))
        connection.close()


    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        #Add Student Name Widget
        self.student_name  = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add Course combo box
        self.course_name =  QComboBox(self)
        courses = ["Astronomy","Biology", "Math",  "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add Student mobile
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)


        # Add a submit button
        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)



        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile =self.mobile.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO  students (name, course, mobile)VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        mainwindow.load_data()



app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
print(mainwindow.load_data())
sys.exit(app.exec())
