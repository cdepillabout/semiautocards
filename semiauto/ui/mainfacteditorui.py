# -*- coding: utf-8 -*-

# Copyright (C) 2013  Dennis Gosnell
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtCore, QtGui

class Ui_MainFactEditor(object):
    def setupUi(self, mainfacteditor):
        mainfacteditor.setObjectName(u"mainfacteditor")
        mainfacteditor.resize(900, 650)

        self.centralwidget = QtGui.QWidget(mainfacteditor)
        self.centralwidget.setObjectName(u"centralwidget")
        mainfacteditor.setCentralWidget(self.centralwidget)

        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addLayout(self.formLayout, 1)

        self.vocab_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.vocab_lineEdit.setObjectName(u"vocab_lineEdit")
        self.formLayout.addRow(u"Vocab:", self.vocab_lineEdit)

        self.vocabkana_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.vocabkana_lineEdit.setObjectName(u"vocabkana_lineEdit")
        self.formLayout.addRow(u"Vocab Kana:", self.vocabkana_lineEdit)

        self.vocabenglish_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.vocabenglish_textEdit.setObjectName(u"vocabenglish_textEdit")
        self.formLayout.addRow(u"Vocab English:", self.vocabenglish_textEdit)

        self.sentence_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.sentence_textEdit.setObjectName(u"sentence_textEdit")
        self.formLayout.addRow(u"Sentence:", self.sentence_textEdit)

        self.sentenceenglish_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.sentenceenglish_textEdit.setObjectName(u"sentenceenglish_textEdit")
        self.formLayout.addRow(u"Sentence English:", self.sentenceenglish_textEdit)

        self.notes_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.notes_textEdit.setObjectName(u"notes_textEdit")
        self.formLayout.addRow(u"Notes:", self.notes_textEdit)

        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(
                QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(u"buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(mainfacteditor.okay)
        self.buttonBox.rejected.connect(mainfacteditor.exit)

        QtCore.QMetaObject.connectSlotsByName(mainfacteditor)


