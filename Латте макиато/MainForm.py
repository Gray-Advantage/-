# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.add_button = QtWidgets.QPushButton(self.central_widget)
        self.add_button.setObjectName("add_button")
        self.horizontal_layout.addWidget(self.add_button)
        self.change_button = QtWidgets.QPushButton(self.central_widget)
        self.change_button.setObjectName("change_button")
        self.horizontal_layout.addWidget(self.change_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontal_layout)
        self.table_widget = QtWidgets.QTableWidget(self.central_widget)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(0)
        self.table_widget.setRowCount(0)
        self.verticalLayout.addWidget(self.table_widget)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Латте макиато"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.change_button.setText(_translate("MainWindow", "Изменить"))
