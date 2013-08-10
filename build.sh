#!/bin/sh
pyuic4 ui/preferences.ui -o semiauto/gen/preferences_ui.py
pyuic4 ui/mainwindow.ui -o semiauto/gen/mainwindow_ui.py
pyrcc4 ui/resources.qrc -o semiauto/gen/resources_rc.py
