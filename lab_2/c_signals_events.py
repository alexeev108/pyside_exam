"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

"""
Подключение формы созданной в дизайнере

Команда для конвертации формы:
PySide6-uic path_to_form.ui -o path_to_form.py
"""

from PySide6 import QtWidgets, QtGui, QtCore

from lab_2.ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создание "прокси" переменной для работы с формой
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

        self.x_screen = int(QtGui.QScreen.geometry(self.screen()).width())
        self.x_window = int(QtWidgets.QWidget.geometry(self.window()).width())
        self.y_screen = int(QtGui.QScreen.geometry(self.screen()).height())
        self.y_window = int(QtWidgets.QWidget.geometry(self.window()).height())



    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLT)
        self.ui.pushButtonRT.clicked.connect(self.onPushButtonRT)
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonCenter)
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLB)
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonRB)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoords)
        self.ui.pushButtonGetData.clicked.connect(self.screenParam)

    # slots --------------------------------------------------------------

    def onPushButtonLT(self) -> None:
        """
        Обработка сигнала clicked для кнопки PushButtonLT

        :return: Non
        """
        self.move(0, 0)

    def onPushButtonRT(self) -> None:
        """
        Обработка сигнала clicked для кнопки PushButtonRT
        :return: Non
        """
        self.move(self.x_screen - self.x_window, 0)

    def onPushButtonCenter(self) -> None:
        """
        Обработка сигнала clicked для кнопки PushButtonCenter
        :return: Non
        """
        self.move(self.x_screen / 2 - self.x_window / 2, self.y_screen / 2 - self.y_window / 2)

    def onPushButtonLB(self) -> None:
        """
        Обработка сигнала clicked для кнопки PushButtonLB
        :return: Non
        """
        self.move(0, self.y_screen - self.y_window)

    def onPushButtonRB(self) -> None:
        """
        Обработка сигнала clicked для кнопки PushButtonLB
        :return: Non
        """
        self.move(self.x_screen - self.x_window, self.y_screen - self.y_window)

    def onPushButtonMoveCoords(self) -> None:
        """
        Обработка сигнала clicked для кнопки PushButtonMoveCoords

        :return: None
        """
        self.move(int(self.ui.spinBoxX.text()), int(self.ui.spinBoxY.text()))

    def screenParam(self):
        self.param = (f'Время: {QtCore.QTime.currentTime().toString()}\n\n'
                      f'Кол-во экранов: {QtGui.QGuiApplication.screens().count(self.screen())}\n'
                      f'Текущее основное окно: {QtWidgets.QApplication.activeWindow().objectName()}\n'
                      f'Разрешение экрана: {QtGui.QScreen.geometry(self.screen()).height()} x'
                      f' {QtGui.QScreen.geometry(self.screen()).width()}\n'
                      f'Основное окно находится на экране с именем '
                      f'{QtWidgets.QApplication.activeWindow().screen().name()}\n'
                      f'Размеры окна {QtWidgets.QApplication.activeWindow().objectName()}: '
                      f'{QtWidgets.QApplication.activeWindow().height()} x '
                      f'{QtWidgets.QApplication.activeWindow().width()}\n'
                      f'Минимальные размеры окна {QtWidgets.QApplication.activeWindow().objectName()}: '
                      f'{QtWidgets.QApplication.activeWindow().minimumHeight()} x '
                      f'{QtWidgets.QApplication.activeWindow().minimumWidth()}\n'
                      f'Текущие координаты окна {QtWidgets.QApplication.activeWindow().objectName()}: '
                      f'({QtWidgets.QApplication.activeWindow().x()}, {QtWidgets.QApplication.activeWindow().y()})\n'
                      f'Текущие координаты центра окна {QtWidgets.QApplication.activeWindow().objectName()}: '
                      f'({(QtWidgets.QApplication.activeWindow().x() + 
                           QtWidgets.QApplication.activeWindow().width()) / 2}, '
                      f'{(QtWidgets.QApplication.activeWindow().y() + 
                           QtWidgets.QApplication.activeWindow().height()) / 2})\n'
                      f'Окно свернуто: {QtWidgets.QWidget.isMinimized(self.window())}\n'
                      f'Окно развернуто: {QtWidgets.QWidget.isMaximized(self.window())}\n'
                      f'Окно активно: {QtWidgets.QWidget.isActiveWindow(self.window())}\n'
                      f'Окно отображено: {QtWidgets.QWidget.windowState(self.window())}')
        self.ui.plainTextEdit.setPlainText(self.param)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Событие изменения положения окна

        :param event: QtGui.QMoveEvent
        :return: None
        """
        self.move_params = (f'Время: {QtCore.QTime.currentTime().toString()}\n'
                          f'Старая позиция:{event.oldPos().x()} x {event.oldPos().y()}\n'
                          f'Новая позиция:{event.pos().x()} x {event.pos().y()}')
        print(self.move_params)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Событие изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """
        self.resize_params = f'Размеры окна: {event.size().height()} x {event.size().width()}'
        print(self.resize_params)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
