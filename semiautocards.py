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
from PyQt4 import QtGui, QtCore
#from yomi_base.lang import japanese
#from yomi_base.preference_data import Preferences
#from yomi_base.reader import MainWindowReader


class Semiauto:
    def __init__(self):
        #self.language = japanese.initLanguage()
        #self.preferences = Preferences()
        #self.preferences.load()
        pass


class SemiautoPlugin(Semiauto):
    def __init__(self):
        Semiauto.__init__(self)

        self.toolIconVisible = False
        self.window = None
        self.anki = anki_host.Anki()
        self.parent = self.anki.window()

        self.setup()

        #separator = QtGui.QAction(self.parent)
        #separator.setSeparator(True)
        #self.anki.addUiAction(separator)

        #action = QtGui.QAction(QtGui.QIcon(':/img/img/icon_logo_32.png'), '&Semiauto...', self.parent)
        #action.setIconVisibleInMenu(True)
        #action.setShortcut('Ctrl+Y')
        #action.triggered.connect(self.onShowRequest)
        #self.anki.addUiAction(action)

    def setupbuttons(self):
        from anki.hooks import wrap
        from aqt.editor import Editor
        from aqt.utils import showInfo

        def buttonPressed(self):
            showInfo("pressed " + `self`)
        def mySetupButtons(self):
            # - size=False tells Anki not to use a small button
            # - the lambda is necessary to pass the editor instance to the
            #   callback, as we're passing in a function rather than a bound
            #   method
            self._addButton("semiautobutton", lambda s=self: buttonPressed(self),
                            text="Semi Auto", size=False)

        Editor.setupButtons = wrap(Editor.setupButtons, mySetupButtons)


    def onShowRequest(self):
        if self.window:
            self.window.setVisible(True)
            self.window.activateWindow()
        else:
            self.window = MainWindowReader(
                self.parent,
                self.preferences,
                self.language,
                None,
                self.anki,
                self.onWindowClose
            )
            self.window.show()


    def onWindowClose(self):
        self.window = None


class SemiautoStandalone(Semiauto):
    def __init__(self):
        Semiauto.__init__(self)

        self.application = QtGui.QApplication(sys.argv)
        self.window = MainWindowReader(
            None,
            self.preferences,
            self.language,
            filename=sys.argv[1] if len(sys.argv) >= 2 else None
        )

        self.window.show()
        self.application.exec_()


if __name__ == '__main__':
    instance = SemiautoStandalone()
else:
    from yomi_base import anki_host
    instance = SemiautoPlugin()

