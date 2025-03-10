import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from ui_elemen import identity_section, navigation_section, registration_form, action_button
from style import STYLE_SHEET

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 420, 400)

        main_layout = QVBoxLayout()
        main_layout.addWidget(identity_section())
        main_layout.addSpacing(10)
        main_layout.addWidget(navigation_section())
        main_layout.addSpacing(10)
        main_layout.addWidget(registration_form())
        main_layout.addSpacing(10)
        main_layout.addWidget(action_button())

        self.setLayout(main_layout)
        self.setStyleSheet(STYLE_SHEET)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())
