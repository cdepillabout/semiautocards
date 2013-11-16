#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Copyright (C) 2011  Alex Yatskov
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


import sys
import locale
import os.path

from PyQt4 import QtGui, QtCore

from anki.hooks import wrap
from aqt.editor import Editor
from aqt.utils import showCritical

from semiauto import anki_host
from semiauto.mainwindow import MainWindow

class SemiautoPlugin(object):
    def __init__(self):

        self.toolIconVisible = False
        self.window = None
        self.anki = anki_host.Anki()
        self.parent = self.anki.window
        #self.preferences = Preferences()

        # Load our specific translator files.
        localedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "semiauto", "gen", "locale")
        self.translator = QtCore.QTranslator()
        self.translator.load("semiauto_qt_" + self.anki.getLang(), localedir);
        QtGui.QApplication.installTranslator(self.translator)

        self.setup()

    def setup(self):
        def mySetupButtons(editor):
            # - size=False tells Anki not to use a small button
            editor._addButton("semiautobutton", lambda editor=editor: self.launchGUI(editor),
                            text="Semi Auto", size=False)
            shortcut = QtGui.QShortcut(QtGui.QKeySequence(_("Ctrl+j")), editor.parentWindow)
            shortcut.connect(shortcut, QtCore.SIGNAL("activated()"),
                    lambda editor=editor: self.launchGUI(editor))

        Editor.setupButtons = wrap(Editor.setupButtons, mySetupButtons)

    def launchGUI(self, editor):
        editor.saveNow()
        note = editor.note

        if not note:
            showCritical("ERROR! Must have note selected.")
            return

        note.flush()
        kanji = note["Vocab"]
        kana = note["VocabKana"]

        self.window = MainWindow(kanji, kana, parent=editor.widget,
                editor=editor, note=note)
        self.window.show()
        #if self.window:
        #    self.window.setVisible(True)
        #    self.window.activateWindow()
        #else:
        #    self.window = MainWindowReader(self.parent, kanji, kana)
        #    self.window.show()

    def onWindowClose(self):
        self.window = None


SemiautoPlugin()

