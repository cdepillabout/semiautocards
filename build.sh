#!/bin/sh

# This generates the .ts files
pylupdate4 semiauto.pro

# this generates the .qm files
lrelease-qt4 semiauto.pro
mv ui/translations/*.qm semiauto/gen/locale

# TODO: 
# HOW TO ACTUALLY GET THE PROGRAM TO USE MY TRANSLATIONS

pyuic4 ui/forms/preferences.ui -o semiauto/gen/preferences_ui.py
pyuic4 ui/forms/mainwindow.ui -o semiauto/gen/mainwindow_ui.py
pyrcc4 ui/resources/resources.qrc -o semiauto/gen/resources_rc.py


