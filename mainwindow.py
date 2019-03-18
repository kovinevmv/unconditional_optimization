# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QSplitter)
from matplotlib.backends.backend_template import FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.statusBar()
        self.mainMenu = self.menuBar()
        self.saveMenu = self.mainMenu.addMenu('Сохранить результат')

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.labelFormula = QtWidgets.QLabel(self.centralWidget)
        self.labelFormula.setMinimumSize(QtCore.QSize(150, 0))
        self.labelFormula.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelFormula.setObjectName("label")
        self.verticalLayout_2.addWidget(self.labelFormula)

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.spinBoxAlpha = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.spinBoxAlpha.setMinimumSize(QtCore.QSize(120, 0))
        self.spinBoxAlpha.setProperty("value", 1.0)
        self.spinBoxAlpha.setObjectName("spinBoxAlpha")
        self.verticalLayout_2.addWidget(self.spinBoxAlpha)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SpinBoxStartX = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBoxStartX.setProperty("value", 2.0)
        self.SpinBoxStartX.setObjectName("SpinBoxStartX")
        self.SpinBoxStartX.setMinimum(-100.0)
        self.SpinBoxStartX.setMaximum(100.0)
        self.horizontalLayout_3.addWidget(self.SpinBoxStartX)
        self.SpinBoxStartY = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBoxStartY.setMinimum(-100.0)
        self.SpinBoxStartY.setMaximum(100.0)
        self.SpinBoxStartY.setProperty("value", 5.0)
        self.SpinBoxStartY.setObjectName("SpinBoxStartY")
        self.horizontalLayout_3.addWidget(self.SpinBoxStartY)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.SpinBoxStepLen = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBoxStepLen.setSingleStep(0.1)
        self.SpinBoxStepLen.setProperty("value", 0.1)
        self.SpinBoxStepLen.setObjectName("SpinBoxStepLen")
        self.SpinBoxStepLen.setMaximum(10.0)
        self.verticalLayout_5.addWidget(self.SpinBoxStepLen)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.SpinBoxStepCount = QtWidgets.QSpinBox(self.centralWidget)
        self.SpinBoxStepCount.setProperty("value", 10)
        self.SpinBoxStepCount.setObjectName("SpinBoxStepCount")
        self.SpinBoxStepCount.setMaximum(200.0)
        self.verticalLayout_9.addWidget(self.SpinBoxStepCount)
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.ComboBoxMethodName = QtWidgets.QComboBox(self.centralWidget)
        self.ComboBoxMethodName.setObjectName("ComboBoxMethodName")
        self.ComboBoxMethodName.addItem("")
        self.ComboBoxMethodName.addItem("")
        self.ComboBoxMethodName.addItem("")
        self.ComboBoxMethodName.addItem("")
        self.ComboBoxMethodName.addItem("")
        self.verticalLayout_4.addWidget(self.ComboBoxMethodName)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.ButtonCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.ButtonCalculate.setObjectName("ButtonCalculate")
        self.verticalLayout_10.addWidget(self.ButtonCalculate)
        self.verticalLayout.addLayout(self.verticalLayout_10)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tableView = QtWidgets.QTableView(self.centralWidget)
        self.tableView.setMinimumSize(QtCore.QSize(400, 400))
        self.tableView.setObjectName("tableView")

        self.figure = plt.figure()
        self.figure.set_facecolor("none")
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.widgetPlot = QtWidgets.QWidget()
        self.widgetPlot.setMinimumSize(QtCore.QSize(400, 400))
        layout = QtWidgets.QVBoxLayout()
        self.widgetPlot.setLayout(layout)

        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.tableView)
        self.splitter.addWidget(self.widgetPlot)

        self.horizontalLayout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1093, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)

        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)


        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu_2.addAction(self.action_3)

        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu_2.addAction(self.action_4)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.ComboBoxMethodName.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Безусловная оптимизация"))
        MainWindow.setWindowIcon(QtGui.QIcon(':/icons/ico.png'))
        self.labelFormula.setText(_translate("MainWindow", "f(x,y)=(y-x^2)^2+a(x-1)^2"))
        self.label.setText(_translate("MainWindow", "Введите коэффициент a:"))
        self.label_2.setText(_translate("MainWindow", "Начальная точка:"))
        self.label_3.setText(_translate("MainWindow", "Длина шага:"))
        self.label_4.setText(_translate("MainWindow", "Количество шагов:"))
        self.label_5.setText(_translate("MainWindow", "Метод:"))
        self.ComboBoxMethodName.setItemText(0, _translate("MainWindow", "Град. с постоянным шагом"))
        self.ComboBoxMethodName.setItemText(1, _translate("MainWindow", "Град. с дроблением шага"))
        self.ComboBoxMethodName.setItemText(2, _translate("MainWindow", "Наискорейшего спуска"))
        self.ComboBoxMethodName.setItemText(3, _translate("MainWindow", "Ньютона-Рафсона"))
        self.ComboBoxMethodName.setItemText(4, _translate("MainWindow", "Полака-Рибьера"))
        self.ButtonCalculate.setText(_translate("MainWindow", "Рассчет"))

        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "Сохранить отчет в формате .docx"))
        self.action_3.setText(_translate("MainWindow", "О программе"))
        self.action_3.setShortcut(_translate("MainWindow", "F1"))
        self.action_4.setText(_translate("MainWindow", "Об авторе"))
