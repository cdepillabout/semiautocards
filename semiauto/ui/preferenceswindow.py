# -*- coding: UTF-8 -*-

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

import aqt

from PyQt4 import QtGui, QtCore
from ..gen.preferences_ui import Ui_PreferencesWindow

class PreferencesWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.parent = parent
        self.ui = Ui_PreferencesWindow()
        self.ui.setupUi(self)
        self.setupSignals(self.ui)
        #self.fillin(word_kanji, word_kana)

    def setupSignals(self, ui):
        # open up preferences dialog when preferences is selected
        #QtCore.QObject.connect(ui.action_Preferences, QtCore.SIGNAL("activated()"),
        #        lambda _: self.launchPreferences())
        pass

    def exit(self):
        """
        reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure you want to quit?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.close()
            """
        self.close()

    def reset(self, button):
        """
        This is the action for the reset button.
        It resets all the selected definition parts and sentences.
        """

    def okay(self):
        """
        Action for the okay button.  This collects the selected definition
        parts and example sentences from our definition web views.
        """
