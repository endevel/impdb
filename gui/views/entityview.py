from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QWidget


class EntityView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.entitylist = QComboBox()
