import sys
import io
import UI_ZLCheck

form_class = UI_ZLCheck.Ui_MainWindow

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
