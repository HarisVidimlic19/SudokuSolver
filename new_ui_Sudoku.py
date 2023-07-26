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

        self.hintButton = QPushButton(self.layoutWidget1)
        self.hintButton.setObjectName(u"hintButton")

        self.gridLayout_2.addWidget(self.hintButton, 2, 0, 1, 1)

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

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem6 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem7 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem8 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem9 = self.tableWidget_7.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget_7.verticalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget_7.verticalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableWidget_7.isSortingEnabled()
        self.tableWidget_7.setSortingEnabled(False)
        self.tableWidget_7.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem12 = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem13 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem14 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem15 = self.tableWidget_8.verticalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget_8.verticalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget_8.verticalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.tableWidget_8.isSortingEnabled()
        self.tableWidget_8.setSortingEnabled(False)
        self.tableWidget_8.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem21 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled3 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled3)

        ___qtablewidgetitem24 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem25 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem27 = self.tableWidget_5.verticalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget_5.verticalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget_5.verticalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled4 = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        self.tableWidget_5.setSortingEnabled(__sortingEnabled4)

        ___qtablewidgetitem30 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem31 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem32 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem33 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled5 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled5)

        ___qtablewidgetitem36 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem37 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem38 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem39 = self.tableWidget_6.verticalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableWidget_6.verticalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.tableWidget_6.verticalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled6 = self.tableWidget_6.isSortingEnabled()
        self.tableWidget_6.setSortingEnabled(False)
        self.tableWidget_6.setSortingEnabled(__sortingEnabled6)

        ___qtablewidgetitem42 = self.tableWidget_9.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem43 = self.tableWidget_9.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem44 = self.tableWidget_9.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem45 = self.tableWidget_9.verticalHeaderItem(0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem46 = self.tableWidget_9.verticalHeaderItem(1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem47 = self.tableWidget_9.verticalHeaderItem(2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled7 = self.tableWidget_9.isSortingEnabled()
        self.tableWidget_9.setSortingEnabled(False)
        self.tableWidget_9.setSortingEnabled(__sortingEnabled7)

        ___qtablewidgetitem48 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem49 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem50 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem51 = self.tableWidget_4.verticalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem52 = self.tableWidget_4.verticalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem53 = self.tableWidget_4.verticalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled8 = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setSortingEnabled(__sortingEnabled8)

        self.difficultyLabel.setText(QCoreApplication.translate("MainWindow", u"Difficulty:", None))
        self.difficultyBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Easy", None))
        self.difficultyBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.difficultyBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Hard", None))
        self.difficultyBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.solveButton.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.hintButton.setText(QCoreApplication.translate("MainWindow", u"Hint", None))
        self.mistakes.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.mistakesLabel.setText(QCoreApplication.translate("MainWindow", u"Mistakes:", None))
    # retranslateUi

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
