import sys

from PySide6.QtWidgets import QApplication, QWidget

from views.ui_form import UIMainWidget

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UIMainWidget()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
