import tkinter as tk
import paho.mqtt.client as mqtt

# MQTT broker information
broker_url = "f2c6012d6da149d1a59063387a77aa22.s2.eu.hivemq.cloud"
broker_port = 8883
broker_ws_port = 8884

# MQTT topic to publish the button press event
topic = "button_press"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Failed to connect to MQTT broker")

def on_publish(client, userdata, mid):
    print("Button press event published to MQTT broker")

def on_button_press():
    client = mqtt.Client()
    client.username_pw_set(username="", password="")
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.tls_set()
    client.connect(broker_url, broker_port)

    # Publish a message indicating the button press
    client.publish(topic, "Button pressed")

    # Disconnect from the MQTT broker
    client.disconnect()

root = tk.Tk()

# Create a button
button = tk.Button(root, text="Press Me", command=on_button_press)
button.pack()

root.mainloop()
