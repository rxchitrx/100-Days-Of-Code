import requests
import os



class sheety:

    def __init__(self, date, time, Exercise, Duration, Calories):
        self.api_endpoint = os.getenv("SHEETY_API_ENDPOINT")
        self.token = os.getenv("SHEETY_TOKEN")
        self.date = date
        self.time = time
        self.exercise = Exercise
        self.duration = Duration
        self.calories = Calories

        header = {
            "Authorization" : f"Bearer {self.token}"
        }

        body = {
            'workout' : {
                'date' : self.date,
                'time' : self.time,
                'exercise' : self.exercise,
                'duration' : self.duration,
                'calories' : self.calories,
            }
        }

        self.response = requests.post(url=self.api_endpoint, json=body)
        print(self.response.status_code)
        print(self.response.json())
        
        