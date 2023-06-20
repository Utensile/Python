import paho.mqtt.client as mqtt
import time 
# MQTT broker details
broker = "f2c6012d6da149d1a59063387a77aa22.s2.eu.hivemq.cloud"
port = 8883
username = "ESP32"
password = "ESP12345"

# MQTT topic and message
topic = "your/topic"
message = "Hello, HiveMQ!"

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(topic)
    else:
        print("Failed to connect, return code: ", rc)

def on_publish(client, userdata, mid):
    print("Message published")

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT broker")

# Create MQTT client
client = mqtt.Client()

# Set MQTT callback functions
client.on_connect = on_connect
client.on_publish = on_publish
client.on_disconnect = on_disconnect

# Set MQTT username and password
client.username_pw_set(username, password)

client.loop_start()
client.connect(broker, port)
while(client.is_connected() == False):
    print("Connecting to MQTT broker...")
    time.sleep(1)
    client.connect(broker, port)
client.publish(topic, message)

# Loop continuously to maintain the connection
client.loop_stop()
