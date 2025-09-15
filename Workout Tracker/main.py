import os
from dotenv import load_dotenv
from nutritionix import nutrition
from Sheety import sheety
from datetime import datetime

now = datetime.now()
date_str = now.strftime("%Y/%m/%d")
time_str = now.strftime("%H:%M:%S")




load_dotenv()

nutrition_data = nutrition()

exercise = nutrition_data.data['exercises'][0]
exercise_name = exercise['name']
exercise_duration = exercise['duration_min']
exercise_calories = exercise['nf_calories']



sheety = sheety(date_str, time_str, exercise_name, exercise_duration, exercise_calories)


