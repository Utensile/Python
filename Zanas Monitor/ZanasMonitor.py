import serial
import time
import codecs
import winsound
import tkinter
from tkinter import *
from PIL import Image, ImageTk

stop=0

# Create the root window
root = Tk()
root.attributes('-fullscreen', True)

# Start the Serial
ser = serial.Serial('COM6', 9600)

root.title('Zanas Z-3 Series Monitor')

# Add Logo
image = Image.open("zanas.png")
width, height = image.size
image = image.resize((int(width * 1.5), int(height * 1.5)))
photo_image = ImageTk.PhotoImage(image)
logo1 = Label(root, image=photo_image)
logo1.pack(side='right', padx=100)
logo2 = Label(root, image=photo_image)
logo2.pack(side='left', padx=100)

# Create the label
alt_label = Label(root, text='Altitude:', font=('Helvetica', 150), fg='#A10000')
alt_label.pack(anchor=CENTER)
alt_value = Label(root, text='0.00 m', font=('Helvetica', 200), fg='black')
alt_value.pack(anchor=CENTER)


# Create the button
button = Button(root, text='Activate', font=('Helvetica', 100), relief=RAISED, bd=20, background='#555555', activeforeground='#BBBBBB',activebackground='#333333', fg='white', command=lambda: Launch())
button.pack(anchor=CENTER)

launch = Label(root, text='Waiting for Activation...', font=('Helvetica', 100), fg='gray')
launch.pack(anchor=CENTER)

# Create the small button
para_button = Button(root, text='Emergency Parachute', font=('Helvetica', 20), relief=RAISED, bd=10, background='#A10000', fg='white', command=lambda: parachute())
para_button.pack(anchor=CENTER, padx=10, pady=100)

# Create the small button 2
stop_button = Button(root, text='Stop Launch', font=('Helvetica', 20), relief=RAISED, bd=10, background='#A10000', fg='white', command=lambda: stopLaunch())
stop_button.pack(anchor=CENTER, padx=10)

# Parachute function
def parachute():
    ser.write(b'2')
    launch['text']= "Parachute Deployed!"
    launch['fg']= 'red'
    root.update()
    winsound.Beep(1000, 500)
    if button['text']=="Launch":
        launch['text']='Waiting for Launch...'
        launch['fg']= 'gray'
    else:
        if button['text']=="Activate":
            launch['text']='Waiting for Activation...'
            launch['fg']= 'gray'
        else:
            launch['text']= "Rocket Ignited"
            launch['fg']= '#003B59'
    root.update()

 
def stopLaunch():
    global stop
    stop=1


def Launch():
    global stop
    stop=0
    if button['text']=="Activate":
        launch['text']='Waiting for Launch...'
        launch['fg']= 'gray'
        button['text']="Launch"
        stop=0
    else:
        if button['text']=="Launch":
            for i in range(5, 0, -1):
                if(stop!=1):
                    launch['text'] = 'Launch in {}'.format(i)
                    root.update()
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
                launch['fg']= '#003B59'
                button['text']="Reset"
            else:
                launch['text']='Waiting for Launch...'
                launch['fg']= 'gray'
                button['text']="Launch"
            root.update()
        else:
            if button['text']=="Reset":
                launch['text']='Waiting for Activation...'
                launch['fg']= 'gray'
                button['text']='Activate'
    
    
while True:
    # Set serial communication port and baud rate
    data=ser.readline()
    # Read and decode double value from serial port
    data = codecs.decode(data).strip()
    # Change the label text
    alt_value['text'] = '{} m'.format(data)
    root.update()




