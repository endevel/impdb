from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class EntityView(QWidget):
    """
    Окно выбора таблиц для импорта
    """
    def __init__(self):
        super().__init__()
        self.entity_list = QComboBox()
        self.btn_run = QPushButton("Run")
        self.init_ui()

    def init_ui(self):
        self.entity_list.addItems(("Account", "Person"))
        vbox = QVBoxLayout()
        vbox.addWidget(self.entity_list)
        vbox.addWidget(self.btn_run)
        self.setLayout(vbox)

