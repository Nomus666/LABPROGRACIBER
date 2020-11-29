
import json

salida  = []
def  llamar ( url ):
    r  =  solicitudes . obtener ( url )
    return ( json . cargas ( r . contenido ))

api  =  input ( "Api key de openweathermap \ t " )
lpc= salida . añadir ( llamar ("https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid= { api } " ))
salida . añadir ( llamar ("https://api.openweathermap.org/data/2.5/weather?id=2172797&appid= { api } " ))
salida . añadir ( llamar ("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid= { api } " ))

print(lpc)