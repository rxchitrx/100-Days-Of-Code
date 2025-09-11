import requests
from datetime import datetime
import smtplib
import time

MY_LAT = "your lat here (in float)"
MY_LONG = "Your long here (in float)"
time_now = datetime.now()
my_email = "your-email-here"
password = "app-password-generated-from-google-account-settings."



# Getting data from ISS API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])
iss_position = {iss_longitude, iss_latitude}


def iss_close_to_me():
    if 20 <= iss_latitude <= 30 and 45 <= iss_longitude <= 55:
        return True
    else:
        return False

def is_dark():
    if time_now.hour <= sunrise_time or time_now.hour >= sunset_time:
        return True
    else:
        return False


# Parameters for the sun API
parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,
}


#Getting data from sunrise/sunset API
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_time = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_time = int(data["results"]["sunset"].split("T")[1].split(":")[0])

while True:
    print("Running script...")
    if iss_close_to_me() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs="email-to-send-to", 
                                msg=f"Look up the ISS is overhead")
    time.sleep(60)
    