import serial
import tkinter as tk

# Define the serial port and baud rate
port = '/dev/ttyACM0'  # Change this to the correct port for your device
baud_rate = 9600  # Change this to the baud rate of your device

# Initialize the serial connection
ser = serial.Serial(port, baud_rate, timeout=1)

# Check if the connection is open
if ser.isOpen():
    print("Serial connection established successfully.")
else:
    print("Failed to establish serial connection.")

# Create a Tkinter window
window = tk.Tk()
window.title("Radar Data Display")

# Create a label to display the received data
data_label = tk.Label(window, text="Waiting for data...", font=("Arial Black", 500))
data_label.pack(pady=40)

# Function to update the displayed data
def update_data():
    data = ser.readline().decode().strip()  # Decode bytes to string and remove leading/trailing whitespace
    if data:
        velocity_mps = float(data)
        data_label.config(text=int(velocity_mps))
    window.after(100, update_data)  # Update every 100 milliseconds

# Call the update_data function to start displaying data
update_data()

# Run the Tkinter event loop
window.mainloop()

# Remember to close the serial connection when you're done
ser.close()
