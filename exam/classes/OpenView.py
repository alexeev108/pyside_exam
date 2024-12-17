from PySide6.QtWidgets import QWidget, QFileSystemModel

from exam.ui.exam_open_form import Ui_Form as Ui_FormOpen

DIRPATH = r'<Your directory>'

class OpenView(QWidget):
    def __init__(self, dir_path):
        super().__init__()
        self.ui = Ui_FormOpen()
        self.ui.setupUi(self)
        self.initSignals()


        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)

        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(DIRPATH))

        self.ui.treeView.clicked.connect(self.on_treeView_clicked)

    def initSignals(self):
        """
        Инициализация сигналов
        :return:
        """
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.openButtonClick)

    def on_treeView_clicked(self, index):
        """
        Отображение пути к файлу в lineEdit
        :param index:
        :return:
        """
        self.indexItem = self.model.index(index.row(), 0, index.parent())
        self.filePath = self.model.filePath(self.indexItem)
        self.ui.lineEdit.setText(self.filePath)

    def openButtonClick(self):
        """
        Открывает выбранный файл и читает из него данные
        :return:
        """
        self.pathname = self.ui.lineEdit.text()
        print(self.pathname)
        with open(self.pathname, "r", encoding='utf-8') as my_file:
            file_contents = my_file.read()
        print(file_contents)

        self.close()