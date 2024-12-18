import datetime
import json
import os

from PySide6 import QtWidgets, QtGui, QtCore
from exam.classes.ItemView import ItemView
from exam.classes.OpenView import OpenView
from exam.classes.SaveAsView import SaveAsView
from ui.exam_main_form import Ui_Organizer
from exam.threads import jsontimer

DIRPATH = r'<Your directory>'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initThreads()
        self.ui = Ui_Organizer()
        self.ui.setupUi(self)
        self.initSignals()
        self.ui.dateTimeEdit.setMinimumDateTime(datetime.datetime.now())
        self.timeto()

    def initThreads(self):
        """
        Инициализация потоков
        :return: None
        """
        self.thread_1 = jsontimer()
        self.thread_2 = jsontimer()

    def initSignals(self):
        """
        Инициализация сигналов
        :return: None
        """
        self.ui.actionOpen.triggered.connect(self.showOpenWindow)
        self.ui.actionSave_as.triggered.connect(self.showSaveAsWindow)
        self.ui.actionExit.triggered.connect(QtGui.QGuiApplication.quit)
        self.ui.pushButton.clicked.connect(self.showItemWindow)
        self.ui.pushButton_2.clicked.connect(self.tojson)
        self.ui.pushButton_3.clicked.connect(self.deleteitem)
        self.thread_1.first_signal.connect(self.tojson)
        self.thread_2.first_signal.connect(self.timeto)

    def load_data(self):
        """
        Открывает data.json в режиме Чтение
        :return:
        """
        try:
            with open('data.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self, data):
        """
        Записывает в файл data.json
        :param data:
        :return:
        """
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def showSaveAsWindow(self):
        """
        Вызов окна "Сохранить как"
        :return:
        """
        self.saveaswindow = SaveAsView(DIRPATH, self.ui.textEdit.toPlainText(), self.ui.dateTimeEdit.text())
        self.saveaswindow.show()

    def showOpenWindow(self):
        """
        Вызов окна "Открыть"
        :return:
        """
        self.openwindow = OpenView(DIRPATH)
        self.openwindow.show()

    def showItemWindow(self):
        """
        Вызов окна конкретной задачи при нажатии на задачу
        :return:
        """
        current_item = self.ui.listWidget.currentItem().text()
        task_name = current_item.split(':')[0]
        data = self.load_data()
        notes = data.get(task_name, {}).get('notes')
        deadline = data.get(task_name, {}).get('deadline')
        self.itemwindow = ItemView(notes, deadline, task_name)
        self.itemwindow.show()

    def tojson(self):
        """
        Функция добавляет в файл data.json текст задачи и установленный срок по задаче.
        Также, выводит в список задач добавленную.
        :return:
        """
        self.thread_1.setstatus(True)
        self.thread_1.start()

        data = self.load_data()
        task_name = self.ui.lineEdit.text()
        notes = self.ui.textEdit.toPlainText()
        deadline_to_json = self.ui.dateTimeEdit.text()
        deadline_new = datetime.datetime.strptime(deadline_to_json, '%d.%m.%Y %H:%M')
        now = datetime.datetime.now()

        time_left = deadline_new - now

        data[task_name] = {'notes': notes, 'deadline': deadline_to_json, 'time_left': str(time_left)[:-10]}
        self.save_data(data)

        self.update_list_widget()
        self.thread_1.setstatus(False)

    def deleteitem(self):
        """
        Функция удаляет задачу из списка задач и из data.json
        :return:
        """
        current_item = self.ui.listWidget.currentItem().text()
        task_name = current_item.split(':')[0]
        data = self.load_data()
        del data[task_name]
        self.save_data(data)
        self.update_list_widget()
        return task_name

    def timeto(self):
        """
        Вывод актуального оставшегося времени до дэдлайна в listwidget
        при открытии приложения
        :return:
        """
        self.thread_2.setstatus(True)
        self.thread_2.start()

        data = self.load_data()
        now = datetime.datetime.now()

        for task_name, task_data in data.items():
            deadline = datetime.datetime.strptime(task_data['deadline'], '%d.%m.%Y %H:%M')
            time_left = deadline - now
            data[task_name]['time_left'] = str(time_left)[:-10]

        self.save_data(data)
        self.update_list_widget()
        self.thread_2.setstatus(False)

    def update_list_widget(self):
        """
        Обновляет данные в listwidget
        :return:
        """
        self.ui.listWidget.clear()
        data = self.load_data()
        for task_name, task_data in data.items():
            self.ui.listWidget.addItem(f"{task_name}: со сроком выполнения: {task_data['deadline']}.\n"
                                       f"Осталось до срока выполнения: {task_data.get('time_left', '')}")


if __name__ == "__main__":
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as f:
            json.dump({}, f, indent=4)

    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()

    app.exec()