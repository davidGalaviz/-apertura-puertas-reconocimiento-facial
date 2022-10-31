from deepface import DeepFace
from paho.mqtt import client as mqtt_client
import random
import time

#variables y constantes 
broker_host = '127.0.0.1'
port = 1883
topic = "codigoIoT/mqtt/python"

# ID generado aleatoriamente 
client_id = f'python-mqtt-{random.randint(0, 1000)}'


#Conexion al broker
def connect_mqtt():
    def on_connect(client, userdata, flags,rc):
        if rc == 0:
            print("Conectado a el broker de MQTT!")
        else:
            print("No se pudo conectar, return code %d\n",rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker_host, port)
    return client

def publish(client, msg):
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

df = DeepFace.find (img_path = "/home/david/Documentos/Git/-apertura-puertas-reconocimiento-facial/deepFace/Elizabeth-olsen.jpg", db_path = "/home/david/Documentos/Git/-apertura-puertas-reconocimiento-facial/deepFace/my_db")
print("Resultado ")
print(type(df))
#Convertir de pandas a JSON 
json_view = df.to_json(orient="index")
print("La exprision en JSON de los resultados es : ")
print(json_view)

#Envio
client = connect_mqtt()
client.loop_start()
publish(client, json_view)