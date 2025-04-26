import sys
import requests
from datetime import datetime
from PyQt5 import QtWidgets, QtGui
from weather_app import Ui_Form

class WeatherApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.update_date()
        self.ui.btn_search.clicked.connect(self.search_weather)
        self.ui.btn_exit.clicked.connect(self.exit_app)

    def search_weather(self):
        location = self.ui.search.text().strip()
        if not location:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a location !")
            return

        try:
            API_KEY = "2a7b91cdb2e4fbdeabccc07ec0a15dcd"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"

            response = requests.get(url)
            data = response.json()

            if str(data.get("cod")) != "200":
                raise Exception("Sorry, location not found.")

            weather = data["weather"][0]["main"]
            icon_code = data["weather"][0]["icon"]
            min_temp = data["main"]["temp_min"]
            max_temp = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            pressure = data["main"]["pressure"]
            visibility = data.get("visibility", 0)

            self.ui.label_cuaca.setText(weather)
            self.update_weather_icon(icon_code)
            self.ui.label_suhu1.setText(f"Min Temperatur : {min_temp} °C")
            self.ui.label_suhu2.setText(f"Max Temperatur : {max_temp} °C")
            self.ui.label_kosong1.setText(f"{humidity} %")
            self.ui.label_kosong2.setText(f"{wind_speed} m/s")
            self.ui.label_kosong3.setText(f"{pressure} hPa")
            self.ui.label_kosong4.setText(f"{visibility/1000:.1f} km")

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def update_weather_icon(self, icon_code):
        url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        image = QtGui.QImage()
        image.loadFromData(requests.get(url).content)
        pixmap = QtGui.QPixmap(image)

        self.ui.logo2.setPixmap(pixmap)
        self.ui.logo2.setScaledContents(True)

    def update_date(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%A, %d %B %Y")
        self.ui.label_date.setText(formatted_date)

    def exit_app(self):
        reply = QtWidgets.QMessageBox.question(self, 'Exit',
            "Are you sure you want to exit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)

        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.qApp.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
