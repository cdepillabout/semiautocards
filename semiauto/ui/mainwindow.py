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
from ..gen.mainwindow_ui import Ui_MainWindow
from .preferenceswindow import PreferencesWindow
#from .deforderer import DefOrderer

#from dictscrape import DaijirinDictionary, DaijisenDictionary, \
#        ProgressiveDictionary, NewCenturyDictionary
from ..dictionary import WebYahooDaijisenDict
from ..utils import abbreviate

from semiauto import anki_host

class MainWindow(QtGui.QMainWindow):

    def __init__(self, word_kanji, word_kana, parent=None, editor=None, note=None, preferences=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.word_kanji = word_kanji
        self.word_kana = word_kana
        self.preferences = preferences
        self.parent = parent
        self.editor = editor
        self.note = note

        self.dict_group_prefs = self.preferences.get_dict_group_prefs_for_note(note)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resize(self.preferences.get("main_window_size_x", 800), self.preferences.get("main_window_size_y", 600))
        if "main_window_position_x" in self.preferences and "main_window_position_y" in self.preferences:
            self.move(self.preferences.get("main_window_position_x"), self.preferences.get("main_window_position_y"))

        self.setupSignals(self.ui)
        self.setupEvents()

        #self.fillin(word_kanji, word_kana)

    def setupSignals(self, ui):
        # open up preferences dialog when preferences is selected
        #QtCore.QObject.connect(ui.action_Preferences, QtCore.SIGNAL("activated()"),
        #        self.launchPreferences)
        ui.action_Preferences.activated.connect(self.launchPreferences)

    def setupEvents(self):
        self.resizeEvent = self.onResize
        self.moveEvent = self.onMove

    def onResize(self, event):
        self.preferences.set("main_window_size_x", event.size().width())
        self.preferences.set("main_window_size_y", event.size().height())
        self.preferences.save()

    def onMove(self, event):
        self.preferences.set("main_window_position_x", event.pos().x())
        self.preferences.set("main_window_position_y", event.pos().y())
        self.preferences.save()

    def launchPreferences(self):
        preferences = PreferencesWindow(parent=self)
        preferences.show()

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
        # this shows the sender (but in this case it will only be the reset button)
        #sender = self.mainwindowselector.sender()
        webviews = [self.ui.daijisendefwebview,
                #self.ui.daijirindefwebview,
                #self.ui.newcenturydefwebview,
                #self.ui.progressdefwebview,
                ]
        for w in webviews:
            mainframe = w.page().mainFrame()
            #mainframe.evaluateJavaScript(u"resetAll()")

    def okay(self):
        """
        Action for the okay button.  This collects the selected definition
        parts and example sentences from our definition web views.
        """
        def collect_example_sentences(mainframe):
            """
            Return a list of all the example_sentences in a qwebframe object.
            """
            example_sentences = []

            ex_sent_divs = mainframe.findAllElements(u'div[class="ex_sent_selected"]')
            for elem in ex_sent_divs:
                jap_sent_elem = elem.findFirst(u'span[class="jap_sentence"]')
                eng_sent_elem = elem.findFirst(u'span[class="eng_trans"]')
                jap_sent = unicode(jap_sent_elem.toPlainText())
                eng_sent = unicode(eng_sent_elem.toPlainText())
                example_sentence = (jap_sent, eng_sent)
                example_sentences.append(example_sentence)

            return example_sentences

        # get accent
        accent = unicode(self.ui.accentlineedit.text())

        jap_webviews = [self.ui.daijisendefwebview, self.ui.daijirindefwebview]
        eng_webviews = [self.ui.newcenturydefwebview, self.ui.progressdefwebview]

        jap_defs = []
        eng_defs = []

        # list of tuples of (japanese_sentences, english_sentence)
        # english_sentence may be none
        example_sentences = []

        for w in jap_webviews:
            mainframe = w.page().mainFrame()
            def_parts = mainframe.findAllElements(u'span[class="defpart_selected"]')
            for elem in def_parts:
                jap_defs.append(u'%s' % unicode(elem.toPlainText()))

            example_sentences += collect_example_sentences(mainframe)

        for w in eng_webviews:
            mainframe = w.page().mainFrame()
            def_parts = mainframe.findAllElements(u'span[class="defpart_selected"]')
            for i, elem in enumerate(def_parts):
                eng_defs.append(u'%s' % unicode(elem.toPlainText()))

            example_sentences += collect_example_sentences(mainframe)

        self.close()
        self.defordererwindow = DefOrderer(accent, jap_defs, eng_defs, example_sentences,
                self.word_kanji, self.word_kana,
                parent=self.parent, editor=self.editor, note=self.note)
        self.defordererwindow.show()

    def addDefinition(self, defwebviewwidget, result):
        # add result definitions
        defwebviewwidget.setDefs(result.defs)

    def fillin(self, word_kanji, word_kana):
        #daijirin = DaijirinDictionary()
        daijisen = WebYahooDaijisenDict()
        #progressive = ProgressiveDictionary()
        #newcentury = NewCenturyDictionary()
        dicts = [
                #(daijirin, self.ui.daijirindefwebview, self.ui.daijirinwebview, self.ui.daijirinresultwordlabel),
                (daijisen, self.ui.daijisendefwebview, self.ui.daijisenresultwordlabel),
                #(progressive, self.ui.progressdefwebview, self.ui.progresswebview, self.ui.progressresultwordlabel),
                #(newcentury, self.ui.newcenturydefwebview, self.ui.newcentywebview, self.ui.newcenturyresultwordlabel),
                ]

        #self.ui.statusbar.showMessage('Adding defs for %s (%s)...' % (word_kanji, word_kana))

        for d, defwebviewwidget, resultwordlabel in dicts:
            result = d.lookup(word_kanji, word_kana)
            #if d == daijirin:
            #    if result.accent:
            #        self.ui.accentlineedit.setText(result.accent)
            #        self.ui.accentlineedit.setEnabled(True)
            #        self.ui.useaccentcheckbox.setEnabled(True)
            #    else:
            #        self.ui.accentlineedit.setText("NO ACCENT")
            #        self.ui.accentlineedit.setEnabled(False)
            #        self.ui.useaccentcheckbox.setEnabled(False)

            # add webview
            #webviewwidget.setUrl(QtCore.QUrl.fromEncoded(result.url))

            # add the resulting word
            resultwordlabeltext = u""
            if result.definition_found():
                if result.kanji == result.kana:
                    resultwordlabeltext = u"%s" % result.kanji
                else:
                    resultwordlabeltext = u"%s (%s)" % (result.kanji, result.kana)
            else:
                resultwordlabeltext = u"NO DEFINITION FOUND"

            resultwordlabel.setToolTip(resultwordlabeltext)
            resultwordlabeltext = self.abbreviate(resultwordlabeltext)
            resultwordlabel.setText(u'<font color="#555555">%s</font>' % resultwordlabeltext)

            #self.addDefinition(defwebviewwidget, result)
