'''Practice
Create a program that will ask user to search a word. Search this word in Giphy (use their API). Return links to these GIFs as a result
Взяти API-weather, розпарсити і вивезти погоду від користувача(вводить локацію, по цій локації повернеться погода, вологість і тд) https://openweathermap.org *Потрібна реєстрація і створення свого api-ключа
Вивезти всіх космонавтів(кількість і імена) http://api.open-notify.org/astros.json '''

import requests
from IPython.display import IFrame, display

# Practice Task 1

def Giphy():
    base_url = 'https://api.giphy.com/v1/gifs/search'
    search = input('Which gif do you want to find').lower()

    parametry = {
        'api_key': 'Cuex3rAQe8a2dM5SmQKlK2AVFxpT2qH2',
        'limit': 25,
        'offset': 0,
        'rating': 'g',
        'lang': 'en',
        'q': search
    }

    response = requests.get(base_url, params=parametry)

    if response.status_code == 200:
        dani = response.json()["data"]
        for gif in dani:
            display(IFrame(src=gif["embed_url"], width=600, height=550))
        if not dani:
            print('No gifs found')
        else:
            print('Incorrect operation, try again')
     
# Practice Task 2 Current weather data 

import requests, json
api_key = "ce937f608ab3872ba81205d9711a820b"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
lang = '&lang=uk'
units = '&units=metric'
city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name + lang + units
 
response = requests.get(complete_url) # # метод get модуля requests
 
x = response.json() ## конвертувати дані у форматі json в

if x["cod"] != "404": # Тепер x містить список вкладених словників, перевірка чи значення ключа "cod" не дорівнює "404"
    y = x["main"]
    temperatura = y["temp"]
    tilotemp = y["feels_like"]
    barometr = y["pressure"]
    vydymist = y["humidity"]
    z = x["weather"]

    weather_description = z[0]["description"]
 
    print(" Температура на дворі (в градусах цельсія) = " +
                    str(temperatura) +
          "\n Відчувається, як (в градусах цельсія) = " +
                    str(tilotemp) +
          "\n Атмосферний тиск (в hPa ) = " +
                    str(barometr) +
          "\n Видимість (в %) = " +
                    str(vydymist) +
          "\n Загальна картина = " +
                    str(weather_description))
 
else:
    print(" Неможливо знайти місто ")

# Task 3 
def kosmos():
    url = 'http://api.open-notify.org/astros.json'
    response = requests.get(url) # daje zaput na otrumania danux

    if response.status_code == 200: # jaksho zaput uspishnu, potribno otrumatu json
        dani = response.json()
        for name in dani['asronavty']:
            print(name['name'])
        print(f'На даний момент на орбіті {dani["number"]} людей')
    else:
        print('Щось пішло не так, спробуйте пізніше.')



