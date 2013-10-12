# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/forms/mainwindow.ui'
#
# Created: Sat Oct 12 12:30:11 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.accentlabel = QtGui.QLabel(self.centralwidget)
        self.accentlabel.setObjectName(_fromUtf8("accentlabel"))
        self.horizontalLayout.addWidget(self.accentlabel)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okaybutton = QtGui.QPushButton(self.centralwidget)
        self.okaybutton.setObjectName(_fromUtf8("okaybutton"))
        self.horizontalLayout.addWidget(self.okaybutton)
        self.cancelbutton = QtGui.QPushButton(self.centralwidget)
        self.cancelbutton.setObjectName(_fromUtf8("cancelbutton"))
        self.horizontalLayout.addWidget(self.cancelbutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Settings = QtGui.QMenu(self.menubar)
        self.menu_Settings.setObjectName(_fromUtf8("menu_Settings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.actionpreferences = QtGui.QAction(MainWindow)
        self.actionpreferences.setObjectName(_fromUtf8("actionpreferences"))
        self.menu_File.addAction(self.action_Quit)
        self.menu_Settings.addAction(self.actionpreferences)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.accentlabel.setBuddy(self.lineEdit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.cancelbutton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2", None))
        self.accentlabel.setText(_translate("MainWindow", "Accent", None))
        self.okaybutton.setText(_translate("MainWindow", "PushButton", None))
        self.cancelbutton.setText(_translate("MainWindow", "PushButton", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Settings.setTitle(_translate("MainWindow", "&Settings", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))
        self.actionpreferences.setText(_translate("MainWindow", "&Preferences...", None))

