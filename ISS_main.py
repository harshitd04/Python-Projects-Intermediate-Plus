import requests
from datetime import datetime
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""

MY_LAT = 28.701868
MY_LONG = 77.098360
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= latitude <= MY_LONG + 5:
        return True

def is_night():

    iss_position = (longitude,latitude)
    parameter ={
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp@gmail.com")
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg="Subject:Look Up. \n\nThe ISS is above you in the sky.")





