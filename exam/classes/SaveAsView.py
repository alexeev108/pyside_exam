import os.path
from PySide6.QtWidgets import QWidget, QFileSystemModel

from exam.ui.exam_saveas_form import Ui_Form as Ui_FormSaveAs

DIRPATH = r'<Your directory>'

class SaveAsView(QWidget):
    def __init__(self, dir_path, text_notes, deadline):
        super().__init__()
        self.text_notes = text_notes
        self.deadline = deadline
        self.ui = Ui_FormSaveAs()
        self.ui.setupUi(self)
        self.initSignals()

        self.ui.comboBox.addItem('.txt')

        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)

        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(DIRPATH))

        self.ui.treeView.clicked.connect(self.on_treeView_clicked)

    def initSignals(self) -> None:
        self.ui.pushButton.clicked.connect(self.saveButtonClick)
        self.ui.pushButton_2.clicked.connect(self.close)

    def on_treeView_clicked(self, index):
        self.indexItem = self.model.index(index.row(), 0, index.parent())
        self.filePath = self.model.filePath(self.indexItem)
        self.ui.lineEdit.setText(self.filePath)

    def saveButtonClick(self):
        self.pathname = self.ui.lineEdit.text()
        self.filename = self.ui.lineEdit_2.text() + self.ui.comboBox.currentText()

        with open(os.path.join(self.filePath, self.filename), 'w', encoding='UTF-8') as newfile:
            newfile.write(f'Текст задачи: {self.text_notes}\n\n'
                          f'Установленный срок выполнения по задаче: {self.deadline}')

        self.close()