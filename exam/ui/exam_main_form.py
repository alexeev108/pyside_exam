# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exam_main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_Organizer(object):
    def setupUi(self, Organizer):
        if not Organizer.objectName():
            Organizer.setObjectName(u"Organizer")
        Organizer.resize(726, 402)
        Organizer.setMaximumSize(QSize(1000, 1000))
        self.actionSave_as = QAction(Organizer)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionExit = QAction(Organizer)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionOpen = QAction(Organizer)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(Organizer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(100, 0))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_6.addWidget(self.lineEdit)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout.addWidget(self.dateTimeEdit)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(300, 0))

        self.verticalLayout_3.addWidget(self.listWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_4.addWidget(self.pushButton_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        Organizer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Organizer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 726, 33))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        Organizer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Organizer)
        self.statusbar.setObjectName(u"statusbar")
        Organizer.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionSave_as)
        self.menu_File.addAction(self.actionExit)

        self.retranslateUi(Organizer)

        QMetaObject.connectSlotsByName(Organizer)
    # setupUi

    def retranslateUi(self, Organizer):
        Organizer.setWindowTitle(QCoreApplication.translate("Organizer", u"\u041f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0449\u0438\u043a \u0437\u0430\u0434\u0430\u0447", None))
        self.actionSave_as.setText(QCoreApplication.translate("Organizer", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
#if QT_CONFIG(shortcut)
        self.actionSave_as.setShortcut(QCoreApplication.translate("Organizer", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("Organizer", u"\u0412\u044b\u0445\u043e\u0434", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("Organizer", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("Organizer", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("Organizer", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.label_4.setText(QCoreApplication.translate("Organizer", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Organizer", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label.setText(QCoreApplication.translate("Organizer", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Organizer", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Organizer", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u0440\u043e\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("Organizer", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.label_3.setText(QCoreApplication.translate("Organizer", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043c\u043e\u0438\u0445 \u0437\u0430\u0434\u0430\u0447", None))
        self.pushButton.setText(QCoreApplication.translate("Organizer", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.pushButton_3.setText(QCoreApplication.translate("Organizer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.menu_File.setTitle(QCoreApplication.translate("Organizer", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

