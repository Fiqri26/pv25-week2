from PyQt6.QtWidgets import (
    QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QGroupBox, QFormLayout
)

def identity_section():
    identitas_box = QGroupBox("Identitas (vertical box layout)")
    identitas_layout = QVBoxLayout()

    label_nama = QLabel("Nama : Muhammad Fiqri Jordy Ardianto")
    label_nim = QLabel("NIM   : F1D022145")
    label_kelas = QLabel("Kelas : C")

    identitas_layout.addWidget(label_nama)
    identitas_layout.addWidget(label_nim)
    identitas_layout.addWidget(label_kelas)
    identitas_box.setLayout(identitas_layout)

    return identitas_box

def navigation_section():
    nav_box = QGroupBox("Navigation (horizontal box layout)")
    nav_layout = QHBoxLayout()

    nav_layout.addWidget(QPushButton("Home"))
    nav_layout.addWidget(QPushButton("About"))
    nav_layout.addWidget(QPushButton("Contact"))

    nav_box.setLayout(nav_layout)
    return nav_box

def registration_form():
    form_box = QGroupBox("User Registration (form layout)")
    form_layout = QFormLayout()

    full_name = QLineEdit()
    email = QLineEdit()
    phone = QLineEdit()

    gender_male = QRadioButton("Male")
    gender_female = QRadioButton("Female")
    gender_layout = QHBoxLayout()
    gender_layout.addWidget(gender_male)
    gender_layout.addWidget(gender_female)

    country = QComboBox()
    country.addItems(["Select Country", "Indonesia", "Malaysia", "Singapura", "Thailand", "Vietnam", "Filipina", "Myanmar", "Laos", "Kamboja"])

    form_layout.addRow("Full Name :", full_name)
    form_layout.addRow("Email :", email)
    form_layout.addRow("Phone :", phone)
    form_layout.addRow("Gender :", gender_layout)
    form_layout.addRow("Country :", country)

    form_box.setLayout(form_layout)
    return form_box

def action_button():
    action_box = QGroupBox("Actions (horizontal box layout)")
    action_layout = QHBoxLayout()

    submit_btn = QPushButton("Submit")
    cancel_btn = QPushButton("Cancel")

    action_layout.addWidget(submit_btn)
    action_layout.addWidget(cancel_btn)
    action_box.setLayout(action_layout)

    return action_box
