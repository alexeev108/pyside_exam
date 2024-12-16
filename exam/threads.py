import datetime
import time
import psutil
import requests
from PySide6 import QtCore, QtWidgets

class jsontimer(QtCore.QThread):
    first_signal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = 60
        self.status = None

    def setstatus(self, status):
        """
        Метод для смены статуса
        :param status:
        :return:
        """
        self.status = status

    def run(self) -> None:
        while True:
            if self.status == False:
                break
            current_time = time.localtime()
            formatted_time = time.strftime("%d.%m.%Y %H:%M", current_time)
            self.first_signal.emit(formatted_time)
            time.sleep(self.delay)