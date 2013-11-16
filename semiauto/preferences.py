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
import pprint
import uuid

class HasToJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return obj.to_json()
        else:
            return json.JSONEncoder.default(self, obj)

class PreferenceWriter(object):
    def __init__(self, decoder):
        self.decoder = decoder
        self.settings = self._load()

    def _defaultFilename(self):
        return os.path.expanduser('~/.semidictrc')

    def _load(self):
        try:
            with open(self._defaultFilename(), 'r') as settingsFile:
                return json.load(settingsFile, encoding="utf-8", object_hook=self.decoder, #cls=SOMETHING
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
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save()

    def save(self):
        with open(self._defaultFilename(), 'w') as settingsFile:
            json.dump(self.settings, settingsFile, ensure_ascii=False, encoding="utf-8",
                    cls=HasToJsonEncoder, sort_keys=True, indent=4, separators=(',', ': '))

class Preferences(PreferenceWriter):
    def __init__(self):
        PreferenceWriter.__init__(self, self.decoder)

    def get_dict_group_prefs_for_note(self, note):
        model = note.model()

        # Get the dictionary groups and model to group mappings from the settings file.
        # If it doesn't exist, then just return blank dictionary groups and model to group
        # mappings.
        dict_groups = self.get("dict_groups", [])
        model_to_dict_group_mappings = self.get("model_to_dict_group_mappings", ModelToGroupMappings())

        # Look for the dictionary group for this model.  If it exists, just return it.
        if model_to_dict_group_mappings.contains_model(model):
            for group in dict_groups:
                if group.id_ == model_to_dict_group_mappings[model_id]:
                    return model_to_dict_group_mappings[model_id]

        # If the mapping for this model -> dictionary group id doesn't exist, then
        # just use the first dictionary group.
        dict_group = None
        if len(dict_groups) > 0:
            dict_group = dict_groups[0]
        # However, if there are no dictionary group, then create a default one
        else:
            dict_group = PreferencesDictionaryGroup()
            dict_groups.append(dict_group)
            self.set("dict_groups", dict_groups)

        # Add a mapping from this model to the specified dictionary group.
        model_to_dict_group_mappings.set_dict_group(model, dict_group)
        self.set("model_to_dict_group_mappings", model_to_dict_group_mappings)

        return dict_group

    @staticmethod
    def decoder(dict_):
        new_dict = {}
        for key, value in dict_.items():
            if key == "model_to_dict_group_mappings":
                new_dict["model_to_dict_group_mappings"] = ModelToGroupMappings.from_json(value)
            else:
                new_dict[key] = value
        return new_dict

class ModelToGroupMappings(object):
    def __init__(self, mappings={}):
        self.mappings = mappings

    def contains_model(self, model):
        return model["id"] in self.mappings

    def get_dict_group(self, model):
        return self.mappings[model["id"]]

    def set_dict_group(self, model, dict_group):
        pprint(dict_group)
        self.mappings[model["id"]] = dict_group.id_

    def to_json(self):
        return { "mappings": self.mappings }

    @classmethod
    def from_json(cls, dict_):
        assert("mappings" in dict_)
        return cls(mappings=dict_["mappings"])


class DictionaryLayouts(object):
    NONE = 0
    LONG = 1
    WIDE = 2

class PreferencesDictionaryGroup(object):
    def __init__(self, name="Default", id_=uuid.uuid1(), layout=DictionaryLayouts.NONE, tabs=2, dicts_per_tab=4):
        self.id_ = str(id_)
        self.layout = layout
        self.tabs = tabs
        self.dicts_per_tab = dicts_per_tab

        self.name = name

        self.lookup_fields = ["Vocab", "VocabKana"]

    def to_json(self):
        return { "id_": self.id_
               , "layout": self.layout
               , "tabs": self.tabs
               , "dicts_per_tab": self.dicts_per_tab
               , "name": self.dicts_per_tab
               }
