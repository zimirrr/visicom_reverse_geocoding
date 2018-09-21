# -*- coding: utf-8 -*-
"""
Class for settings dialog from qt designer
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'settings_dialog.ui'))


class Config(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Config, self).__init__()
        self.setupUi(self)
