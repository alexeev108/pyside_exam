# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_ship_parameters.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 300)
        Form.setMaximumSize(QSize(500, 300))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(400, 170))
        self.groupBox.setMaximumSize(QSize(450, 200))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(16, 31, 335, 133))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 0))

        self.verticalLayout.addWidget(self.label_5)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEditTemp = QLineEdit(self.layoutWidget)
        self.lineEditTemp.setObjectName(u"lineEditTemp")
        self.lineEditTemp.setMinimumSize(QSize(200, 0))
        self.lineEditTemp.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_2.addWidget(self.lineEditTemp)

        self.lineEditGerm = QLineEdit(self.layoutWidget)
        self.lineEditGerm.setObjectName(u"lineEditGerm")
        self.lineEditGerm.setEnabled(True)
        self.lineEditGerm.setMinimumSize(QSize(200, 0))
        self.lineEditGerm.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_2.addWidget(self.lineEditGerm)

        self.lineEditTank1 = QLineEdit(self.layoutWidget)
        self.lineEditTank1.setObjectName(u"lineEditTank1")
        self.lineEditTank1.setMinimumSize(QSize(200, 0))
        self.lineEditTank1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_2.addWidget(self.lineEditTank1)

        self.lineEditTank2 = QLineEdit(self.layoutWidget)
        self.lineEditTank2.setObjectName(u"lineEditTank2")
        self.lineEditTank2.setMinimumSize(QSize(200, 0))
        self.lineEditTank2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_2.addWidget(self.lineEditTank2)

        self.lineEditTank3 = QLineEdit(self.layoutWidget)
        self.lineEditTank3.setObjectName(u"lineEditTank3")
        self.lineEditTank3.setMinimumSize(QSize(200, 0))
        self.lineEditTank3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_2.addWidget(self.lineEditTank3)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u043a \u21161", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u043a \u21162", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u043a \u21163", None))
        self.lineEditTemp.setPlaceholderText(QCoreApplication.translate("Form", u"22C", None))
        self.lineEditGerm.setPlaceholderText(QCoreApplication.translate("Form", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.lineEditTank1.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.lineEditTank2.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.lineEditTank3.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u043e\u0440\u043c\u0430", None))
    # retranslateUi

