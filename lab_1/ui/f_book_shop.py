# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'f_book_shop.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(463, 360)
        Form.setMinimumSize(QSize(300, 0))
        Form.setMaximumSize(QSize(500, 500))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        palette = QPalette()
        brush = QBrush(QColor(170, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setTextFormat(Qt.TextFormat.AutoText)

        self.verticalLayout_2.addWidget(self.label)

        self.textEditBook = QTextEdit(Form)
        self.textEditBook.setObjectName(u"textEditBook")

        self.verticalLayout_2.addWidget(self.textEditBook)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label_2.setPalette(palette1)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButtonCard = QRadioButton(Form)
        self.radioButtonCard.setObjectName(u"radioButtonCard")

        self.verticalLayout.addWidget(self.radioButtonCard)

        self.radioButtonQr = QRadioButton(Form)
        self.radioButtonQr.setObjectName(u"radioButtonQr")

        self.verticalLayout.addWidget(self.radioButtonQr)

        self.radioButtonCash = QRadioButton(Form)
        self.radioButtonCash.setObjectName(u"radioButtonCash")

        self.verticalLayout.addWidget(self.radioButtonCash)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043d\u0438\u0433\u0443", None))
        self.textEditBook.setPlaceholderText(QCoreApplication.translate("Form", u"\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440 \u0438 \u0443\u0437\u043d\u0438\u043a \u0410\u0437\u043a\u0430\u0431\u0430\u043d\u0430...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u044b", None))
        self.radioButtonCard.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u043a\u0430\u0440\u0442\u0435", None))
        self.radioButtonQr.setText(QCoreApplication.translate("Form", u"\u041f\u043e QR", None))
        self.radioButtonCash.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
    # retranslateUi

