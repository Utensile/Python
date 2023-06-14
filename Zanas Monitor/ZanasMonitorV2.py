import serial
import time
import codecs
import winsound
import threading
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk

# Function to handle opening the serial port
def open_serial_port():
    # Get the serial port name and baud rate from the input fields
    port_name = port_name_entry.get()
    baud_rate = baud_rate_entry.get()

    # Attempt to open the serial port
    try:
        # Open the serial port
        ser = serial.Serial(port_name, baud_rate)

        # If successful, close the window
        root.withdraw()

        # Open a new window using Tkinter
        window = tk.Tk()
        window.title("Zanas Z-3 Series Monitor")  # Add title to the window

        global maxh;
        maxh=0;
        
        def parachute():
            ser.write(b'2')
            launch['text']= "Parachute Deployed!"
            launch['foreground']= "#91030a"
            window.update()
            winsound.Beep(1000, 500)
            if button['text']=="Launch":
                launch['text']='Waiting for Launch...'
                launch['foreground']= gray
            else:
                if button['text']=="Activate":
                    launch['text']='Waiting for Activation...'
                    launch['foreground']= gray
                else:
                    launch['foreground']= '#DDDDDD'
                    launch['text']= "Rocket Ignited"         
            window.update()

        def stopLaunch():
            global stop
            stop=1
        
        def Launch():
            global stop
            stop=0
            if button['text']=="Activate":
                launch['text']='Waiting for Launch...'
                launch['foreground']= gray
                button['text']="Launch"
                button['bg']="#91030a"
                stop=0
            else:
                if button['text']=="Launch":
                    for i in range(5, 0, -1):
                        if(stop!=1):
                            launch['text'] = 'Launch in {}'.format(i)
                            window.update()
                        if(stop!=1):
                            winsound.Beep(800, 300)
                        if(stop!=1):
                            time.sleep(0.7)
                        else:
                            break
                    if(stop!=1):
                        ser.write(b'1')
                        launch['text']= "LAUNCHED!!!"
                        root.update()
                        winsound.Beep(1000, 1000)
                        launch['text']= "Rocket Ignited"
                        launch['foreground']= '#DDDDDD'
                        button['text']="Reset"
                        button['bg']=gray
                    else:
                        launch['text']='Waiting for Launch...'
                        launch['foreground']= gray
                        button['text']="Launch"
                        button['bg']="#91030a"
                    window.update()
                else:
                    if button['text']=="Reset":
                        launch['text']='Waiting for Activation...'
                        launch['foreground']= gray
                        button['text']='Activate'
                        button['bg']=gray
        
        # Make the new window fullscreen
        window.attributes('-fullscreen', True)
        window.configure(bg="#282424")
        # Set the font size and color for the serial reader window
        serial_label_font = ('Helvetica', 200)
        serial_label_color = 'white'
        alt_label_font = ('Helvetica', 150, "bold")
        crimson = '#DC143C'
        gray="#8C92AC"

        # Add a label to the window for displaying serial data
        alt_label = ttk.Label(window, text="Altitude:", font=alt_label_font, foreground=crimson, background="#282424")
        alt_label.pack(anchor='center')
        serial_label = ttk.Label(window, text="Awaiting Data...", font=serial_label_font, foreground=serial_label_color, background="#282424")
        serial_label.pack(anchor='center')

        button = tk.Button(window, text="Activate", font=("Helvetica", 100, "bold"), bg=gray, foreground='white', relief='raised', bd=20, command=Launch, width=int(root.winfo_screenwidth()/2))
        button.pack(pady=20)
        launch = ttk.Label(window, text="Waiting for Activation...", font=('Helvetica', 100), foreground=gray, background="#282424")
        launch.pack(anchor='center', pady=20)

        maxhLabel = ttk.Label(window, text="Max Height: 0.00 m", font=('Helvetica', 80, "bold"), foreground="#D89216", background="#282424")
        maxhLabel.pack(anchor='center', pady=20)

        para_button = tk.Button(window, text="Emergency Parachute", font=("Helvetica", 20), bg="#91030a", foreground='white', relief='raised', bd=10, command=parachute)
        stop_button = tk.Button(window, text="Stop Launch", font=("Helvetica", 20), bg="#91030a", foreground='white', relief='raised', bd=10, command=stopLaunch)
        para_button.place(x=root.winfo_screenwidth()/2.6, y=root.winfo_screenheight()*0.89)
        stop_button.place(x=root.winfo_screenwidth()/1.9, y=root.winfo_screenheight()*0.89)
        # Function to read serial data and update the label
        def read_serial():
            while True:
                global maxh
                data = ser.readline().decode().strip()
                serial_label.configure(text=data)
                if(data[0].isnumeric()):
                    res = ''
                    for i in range(0, len(data)):
                        if data[i]!=" ":
                            res = res + data[i]
                        else:
                            break
                    if(float(res)>maxh):
                        maxh=float(res)
                        maxhLabel.configure(text="Max Height: "+str(maxh)+" m")

        
        
        # Start reading serial data in a separate thread
        t = threading.Thread(target=read_serial)
        t.start()

        window.mainloop()

    except serial.SerialException as e:
        # Display error message in a messagebox
        messagebox.showerror("Error", str(e))

def parachute():
    global stop


def stopLaunch():
    global stop

# Create the main Tkinter window
root = tk.Tk()
root.title("Configurazione Seriale Zanas")  # Add title to the window
root.configure(bg="#282424")

# Configure the window size
root.geometry("600x300")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (600 / 2))
y = int((screen_height / 2) - (300 / 2))
root.geometry(f"600x300+{x}+{y}")

# Add labels and input fields to the window with padding
port_name_label = ttk.Label(root, text="Serial Port Name:",font=("Helvetica", 17), background="#282424", foreground="#DDDDDD")
port_name_label.grid(row=0, column=0, padx=10, pady=10)  # Add port_name_label to the window with padding

port_name_entry = ttk.Entry(root, font=("Helvetica", 20))
port_name_entry.grid(row=0, column=1, padx=10, pady=10)  # Add port_name_entry to the window with padding
port_name_entry.insert(0, "COM");

baud_rate_label = ttk.Label(root, text="Baud Rate:",font=("Helvetica", 20), background="#282424", foreground="#DDDDDD")
baud_rate_label.grid(row=1, column=0, padx=10, pady=10)  # Add baud_rate_label to the window with padding

baud_rate_entry = ttk.Entry(root, font=("Helvetica", 20))
baud_rate_entry.insert(0, "9600");
baud_rate_entry.grid(row=1, column=1, padx=10, pady=10)  # Add baud_rate_entry to the window with padding

# Add a button to the window with padding
open_button = tk.Button(root, text="Avvia Monitor Zanas", font=("Helvetica", 25), command=open_serial_port)
open_button.grid(row=2, column=0, columnspan=2, pady=40)  # Add open_button to the window

# Run the Tkinter event loop
root.mainloop()
