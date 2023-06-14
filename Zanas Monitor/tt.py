import tkinter as tk
import serial

# Create a Tkinter window
root = tk.Tk()

# Create a label to display the data
label = tk.Label(root, text="Data from Arduino: ")
label.pack()

# Open the serial port
ser = serial.Serial('COM6', 9600) 

# Function to read data from Arduino and update the label
def read_serial():
    data = ser.readline().decode().strip()
    label.config(text="Data from Arduino: {}".format(data))
    root.after(100, read_serial)

read_serial()

root.mainloop()
