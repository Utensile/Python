import tkinter as tk
from tkinter import messagebox
import socket

def send_command():
    host = ip_entry.get()    # IP address of the ESP32
    port = 1234             # Port number on which ESP32 is listening
    command = command_entry.get()  # Command entered in the entry field
    
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the ESP32
        client_socket.connect((host, port))
        
        # Send the command to the ESP32
        client_socket.sendall(command.encode())
        print("Command sent to ESP32:", command)
        
    except ConnectionRefusedError:
        error_message = "Failed to connect to the ESP32."
        messagebox.showerror("Connection Error", error_message)
        
    finally:
        # Close the socket
        client_socket.close()

# Create the tkinter window
window = tk.Tk()
window.title("Wireless Button")
window.geometry("300x150")

# IP address entry field
ip_label = tk.Label(window, text="ESP32 IP Address:")
ip_label.pack()
ip_entry = tk.Entry(window)
ip_entry.pack()

# Command entry field
command_label = tk.Label(window, text="Command:")
command_label.pack()
command_entry = tk.Entry(window)
command_entry.pack()

# Create the button
button = tk.Button(window, text="Press me", command=send_command)
button.pack()

# Start the tkinter event loop
window.mainloop()
