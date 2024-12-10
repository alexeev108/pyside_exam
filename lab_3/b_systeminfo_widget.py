"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""


"""
Подключение формы созданной в дизайнере

Команда для конвертации формы:
PySide6-uic path_to_form.ui -o path_to_form.py
"""

import psutil
from PySide6 import QtCore, QtWidgets
from lab_3.ui.b_systeminfo_widget_form import Ui_Form
from lab_3.a_threads import SystemInfo


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.thread.start()

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """

        self.thread = SystemInfo()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.ui.pushButton.clicked.connect(self.onPushButton)
        self.thread.started.connect(lambda: print("Thread started"))
        self.thread.systemInfoReceived.connect(self.reportProgress)

    def onPushButton(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButton

        :return: None
        """

        self.thread.delay = int(self.ui.lineEdit.text())

    def reportProgress(self) -> None:
        """
        Приём данных из потока и обработка их в основном цикле приложения

        :param progress: прогресс выполнения функции в потоке
        :return: None
        """

        self.ui.lcdNumber.display(str(psutil.cpu_percent()))
        self.ui.lcdNumber_2.display(str(psutil.virtual_memory().percent))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()