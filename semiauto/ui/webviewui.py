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

from PyQt4 import QtCore, QtGui, QtWebKit

class WebPage(QtWebKit.QWebPage):
    """
    This is an overridden webpage that prints javascript error messages
    to the console.  This helps in debugging.
    """
    def __init__(self, parent=None):
        super(WebPage, self).__init__(parent)

    def javaScriptConsoleMessage(self, message, linenumber, sourceid):
        print("javascript ERROR! (%s) %s: %s" % (sourceid, linenumber, message))


class WebView(QtWebKit.QWebView):
    def __init__(self, parent=None, ):
        super(WebView, self).__init__(parent)

    def setDefs(self, defs):
        html += u"\n</body></html>"

        webpage = DefWebPage(self)
        webpage.mainFrame().setHtml(html)
        self.setPage(webpage)


