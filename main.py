import sys
from PyQt6 import QtWidgets
from gui.spam_gui import Ui_MainWindow
from model import train_and_predict
from langdetect import detect, LangDetectException

class SpamApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Spam Detector")
        # Połączenie przycisku sprawdź oraz reset z funkcją
        self.ui.check_btn.clicked.connect(self.check_message)
        self.ui.reset_btn.clicked.connect(self.erease_field)
        self.ui.type_text.returnPressed.connect(self.check_message)
    def check_message(self):
        text = self.ui.type_text.text().strip()

        if not text:
            self.ui.warning_message.setText("Podaj treść wiadomości.")
            return

        try:
            lang = detect(text)
        except LangDetectException:
            self.ui.warning_message.setText("Nie udało się rozpoznać języka.")
            return

        if lang != "en":
            self.ui.warning_message.setText("Wpisz wiadomość po angielsku.")
            return

        result = train_and_predict(text)
        if result == 1:
            self.ui.warning_message.setText("To jest SPAM!")
        else:
            self.ui.warning_message.setText("To NIE jest spam.")

    def erease_field(self):
        text = self.ui.type_text.text().strip()
        if text:
            self.ui.type_text.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SpamApp()
    window.show()
    sys.exit(app.exec())

