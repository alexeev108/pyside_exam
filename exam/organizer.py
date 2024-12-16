import datetime
import json
import os.path
import re

from PySide6 import QtWidgets, QtGui

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
        :return:
        """

        self.ui.actionOpen.triggered.connect(self.showOpenWindow)
        self.ui.actionSave_as.triggered.connect(self.showSaveAsWindow)
        self.ui.actionExit.triggered.connect(QtGui.QGuiApplication.quit)
        self.ui.pushButton.clicked.connect(self.showItemWindow)
        self.ui.pushButton_2.clicked.connect(self.tojson)
        self.ui.pushButton_3.clicked.connect(self.deleteitem)

        self.thread_1.first_signal.connect(self.tojson)
        self.thread_2.first_signal.connect(self.timeto)
        # self.thread_1.started.connect(lambda: print("Thread_1 started"))
        # self.thread_1.started.connect(lambda: print("Thread_2 started"))

    def showSaveAsWindow(self):
        """
        Вызов окна "Сохранить как"
        :return:
        """
        self.saveaswindow = SaveAsView(DIRPATH, self.get_text_notes(), self.getdeadline())
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
        self.itemwindow = ItemView(self.get_item_notes(), self.get_item_deadline())
        self.itemwindow.show()

    def get_text_notes(self):
        """
        Функция получает текст задачи
        :return:
        """
        return self.ui.textEdit.toPlainText()

    def getdeadline(self):
        """
        Функция получает срок задачи
        :return:
        """
        return self.ui.dateTimeEdit.text()

    def tojson(self):
        """
        Функция добавляет в файл data.json текст задачи и установленный срок по задаче
        :return:
        """
        self.thread_1.setstatus(True)
        self.thread_1.start()
        with open('data.json', encoding='utf-8') as file:
            new = json.load(file)
            x = self.ui.dateTimeEdit.dateTime().toPython() - datetime.datetime.now()
            y = str(x)[:-10]
            new[f'{self.getdeadline()}'] = [self.get_text_notes(), y]
        with open('data.json', 'w', encoding='utf-8') as file_new:
            json.dump(new, file_new, ensure_ascii=False, indent=4)

        self.ui.listWidget.clear()
        for item in new:
            x = new.get(f'{item}')
            self.ui.listWidget.addItem(f'Задача со сроком выполнения: {item}.\n'
                                       f'Осталось до срока выполнения: {x[1]}')
        self.thread_1.setstatus(False)

    def openitem(self):
        """
        Из поля с задачами выделяет установленный срок
        :return:
        """
        current_item = self.ui.listWidget.currentItem().text()
        regular_item = re.search(r'\d{2}\.\d{2}\.\d{4} \d:\d{2}', current_item).group()
        return regular_item

    def get_item_notes(self):
        self.item_notes = self.openitem()
        with open('data.json', encoding='utf-8') as file:
            new = json.load(file)
            for item in new:
                if item == self.item_notes:
                    x = new.get(f'{item}')
                    y = x[0]
        return y

    def get_item_deadline(self):
        self.item_notes = self.openitem()
        with open('data.json', encoding='utf-8') as file:
            new = json.load(file)
            for item in new:
                if item == self.item_notes:
                    return item

    def deleteitem(self):
        current_item = self.ui.listWidget.currentItem().text()
        regular_item = re.search(r'\d{2}\.\d{2}\.\d{4} \d:\d{2}', current_item).group()
        with open('data.json', encoding='utf-8') as file:
            new = json.load(file)
            for item in new:
                if item == regular_item:
                    del new[f'{regular_item}']
                    break
        with open('data.json', 'w', encoding='utf-8') as file_new:
            json.dump(new, file_new, ensure_ascii=False, indent=4)

        self.ui.listWidget.clear()
        self.timeto()

    def timeto(self):
        self.thread_2.setstatus(True)
        self.thread_2.start()
        with open('data.json', encoding='utf-8') as file:
            new = json.load(file)
            if len(new) == 0:
                self.ui.listWidget.clear()
            for item in new:
                new_datetime = datetime.datetime.strptime(item, '%d.%m.%Y %H:%M')
                x = new_datetime - datetime.datetime.now()
                y = str(x)[:-10]
                new[f'{item}'][1] = y

            with open('data.json', 'w', encoding='utf-8') as file_new:
                json.dump(new, file_new, ensure_ascii=False, indent=4)

            self.ui.listWidget.clear()
            for item in new:
                x = new.get(f'{item}')
                self.ui.listWidget.addItem(f'Задача со сроком выполнения: {item}.\n'
                                           f'Осталось до срока выполнения: {x[1]}')


if __name__ == "__main__":
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as f:
            json.dump({}, f, indent=4)

    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()

    app.exec()