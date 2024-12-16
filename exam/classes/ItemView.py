import json

from PySide6.QtWidgets import QWidget

from exam.ui.exam_item_form import Ui_Form as Ui_ItemOpen

class ItemView(QWidget):
    def __init__(self, text_notes, deadline):
        super().__init__()
        self.text_notes = text_notes
        self.deadline = deadline
        self.ui = Ui_ItemOpen()
        self.ui.setupUi(self)
        self.initSignals()

        self.ui.textEdit.setText(self.text_notes)
        self.ui.lineEdit.setText(self.deadline)

    def initSignals(self) -> None:
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.text_change)

    def text_change(self):
        with open('data.json', encoding='utf-8') as file:
            new = json.load(file)
            for item in new:
                if item == self.deadline:
                    new[f'{item}'][0] = self.ui.textEdit.toPlainText()
        with open('data.json', 'w', encoding='utf-8') as file_new:
            json.dump(new, file_new, ensure_ascii=False, indent=4)