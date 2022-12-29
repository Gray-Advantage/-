from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from AddEditCoffeeForm import Ui_DialogWindow
from MainForm import Ui_MainWindow
from sqlite3 import connect
from sys import argv, exit


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.dialog = None
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)

        self.add_button.clicked.connect(self.add_new_coffee)
        self.change_button.clicked.connect(self.change_coffee_in_focus)

        self.change_button.setEnabled(False)
        self.table_widget.currentItemChanged.connect(lambda: self.change_button.setEnabled(True))

        self.update_table()

    def update_table(self):
        with connect("data/coffee.sqlite") as db:
            res = db.cursor().execute("SELECT * FROM coffee").fetchall()

        title = ["id", "Название сорта", "Степень прожарки", "Молотый/Зёрна",
                 "Описание вкуса", "Цена", "Объём упаковки"]

        self.table_widget.setRowCount(len(res))
        self.table_widget.setColumnCount(len(res[0]))
        self.table_widget.setHorizontalHeaderLabels(title)

        for i, (id_product, name, roasting, is_ground, taste, price, volume) in enumerate(res):
            self.table_widget.setItem(i, 0, QTableWidgetItem(str(id_product)))
            self.table_widget.setItem(i, 1, QTableWidgetItem(name))
            self.table_widget.setItem(i, 2, QTableWidgetItem(str(roasting)))
            self.table_widget.setItem(i, 3, QTableWidgetItem("Молотый" if is_ground else "В зёрнах"))
            self.table_widget.setItem(i, 4, QTableWidgetItem(taste))
            self.table_widget.setItem(i, 5, QTableWidgetItem(str(price)))
            self.table_widget.setItem(i, 6, QTableWidgetItem(str(volume)))

    def add_new_coffee(self):
        self.dialog = Dialog(self)
        self.dialog.show()

    def change_coffee_in_focus(self):
        res = [self.table_widget.item(self.table_widget.currentRow(), i).text() for i in range(7)]
        self.dialog = Dialog(self, res)
        self.dialog.show()

    def add_or_change_coffee(self, add_mode, info):
        if add_mode:
            with connect("data/coffee.sqlite") as db:
                db.cursor().execute("INSERT INTO coffee(grade, degree_roasting, is_ground, "
                                    "taste_description, price, packing_volume) "
                                    f"VALUES('{info[0]}', {info[1]}, {int(info[2])}, '{info[3]}',"
                                    f" {info[4]}, {info[5]})")
        else:
            with connect("data/coffee.sqlite") as db:
                db.cursor().execute(f"UPDATE coffee "
                                    f"SET grade = '{info[1]}', "
                                    f"degree_roasting = {info[2]}, "
                                    f"is_ground = {int(info[3])}, "
                                    f"taste_description = '{info[4]}', "
                                    f"price = {info[5]}, "
                                    f"packing_volume = {info[6]} "
                                    f"WHERE id = {info[0]}")
        self.update_table()


class Dialog(QMainWindow, Ui_DialogWindow):
    def __init__(self, parent, info=None):
        super().__init__()
        self.parent = parent
        self.info = info
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.name.textChanged.connect(self.check_name)
        self.description.textChanged.connect(self.check_description)
        self.is_ground.stateChanged.connect(self.change_mode_in_ground)
        self.ok_button.clicked.connect(self.save_changed)

        self.check_name()

        if self.info is None:
            self.setWindowTitle("Добавить кофе")
            self.ok_button.setText("Добавить")
        else:
            self.setWindowTitle("Изменить кофе")
            self.ok_button.setText("Изменить")
            self.name.setText(self.info[1])
            self.degree_roasting.setValue(int(self.info[2]))
            self.is_ground.setChecked(self.info[3] == "Молотый")
            self.description.setText(self.info[4])
            self.price.setValue(float(self.info[5]))
            self.packing_volume.setValue(int(self.info[6]))

    def change_mode_in_ground(self):
        if self.is_ground.isChecked():
            self.is_ground.setText("Да")
        else:
            self.is_ground.setText("Нет")

    def check_name(self):
        self.ok_button.setEnabled(True)
        if self.name.text() == "" or self.description.text() == "":
            self.ok_button.setEnabled(False)

    def check_description(self):
        self.ok_button.setEnabled(True)
        if self.description.text() == "" or self.name.text() == "":
            self.ok_button.setEnabled(False)

    def save_changed(self):
        add_mode = self.info is None
        res = [self.name.text(), self.degree_roasting.value(), self.is_ground.isChecked(),
               self.description.text(), self.price.value(), self.packing_volume.value()]
        if not add_mode:
            res = [self.info[0]] + res
        self.parent.add_or_change_coffee(add_mode, res)
        self.destroy()


if __name__ == '__main__':
    app = QApplication(argv)
    window = Window()
    window.show()
    exit(app.exec())
