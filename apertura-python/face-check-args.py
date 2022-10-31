from deepface import DeepFace
from paho.mqtt import client as mqtt_client
import argparse
import pandas as pd
import random
import time

#variables y constantes 
broker = '127.0.0.1'
port = 1883
topic = "codigoIoT/mqtt/python"

# ID generado aleatoriamente 
client_id = f'python-mqtt-{random.randint(0, 1000)}'

#parser
parser = argparse.ArgumentParser()
parser.add_argument("img_path", help="Ruta de la imagen a buscar en la DB")
parser.add_argument("db_path", help="Ruta de la base de datos de caras")
args = parser.parse_args()

#Conexion al broker
def connect_mqtt():
    def on_connect(client, userdata, flags,rc):
        if rc == 0:
            print("Conectado a el broker de MQTT!")
        else:
            print("No se pudo conectar, return code %d\n",rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, mensaje):
    time.sleep(1)
    msg = mensaje
    result = client.publish(topic, msg)
    time.sleep(1)
    print(result)

    status = result[0]
    if status == 0:
        print(f"Send`{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic `{topic}`")

#Buscar rostro

print("Buscando rostro")

df = DeepFace.find (img_path = args.img_path, db_path = args.db_path)
print("Resultado ")
print(df)
#Convertir de pandas a JSON 
json_view = df.to_json(orient="index")
print("La exprision en JSON de los resultados es : ")
print(json_view)

#Envio
client = connect_mqtt()
client.loop_start()
publish(client, json_view)