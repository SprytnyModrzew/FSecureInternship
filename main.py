from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    # defined location of Poznan
    measurements = requests.get(f"https://www.metaweather.com/api/location/{woeId}")
    measure_json = measurements.json()['consolidated_weather'][0]

    # chosen some (not all) values to represent
    return render_template('measurements.html', station_location=location, date=measure_json['applicable_date'],
                           min_temp=round(measure_json['min_temp'], 2), max_temp=round(measure_json['max_temp'], 2),
                           humidity=round(measure_json['humidity'], 0),
                           weather_state_name=measure_json['weather_state_name'],
                           cur_temp=round(measure_json['the_temp'], 2))


if __name__ == "__main__":
    # defined location of Poznan, wasn't sure whether to use predefined location or getting it from the user
    response = requests.get("https://www.metaweather.com/api/location/search/?lattlong=52.409538,16.931992")
    woeId = response.json()[0]['woeid']
    location = response.json()[0]['title']

    app.run()
