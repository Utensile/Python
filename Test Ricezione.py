import serial # import serial library
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import codecs
# open serial port
ser = serial.Serial('COM5', 9600)

# set font and size
fig = plt.figure(figsize=(15, 10))

# define callback for button press
def press_button(event):
    print('Pressed!')

# add button
fig2 = plt.figure()
axbutton = fig2.add_axes([0.25, 0.25, 50, 25])
btn = Button(axbutton, 'Change Color')
btn.on_clicked(press_button)

while True:
    # read double from serial port
    double_value = ser.readline()
    double_value = codecs.decode(double_value).strip() # strip /n at the end
    
    # update text
    fig.texts = [] # clear previous texts
    fig.text(0.2, 0.3, 'Altitude: ' + double_value + ' m', fontsize=100, style='oblique', color='red') # center text
    plt.draw()
    plt.pause(0.0001)
    print(double_value)
