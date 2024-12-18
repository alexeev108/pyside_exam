import json

from PySide6.QtWidgets import QWidget

from exam.ui.exam_item_form import Ui_Form as Ui_ItemOpen

class ItemView(QWidget):
    def __init__(self, text_notes, deadline, task_name):
        super().__init__()
        self.text_notes = text_notes
        self.deadline = deadline
        self.task_name = task_name
        self.ui = Ui_ItemOpen()
        self.ui.setupUi(self)
        self.initSignals()

        self.ui.textEdit.setText(self.text_notes)
        self.ui.lineEdit.setText(self.deadline)

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return:
        """
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.text_change)

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

    def text_change(self):
        """
        Функция заменяет текст в data.json на введенный в textEdit
        :return:
        """
        data = self.load_data()
        data[self.task_name]['notes'] = self.ui.textEdit.toPlainText()

        self.save_data(data)
