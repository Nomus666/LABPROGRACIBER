import requests
import json

salida  = []


api="b1b15e88fa797225412429c1c50c122a1"

url=( "https://api.openweathermap.org/data/2.5/weather?q=Monterrey&appid=" + api )

data=requests.get(url)
read=data.json()
temp= (["temp"]["average"])
clima = round(temp - 273.15)
humedad=(["humidity"])
viento=(["wind_speed"])

print(salida[0])

