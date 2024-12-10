"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
"""
Подключение формы созданной в дизайнере

Команда для конвертации формы:
PySide6-uic path_to_form.ui -o path_to_form.py
"""

import psutil
import requests
import time

from PySide6 import QtCore, QtWidgets
from lab_3.ui.d_many_widgets_and_threads_form import Ui_Form
from lab_3.a_threads import SystemInfo
from lab_3.a_threads import WeatherHandler


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.threadCPURAM.start()

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """

        self.threadCPURAM = SystemInfo()
        self.threadWeatherHandler = WeatherHandler()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButton_3.clicked.connect(self.onPushButtonStart)
        self.ui.pushButton_2.clicked.connect(self.onPushButtonStartCPURAM)
        self.ui.pushButton.clicked.connect(self.onPushButtonStop)
        self.threadCPURAM.systemInfoReceived.connect(self.reportProgress_first)
        self.threadWeatherHandler.first_signal.connect(self.reportProgress_second)

    def onPushButtonStart(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButton

        :return: None
        """
        self.threadWeatherHandler.setstatus(True)
        self.threadWeatherHandler.setDelay(int(self.ui.lineEdit_3.text()))
        self.threadWeatherHandler.setlatlon(float(self.ui.lineEdit.text()), float(self.ui.lineEdit_2.text()))
        self.threadWeatherHandler.start()
        self.ui.lineEdit.setEnabled(False)
        self.ui.lineEdit_2.setEnabled(False)
        self.ui.lineEdit_3.setEnabled(False)

    def onPushButtonStartCPURAM(self) -> None:
        self.threadCPURAM.delay = int(self.ui.lineEdit_3.text())

    def onPushButtonStop(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButton2

        :return: None
        """
        self.threadWeatherHandler.setstatus(False)
        self.ui.textEdit.setText('Thread stopped')
        self.ui.lineEdit.setEnabled(True)
        self.ui.lineEdit_2.setEnabled(True)
        self.ui.lineEdit_3.setEnabled(True)

    def reportProgress_first(self) -> None:
        """
        Приём данных из потока и обработка их в основном цикле приложения

        :param progress: прогресс выполнения функции в потоке
        :return: None
        """

        self.ui.lcdNumber.display(str(psutil.cpu_percent()))
        self.ui.lcdNumber_2.display(str(psutil.virtual_memory().percent))

    def reportProgress_second(self) -> None:
        """
        Приём данных из потока и обработка их в основном цикле приложения

        :param progress: прогресс выполнения функции в потоке
        :return: None
        """
        response = requests.get(self.threadWeatherHandler.api_url)
        data = response.json()
        self.ui.textEdit.setText(f'{data}')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()