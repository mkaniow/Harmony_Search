import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QTableWidget, QTableWidgetItem, QMessageBox
import HS_algorithm


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Harmony Search'
        self.left = 500
        self.top = 500
        self.width = 580
        self.height = 315
        self.setStyleSheet("background: #6699CC;")
        self.initUI()
        
    def create_label(self, name, x, y):
        label = QLabel(name, self) 
        label.move(x, y)
        return label

    def create_line_edit(self, x, y, height, width):
        line = QLineEdit(self) 
        line.move(x, y)
        line.resize(height, width)
        line.setStyleSheet(
            "background: #FFFFFF;" +
            "border: 1px solid '#008080';" +
            "border-radius: 10px;"
            )
        return line

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.rb2 = QRadioButton("2", self, clicked= lambda: self.create_table(self.rb2))
        self.rb2.setGeometry(15, 10, 100, 30)
  
        self.rb3 = QRadioButton("3", self, clicked= lambda: self.create_table(self.rb3))
        self.rb3.setGeometry(55, 10, 100, 30)

        self.rb4 = QRadioButton("4", self, clicked= lambda: self.create_table(self.rb4))
        self.rb4.setGeometry(95, 10, 100, 30)

        self.rb5 = QRadioButton("5", self, clicked= lambda: self.create_table(self.rb5))
        self.rb5.setGeometry(135, 10, 100, 30)

        self.labelmin = self.create_label('min', 45, 35)
        self.labelmin.hide()

        self.labelmax = self.create_label('max', 105, 35)
        self.labelmax.hide()

        self.label1 = self.create_label('1', 10, 55)
        self.label1.hide()

        self.label2 = self.create_label('2', 10, 80)
        self.label2.hide()

        self.label3 = self.create_label('3', 10, 105)
        self.label3.hide()

        self.label4 = self.create_label('4', 10, 130)
        self.label4.hide()

        self.label5 = self.create_label('5', 10, 155)
        self.label5.hide()

        self.min1 = self.create_line_edit(30, 60, 50, 20)
        self.min1.hide()

        self.min2 = self.create_line_edit(30, 85, 50, 20)
        self.min2.hide()

        self.min3 = self.create_line_edit(30, 110, 50, 20)
        self.min3.hide()

        self.min4 = self.create_line_edit(30, 135, 50, 20)
        self.min4.hide()

        self.min5 = self.create_line_edit(30, 160, 50, 20)
        self.min5.hide()

        self.max1 = self.create_line_edit(90, 60, 50, 20)
        self.max1.hide()

        self.max2 = self.create_line_edit(90, 85, 50, 20)
        self.max2.hide()

        self.max3 = self.create_line_edit(90, 110, 50, 20)
        self.max3.hide()

        self.max4 = self.create_line_edit(90, 135, 50, 20)
        self.max4.hide()

        self.max5 = self.create_line_edit(90, 160, 50, 20)
        self.max5.hide()

        self.label_iteration = self.create_label("Iterations", 10, 180)
        self.iteration = self.create_line_edit(60, 185, 50, 20)

        self.label_HMS = self.create_label("HMS", 10, 205)
        self.HMS = self.create_line_edit(60, 210, 50, 20)

        self.label_HMRC = self.create_label("HMRC", 10, 230)
        self.HMRC = self.create_line_edit(60, 235, 50, 20)

        self.label_PAR = self.create_label("PAR", 10, 255)
        self.PAR = self.create_line_edit(60, 260, 50, 20)

        self.label_R = self.create_label("R", 10, 280)
        self.R = self.create_line_edit(60, 285, 50, 20)

        self.label_function = self.create_label("Function", 370, 10)
        self.function = self.create_line_edit(220, 35, 350, 20)

        self.button = QPushButton('Solve', self)
        self.button.move(470,275)
        self.button.setStyleSheet(
            "background: #FFFFFF;" +
            "border: 1px solid '#008080';" +
            "border-radius: 10px;"
            )
        self.button.clicked.connect(self.on_click)
        self.show()

    def create_table(self, name):
        if name.text() == "2":
            if name.isChecked():
                self.labelmin.show()
                self.labelmax.show()
                self.label1.show()
                self.label2.show()
                self.label3.hide()
                self.label4.hide()
                self.label5.hide()
                self.min1.show()
                self.min2.show()
                self.max1.show()
                self.max2.show()
                self.min3.hide()
                self.max3.hide()
                self.min4.hide()
                self.max4.hide()
                self.min5.hide()
                self.max5.hide()
        if name.text() == "3":
            if name.isChecked():
                self.labelmin.show()
                self.labelmax.show()
                self.label1.show()
                self.label2.show()
                self.label3.show()
                self.label4.hide()
                self.label5.hide()
                self.min1.show()
                self.min2.show()
                self.min3.show()
                self.max1.show()
                self.max2.show()
                self.max3.show()
                self.min4.hide()
                self.max4.hide()
                self.min5.hide()
                self.max5.hide()
        if name.text() == "4":
            if name.isChecked():
                self.labelmin.show()
                self.labelmax.show()
                self.label1.show()
                self.label2.show()
                self.label3.show()
                self.label4.show()
                self.label5.hide()
                self.min1.show()
                self.min2.show()
                self.min3.show()
                self.min4.show()
                self.max1.show()
                self.max2.show()
                self.max3.show()
                self.max4.show()
                self.min5.hide()
                self.max5.hide()
        if name.text() == "5":
            if name.isChecked():
                self.labelmin.show()
                self.labelmax.show()
                self.label1.show()
                self.label2.show()
                self.label3.show()
                self.label4.show()
                self.label5.show()
                self.min1.show()
                self.min2.show()
                self.min3.show()
                self.min4.show()
                self.min5.show()
                self.max1.show()
                self.max2.show()
                self.max3.show()
                self.max4.show()
                self.max5.show()

    def createTable(self, memory):
        self.cords_value = len(memory[0][0])
        self.memory_len_value = len(memory)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.memory_len_value)
        self.tableWidget.setColumnCount(self.cords_value + 1)
        
        label_names = [f'X{i+1}' for i in range(len(memory[0][0]))]
        label_names.append('result')
        
        for i in range(len(memory)):
            for j in range(len(memory[i][0])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(memory[i][0][j])))
        
        for i in range(len(memory)):
            self.tableWidget.setItem(i - 1, len(memory[0][0]) + len(memory[0][0]) + 1, QTableWidgetItem(str(memory[i][1])))
        
        for i in range(len(memory[0][0])):
            self.tableWidget.setHorizontalHeaderLabels(label_names)
        
        self.tableWidget.show()

    def warning(self):
        self.warning_box = QMessageBox()
        self.warning_box.setWindowTitle("WARNING!")
        self.warning_box.setText("Please check your inputs")
        self.warning_box.setIcon(QMessageBox.Warning)
        self.warning_box.exec_()

    def on_click(self):
        try:
            iteration_value = int(self.iteration.text())
            hms_value = int(self.HMS.text())
            hmrc_value = float(self.HMRC.text())
            par_value = float(self.PAR.text())
            r_value = float(self.R.text())
            function_value = self.function.text()
        except:
            self.warning()

        if self.rb2.isChecked():
            try:
                self.solve_for_2 = HS_algorithm.Calculate(iteration_value, hms_value, hmrc_value, par_value, r_value, function_value, 2, int(self.min1.text()), int(self.max1.text()), int(self.min2.text()), int(self.max2.text()))
                self.createTable(self.solve_for_2.memory)
            except:
                self.warning()
        elif self.rb3.isChecked():
            try:
                self.solve_for_3 = HS_algorithm.Calculate(iteration_value, hms_value, hmrc_value, par_value, r_value, function_value, 3, int(self.min1.text()), int(self.max1.text()), int(self.min2.text()), int(self.max2.text()), int(self.min3.text()), int(self.max3.text()))
                self.createTable(self.solve_for_3.memory)
            except:
                self.warning()    
        elif self.rb4.isChecked():
            try:
                self.solve_for_4 = HS_algorithm.Calculate(iteration_value, hms_value, hmrc_value, par_value, r_value, function_value, 4, int(self.min1.text()), int(self.max1.text()), int(self.min2.text()), int(self.max2.text()), int(self.min3.text()), int(self.max3.text()), int(self.min4.text()), int(self.max4.text()))
                self.createTable(self.solve_for_4.memory)
            except:
                self.warning()
        elif self.rb5.isChecked():
            try:
                self.solve_for_5 = HS_algorithm.Calculate(iteration_value, hms_value, hmrc_value, par_value, r_value, function_value, 5, int(self.min1.text()), int(self.max1.text()), int(self.min2.text()), int(self.max2.text()), int(self.min3.text()), int(self.max3.text()), int(self.min4.text()), int(self.max4.text()), int(self.min5.text()), int(self.max5.text()))
                self.createTable(self.solve_for_5.memory)
            except:
                self.warning()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

# for help
# (x1+2*x2-7)^2+(2*x1+x2-5)^2
# (x1)^2+(x2)^2+(x3)^2