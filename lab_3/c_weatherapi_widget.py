"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""

"""
Подключение формы созданной в дизайнере

Команда для конвертации формы:
PySide6-uic path_to_form.ui -o path_to_form.py
"""

import requests
from PySide6 import QtCore, QtWidgets
from lab_3.ui.c_weatherapi_widget_form import Ui_Form
from lab_3.a_threads import WeatherHandler

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """
        self.thread = WeatherHandler()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButton.clicked.connect(self.onPushButtonStart)
        self.thread.started.connect(lambda: print("Thread started"))
        self.thread.first_signal.connect(self.reportProgress)
        self.ui.pushButton_2.clicked.connect(self.onPushButtonStop)

    def onPushButtonStart(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButton

        :return: None
        """
        self.thread.setstatus(True)
        self.thread.setDelay(int(self.ui.lineEdit_3.text()))
        self.thread.setlatlon(float(self.ui.lineEdit.text()), float(self.ui.lineEdit_2.text()))
        self.thread.start()
        self.ui.lineEdit.setEnabled(False)
        self.ui.lineEdit_2.setEnabled(False)
        self.ui.lineEdit_3.setEnabled(False)

    def onPushButtonStop(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButton2

        :return: None
        """
        self.thread.setstatus(False)
        print("Thread stopped")
        self.ui.textEdit.setText('Thread stopped')
        self.ui.lineEdit.setEnabled(True)
        self.ui.lineEdit_2.setEnabled(True)
        self.ui.lineEdit_3.setEnabled(True)

    def reportProgress(self) -> None:
        """
        Приём данных из потока и обработка их в основном цикле приложения

        :param progress: прогресс выполнения функции в потоке
        :return: None
        """
        response = requests.get(self.thread.api_url)
        data = response.json()
        self.ui.textEdit.setText(f'{data}')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()