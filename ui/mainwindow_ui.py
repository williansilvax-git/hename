# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 622)
        MainWindow.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.actionSair = QAction(MainWindow)
        self.actionSair.setObjectName(u"actionSair")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(690, 10, 321, 221))
        self.groupBox.setStyleSheet(u"font: 700 italic 11pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 60, 301, 111))
        self.label_5.setLineWidth(1)
        self.label_5.setWordWrap(True)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 671, 27))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line_diretorio = QLineEdit(self.widget)
        self.line_diretorio.setObjectName(u"line_diretorio")

        self.horizontalLayout.addWidget(self.line_diretorio)

        self.push_selecionar = QPushButton(self.widget)
        self.push_selecionar.setObjectName(u"push_selecionar")

        self.horizontalLayout.addWidget(self.push_selecionar)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 40, 671, 231))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.list_arquivos = QListWidget(self.widget1)
        self.list_arquivos.setObjectName(u"list_arquivos")

        self.verticalLayout.addWidget(self.list_arquivos)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.line_pseudo_nome = QLineEdit(self.widget1)
        self.line_pseudo_nome.setObjectName(u"line_pseudo_nome")

        self.horizontalLayout_2.addWidget(self.line_pseudo_nome)

        self.radio_unico = QRadioButton(self.widget1)
        self.radio_unico.setObjectName(u"radio_unico")

        self.horizontalLayout_2.addWidget(self.radio_unico)

        self.radio_todos = QRadioButton(self.widget1)
        self.radio_todos.setObjectName(u"radio_todos")
        self.radio_todos.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radio_todos)

        self.push_executar = QPushButton(self.widget1)
        self.push_executar.setObjectName(u"push_executar")

        self.horizontalLayout_2.addWidget(self.push_executar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 280, 671, 217))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.list_renomeados = QListWidget(self.widget2)
        self.list_renomeados.setObjectName(u"list_renomeados")

        self.verticalLayout_2.addWidget(self.list_renomeados)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1026, 23))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menuArquivo.addAction(self.actionSair)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"AVISO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ferramenta ainda em fase de desenvolvimento... Ap\u00f3s o renomeamento dos arquivos, n\u00e3o ser\u00e1 poss\u00edvel desfazer o processo. Por isso use com cuidado.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Diret\u00f3rio", None))
        self.push_selecionar.setText(QCoreApplication.translate("MainWindow", u"Selecionar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Arquivos listados", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pseudo-nome:", None))
        self.radio_unico.setText(QCoreApplication.translate("MainWindow", u"\u00danico arquivo", None))
        self.radio_todos.setText(QCoreApplication.translate("MainWindow", u"Todos", None))
        self.push_executar.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Arquivos renomeados", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
    # retranslateUi

