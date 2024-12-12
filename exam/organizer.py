import os.path

from PySide6 import QtCore, QtWidgets, QtGui

from PySide6.QtWidgets import QApplication, QWidget, QFileSystemModel
from exam.ui.exam_main_form import Ui_Organizer
from exam.ui.exam_saveas_form import Ui_Form


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Organizer()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self) -> None:
        self.ui.actionExit.triggered.connect(QtGui.QGuiApplication.quit)
        self.ui.actionSave_as.triggered.connect(self.showFileSystemWindow)

    def showFileSystemWindow(self):
        dirPath = r'<Your directory>'
        self.demo = SaveAsView(dirPath)
        self.demo.show()


class SaveAsView(QWidget):
    def __init__(self, dir_path):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)

        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(dirPath))

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
        self.filename = self.ui.lineEdit_2.text()
        print(self.pathname)
        print(self.filename)
        with open(os.path.join(self.filePath, self.filename), 'w') as newfile:
            newfile.write(MainWindow.gettext())
        print(os.path.join(self.filePath, self.filename))
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    dirPath = r'<Your directory>'
    window = MainWindow()
    window.show()

    app.exec()