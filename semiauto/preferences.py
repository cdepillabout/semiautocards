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

import json
import os

class Preferences(object):

    def __init__(self):
        self.settings = self._load()

    def _defaultFilename(self):
        return os.path.expanduser('~/.semidictrc')

    def _load(self):
        try:
            with open(self._defaultFilename(), 'r') as settingsFile:
                return json.load(settingsFile, encoding="utf-8" #object_hook=SOMETHING, #cls=SOMETHING
                        )
        # if the file doesn't exist, we will get an IO Error
        except IOError:
            return {}

    def __contains__(self, key):
        return key in self.settings

    def __getitem__(self, key):
        return self.settings[key]

    def __setitem__(self, key, value):
        self.settings[key] = value

    def get(self, key, default=None):
        try:
            return self.settings[key]
        except KeyError:
            return default

    def set(self, key, value):
        self.settings[key] = value

    def save(self):
        with open(self._defaultFilename(), 'w') as settingsFile:
            json.dump(self.settings, settingsFile, ensure_ascii=False, encoding="utf-8",
                    sort_keys=True, indent=4, separators=(',', ': '))
