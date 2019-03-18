import os
from io import BytesIO

import numpy as np
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap, QPalette
from PyQt5.QtWidgets import QHeaderView, QFileDialog, QMessageBox, QDialog, QLabel
import mainwindow

from methods import Methods
from function import Function
from point import Point
from informationdialog import InformationDialog
from save import Doc

import resources


class ExampleApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.methods = Methods(Function())
        self.model = QStandardItemModel()

        self.initButtons()
        self.res = []

    def initButtons(self):
        self.ButtonCalculate.clicked.connect(self.calculate)

        self.action.setShortcut("Ctrl+S")
        self.action.setStatusTip('Сохранить картинку и таблицу в файл')
        self.action.triggered.connect(self.save_report)
        self.action_3.triggered.connect(self.show_info)
        self.action_4.triggered.connect(self.show_about_author)

    def show_info(self):
        brows = InformationDialog(':/help_docs/', 'index.html', self)
        brows.show()

    def show_about_author(self):
        inf = QDialog(self)
        inf.setWindowModality(QtCore.Qt.ApplicationModal)
        lay = QtWidgets.QHBoxLayout()
        e = QLabel()
        e.setFixedSize(180, 180)
        e.setPixmap(QPixmap(':/icons/me.jpg'))
        c = QLabel("<center><big>Студент: Ковынев М.В.<p>Группа: 6304 - ПИ<p>Почта: "
                   "kovinevmv@gmail.com<p>Git: @kovinevmv</center></big>")
        c.setWordWrap(True)

        lay.addWidget(e)
        lay.addWidget(c)

        inf.setFixedSize(600, 200)
        inf.setWindowTitle('Об авторе')
        inf.setLayout(lay)
        inf.show()

    def init_table(self, headers_, count_rows):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(headers_)
        self.model.setVerticalHeaderLabels([str(i) for i in range(count_rows)])

        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def init_values(self):
        self.methods.set_alpha(self.spinBoxAlpha.value())
        self.methods.set_step_len(self.SpinBoxStepLen.value())
        self.methods.set_step_count(self.SpinBoxStepCount.value())

        self.methods.set_start(Point(self.SpinBoxStartX.value(),
                                     self.SpinBoxStartY.value()))

    def calculate(self):
        self.init_values()
        self.res = self.calc_by_index_of_method(self.ComboBoxMethodName.currentIndex())

        try:
            self.init_table(self.res[0].keys(), len(self.res))
            for i, d in enumerate(self.res):
                for j, (key, value) in enumerate(d.items()):
                    item = QStandardItem(str(value))
                    self.model.setItem(i, j, item)

            self.plot(self.res)
        except:
            pass

    def calc_by_index_of_method(self, index):
        if index == 0:
            return self.methods.gradient_descent_const_step()
        if index == 1:
            return self.methods.gradient_descent_split_step()
        if index == 2:
            return self.methods.gradient_descent_fast()
        if index == 3:
            return self.methods.newton_raphson()
        if index == 4:
            return self.methods.polak_ribiere()
        if index == 5:
            return self.methods.davidon_fletcher_powell()

    def plot(self, res):
        X = np.arange(-5, 10, 0.025)
        Y = np.arange(-5, 20, 0.025)
        levels = np.arange(0.1, 20, 1)
        X, Y = np.meshgrid(X, Y)
        Z = self.methods.function.f(X, Y)

        x = [i['x'] for i in res]
        y = [i['y'] for i in res]

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        ax.set_xlim([-2, 4])
        ax.set_ylim([-2, 8])
        ax.plot(x, y, marker='o', lw=1, color='r')
        ax.contour(X, Y, Z, levels=levels)
        self.canvas.draw()

    def parse_method_name(self, index):
        list_method_names = ['Градиентный метод с постоянным шагом',
                             'Градиентный метод с дроблением шага',
                             'Метод наискорейшего спуска',
                             'Метод Ньютона-Рафсона',
                             'Метод Полака-Рибьера',
                             'Метод Давидона-Флетчера-Пауэлла',
                             'Метод Бройдена-Флетчера-Шенно']

        return list_method_names[index]

    def save_report(self):
        if self.res:
            self.figure.savefig('img.png')
            with open('img.png', 'rb') as f:
                image = BytesIO(f.read())
            os.remove('img.png')

            method_name = self.parse_method_name(self.ComboBoxMethodName.currentIndex())

            d = Doc(image, self.res, method_name)

            from datetime import datetime
            time = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
            output_file = QFileDialog.getSaveFileName(self, "Save as doc", f"{method_name}_{time}.docx",
                                                      'Microsoft Word Docx (*.docx)')

            if len(output_file[0]) == 0:
                return

            d.save(output_file[0])

        else:
            self.create_error_msg('Таблица пуста. Выберите метод и рассчитайте приближение.')

    def create_error_msg(self, msg_text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка в ходе сохранения файла")
        msg.setInformativeText(msg_text)
        msg.setWindowTitle("Ошибка")
        msg.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
