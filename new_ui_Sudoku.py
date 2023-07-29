# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SudokuSAxjIF.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 460)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setBaseSize(QSize(500, 0))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 954, 297))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # Create the 9x9 table widgets
        self.tableWidget = QTableWidget(self.layoutWidget)
        self.tableWidget_2 = QTableWidget(self.layoutWidget)
        self.tableWidget_3 = QTableWidget(self.layoutWidget)
        self.tableWidget_4 = QTableWidget(self.layoutWidget)
        self.tableWidget_5 = QTableWidget(self.layoutWidget)
        self.tableWidget_6 = QTableWidget(self.layoutWidget)
        self.tableWidget_7 = QTableWidget(self.layoutWidget)
        self.tableWidget_8 = QTableWidget(self.layoutWidget)
        self.tableWidget_9 = QTableWidget(self.layoutWidget)

        self.createTableWidget(self.tableWidget, '', 0, 0)
        self.createTableWidget(self.tableWidget_2, '2', 0, 1)
        self.createTableWidget(self.tableWidget_3, '3', 0, 2)
        self.createTableWidget(self.tableWidget_4, '4', 1, 0)
        self.createTableWidget(self.tableWidget_5, '5', 1, 1)
        self.createTableWidget(self.tableWidget_6, '6', 1, 2)
        self.createTableWidget(self.tableWidget_7, '7', 2, 0)
        self.createTableWidget(self.tableWidget_8, '8', 2, 1)
        self.createTableWidget(self.tableWidget_9, '9', 2, 2)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(360, 350, 235, 89))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.difficultyLabel = QLabel(self.layoutWidget1)
        self.difficultyLabel.setObjectName(u"difficultyLabel")

        self.horizontalLayout.addWidget(self.difficultyLabel)

        self.difficultyBox = QComboBox(self.layoutWidget1)
        self.difficultyBox.addItem("")
        self.difficultyBox.addItem("")
        self.difficultyBox.addItem("")
        self.difficultyBox.addItem("")
        self.difficultyBox.setObjectName(u"difficultyBox")

        self.horizontalLayout.addWidget(self.difficultyBox)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.solveButton = QPushButton(self.layoutWidget1)
        self.solveButton.setObjectName(u"solveButton")

        self.gridLayout_2.addWidget(self.solveButton, 2, 1, 1, 1)

        self.resetButton = QPushButton(self.layoutWidget1)
        self.resetButton.setObjectName(u"resetButton")

        self.gridLayout_2.addWidget(self.resetButton, 1, 0, 1, 1)

        self.newButton = QPushButton(self.layoutWidget1)
        self.newButton.setObjectName(u"newButton")

        self.gridLayout_2.addWidget(self.newButton, 2, 0, 1, 1)

        self.mistakes = QLabel(self.layoutWidget1)
        self.mistakes.setObjectName(u"mistakes")

        self.gridLayout_2.addWidget(self.mistakes, 0, 1, 1, 1)

        self.mistakesLabel = QLabel(self.layoutWidget1)
        self.mistakesLabel.setObjectName(u"mistakesLabel")
        self.mistakesLabel.setTextFormat(Qt.AutoText)
        self.mistakesLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.mistakesLabel, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        self.resetButton.clicked.connect(MainWindow.resetBoard)
        self.tableWidget.cellChanged.connect(MainWindow.editCell)
        self.tableWidget_2.cellChanged.connect(MainWindow.editCell)
        self.tableWidget_3.cellChanged.connect(MainWindow.editCell)
        self.tableWidget_4.cellChanged.connect(MainWindow.editCell)
        self.tableWidget_5.cellChanged.connect(MainWindow.editCell)
        self.tableWidget_6.cellChanged.connect(MainWindow.editCell)
        self.tableWidget_7.cellChanged.connect(MainWindow.editCell)
        self.tableWidget_8.cellChanged.connect(MainWindow.editCell)
        self.tableWidget_9.cellChanged.connect(MainWindow.editCell)
        self.newButton.clicked.connect(MainWindow.newBoard)
        self.solveButton.clicked.connect(MainWindow.autoSolve)
        self.difficultyBox.currentIndexChanged.connect(MainWindow.selectDifficulty)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def createTableWidget(self, widget: QTableWidget, widgetCount: str, row: int, column: int):        
        # Set 3 columns
        widget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)

        # Set 3 rows
        widget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        widget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        widget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        widget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()

        # Set each item in the table 9x9
        widget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        widget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        widget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        widget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        widget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        widget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        widget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        widget.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        widget.setItem(2, 2, __qtablewidgetitem14)

        # Set the size policy
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())

        # Set the widget properties
        widget.setSizePolicy(sizePolicy)
        widget.setObjectName(u"tableWidget"+widgetCount)
        widget.setMinimumSize(QSize(0, 0))
        widget.setMaximumSize(QSize(301, 91))
        widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        widget.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        widget.setSelectionMode(QAbstractItemView.NoSelection)
        widget.setIconSize(QSize(0, 0))

        widget.horizontalHeader().setVisible(False)
        widget.verticalHeader().setVisible(False)

        setattr(self, "tableWidget"+widgetCount, widget) # Set the widget in the class
        self.gridLayout.addWidget(widget, row, column, 1, 1) # Add the widget to the grid layout

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        self.difficultyLabel.setText(QCoreApplication.translate("MainWindow", u"Difficulty:", None))
        self.difficultyBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Easy", None))
        self.difficultyBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.difficultyBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Hard", None))
        self.difficultyBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.solveButton.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.newButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.mistakes.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.mistakesLabel.setText(QCoreApplication.translate("MainWindow", u"Mistakes:", None))
    # retranslateUi
