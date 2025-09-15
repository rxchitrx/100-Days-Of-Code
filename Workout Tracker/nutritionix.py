import os
import requests

class nutrition():
    base_url = "https://trackapi.nutritionix.com/"

    def __init__(self):
        app_id = os.getenv("NUTRITIONIX_APP_ID")
        api_key = os.getenv("NUTRITIONIX_API_KEY")



        headers = {
            "Content-Type" : 'application/json',
            "x-app-id" : app_id,
            "x-app-key" : api_key, 
        }

        self.query = input("What did you do today? ")
        self.weight_kg = input("What is your weight in kgs? ")
        self.height_cm = input("What is your height in cms? ")
        self.age = input("What is your age? ")

        payload = {
            "query" : self.query,
            "weight_kg" : self.weight_kg,
            "height_cm" : self.height_cm,
            "age" : self.age,
        }

        self.response = requests.post(url=f"{nutrition.base_url}v2/natural/exercise", headers=headers, json=payload)
        print(self.response.status_code)
        self.data = self.response.json()
        
        
        
        
        


