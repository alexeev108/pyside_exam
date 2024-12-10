"""
Модуль в котором содержаться потоки Qt
"""

import time

import psutil
import requests
from PySide6 import QtCore, QtWidgets


class SystemInfo(QtCore.QThread):
    systemInfoReceived =QtCore.Signal(list)  # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None  # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def run(self) -> None:  # TODO переопределить метод run
        if self.delay is None:  # TODO Если задержка не передана в поток перед его запуском
            self.delay = 1  # TODO то устанавливайте значение 1

        while True:  # TODO Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory().percent  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            self.systemInfoReceived.emit([cpu_value, ram_value])  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay


class WeatherHandler(QtCore.QThread):
    first_signal = QtCore.Signal(dict)
    # TODO Пропишите сигналы, которые считаете нужными

    def __init__(self, parent=None):
        super().__init__(parent)
        self.lat = None
        self.lon = None
        self.api_url = \
            f"https://api.open-meteo.com/v1/forecast?latitude={self.lat}&longitude={self.lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def setlatlon(self, lat, lon) -> None:
        """
        Метод для установки lat, lon, api_url

        :param
        :return: None
        """

        self.lat = lat
        self.lon = lon
        self.api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    def setstatus(self, status):
        """
        Метод для смены статуса
        :param status:
        :return:
        """
        self.__status = status


    def run(self) -> None:
        # TODO настройте метод для корректной работы
        if self.__status == True:
            while self.__status:
                # TODO Примерный код ниже

                response = requests.get(self.api_url)
                data = response.json()
                self.first_signal.emit(data)
                time.sleep(self.__delay)

