"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore, QtGui

from lab_2.ui.d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

        self.settings = QtCore.QSettings("NumberSettings")  # Создание объекта QSettings для хранения настроек

        self.ui.comboBox.addItem('oct')
        self.ui.comboBox.addItem('hex')
        self.ui.comboBox.addItem('bin')
        self.ui.comboBox.addItem('dec')

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """
        self.ui.dial.valueChanged.connect(self.changeDial)
        self.ui.horizontalSlider.valueChanged.connect(self.changeSlider)
        self.ui.comboBox.textActivated.connect(self.changeCombobox)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Событие нажатия на клавиатуру

        :param event: QtGui.QKeyEvent
        :return: None
        """
        if event.text() == '+':
            self.ui.dial.setValue(self.ui.dial.value() + 1)
        elif event.text() == '-':
            self.ui.dial.setValue(self.ui.dial.value() - 1)

    def changeDial(self) -> None:
        """
        Обработка сигнала при изменении dial
        :return: None
        """
        self.ui.horizontalSlider.setValue(self.ui.dial.value())
        self.ui.lcdNumber.display(self.ui.dial.value())
        print(f'Новое значение: {self.ui.dial.value()}')

    def changeSlider(self) -> None:
        """
        Обработка сигнала при изменении slider
        :return: None
        """
        self.ui.dial.setValue(self.ui.horizontalSlider.value())
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())

    def changeCombobox(self):
        if self.ui.comboBox.currentText() == 'oct':
            self.new = oct(self.ui.dial.value())
            self.ui.lcdNumber.display(self.new)
        elif self.ui.comboBox.currentText() == 'hex':
            self.new = hex(self.ui.dial.value())
            self.ui.lcdNumber.display(self.new)
        elif self.ui.comboBox.currentText() == 'bin':
            self.new = bin(self.ui.dial.value())
            self.ui.lcdNumber.display(self.new)
        elif self.ui.comboBox.currentText() == 'dec':
            self.new = int(self.ui.dial.value())
            self.ui.lcdNumber.display(self.new)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        if self.ui.comboBox.textActivated:
            self.settings.setValue("comboBox_value", self.ui.comboBox.currentText())
            self.settings.setValue("lcdNumber_value", self.ui.dial.value())
            QtWidgets.QMessageBox.about(self, "Путь", self.settings.fileName())

    def showSettingsPath(self) -> None:
        """
        Показ пути хранения настроек

        :return: None
        """

        QtWidgets.QMessageBox.about(self, "Путь", self.settings.fileName())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
