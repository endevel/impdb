from PyQt5.QtWidgets import QMainWindow

from gui.views.entityview import EntityView


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.entityview = EntityView()
        self.init_ui()

    def init_ui(self):
        self.setCentralWidget(self.entityview)
