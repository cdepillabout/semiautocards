# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/forms/preferences.ui'
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

class Ui_preferencesDialog(object):
    def setupUi(self, preferencesDialog):
        preferencesDialog.setObjectName(_fromUtf8("preferencesDialog"))
        preferencesDialog.resize(1069, 604)
        self.verticalLayout_2 = QtGui.QVBoxLayout(preferencesDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox = QtGui.QGroupBox(preferencesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.preferencesetlistview = QtGui.QListView(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preferencesetlistview.sizePolicy().hasHeightForWidth())
        self.preferencesetlistview.setSizePolicy(sizePolicy)
        self.preferencesetlistview.setObjectName(_fromUtf8("preferencesetlistview"))
        self.verticalLayout.addWidget(self.preferencesetlistview)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addpreferencesetbutton = QtGui.QPushButton(self.groupBox)
        self.addpreferencesetbutton.setObjectName(_fromUtf8("addpreferencesetbutton"))
        self.horizontalLayout_2.addWidget(self.addpreferencesetbutton)
        self.deletepreferencesetbutton = QtGui.QPushButton(self.groupBox)
        self.deletepreferencesetbutton.setObjectName(_fromUtf8("deletepreferencesetbutton"))
        self.horizontalLayout_2.addWidget(self.deletepreferencesetbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(preferencesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closebutton = QtGui.QPushButton(preferencesDialog)
        self.closebutton.setObjectName(_fromUtf8("closebutton"))
        self.horizontalLayout.addWidget(self.closebutton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(preferencesDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.closebutton, QtCore.SIGNAL(_fromUtf8("clicked()")), preferencesDialog.close)
        QtCore.QMetaObject.connectSlotsByName(preferencesDialog)

    def retranslateUi(self, preferencesDialog):
        preferencesDialog.setWindowTitle(_translate("preferencesDialog", "Dialog", None))
        self.groupBox.setTitle(_translate("preferencesDialog", "GroupBox", None))
        self.addpreferencesetbutton.setText(_translate("preferencesDialog", "PushButton", None))
        self.deletepreferencesetbutton.setText(_translate("preferencesDialog", "PushButton", None))
        self.groupBox_2.setTitle(_translate("preferencesDialog", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("preferencesDialog", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("preferencesDialog", "Tab 2", None))
        self.closebutton.setText(_translate("preferencesDialog", "PushButton", None))

