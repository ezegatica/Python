import time
import random
import json
from Adafruit_IO import Client, Feed

ADAFRUIT_IO_KEY =       
ADAFRUIT_IO_USERNAME =  
api_key =               
base_url =              

def obtenerTemperatura(ciudad):
    import requests
    import json

    
    complete_url = base_url + "appid=" + api_key + "&q=" + ciudad
    respuestaHTTP = requests.get(complete_url)

    if(respuestaHTTP.status_code == 200):  # codigo 200 es que fue exitoso
        respuestaJson = respuestaHTTP.json()

        # Adentro de main están todos los datos de temperatura, presión, etc. Entonces se guarda en una variable para poder acceder a esos datos
        y = respuestaJson["main"]
        # print(y)
        temperatura = y["temp"]
        st = y["feels_like"]
        presionAtmosferica = y["pressure"]
        humedad = y["humidity"]
        aux = respuestaJson["weather"]
        #clima = aux[0]["description"]
        # print(aux[0])
        #print(presionAtmosferica, humedad, clima)
        # Se resta 273 para pasarlo de Kelvin a Celsius
        return (temperatura-273, humedad, aux[0]["main"], presionAtmosferica, st-273)

    elif(respuestaHTTP.status_code == 404):  # codigo 404 es que no se encontró la ciudad
        print("No se encontró la ciudad")

    elif(respuestaHTTP.status_code == 401):  # codigo 401 es de un error en la API
        print("Error en la API. Quizas hay que esperar a que se active")

    else:
        print("El código HTTP fue " + str(respuestaHTTP.status_code))



ciudad = "Buenos Aires"
informacion = obtenerTemperatura(ciudad)

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
print("INFO:", informacion)
temperaturaFeed = aio.feeds('temperatura')
humedadFeed = aio.feeds('humedad')
climaFeed = aio.feeds('clima')
presionFeed = aio.feeds('presion')
stFeed = aio.feeds('st')
aio.send_data(temperaturaFeed.key, informacion[0])
aio.send_data(humedadFeed.key, informacion[1])
aio.send_data(climaFeed.key, informacion[2])
aio.send_data(presionFeed.key, informacion[3])
aio.send_data(stFeed.key, informacion[4])
