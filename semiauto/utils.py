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


def abbreviate(self, text, max=20):
    """Abbreviate a string."""
    if max < 5:
        raise Exception("Max cannot be less than 5.")

    beforelen = int((max - 3) / 2)
    afterlen = 0 - beforelen

    if len(text) > max:
        return u"%s%s%s" % (text[:beforeandafterlen], u"...", text[afterlen:])
    else:
        return text
