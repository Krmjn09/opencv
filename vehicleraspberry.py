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

# Configure the main window padding
window.configure(padx=20, pady=20)

# Create labels for speed, emoji, and status with increased fonts and padding
speed_label = tk.Label(window, text="Current Speed: 0 km/h", font=("Arial Black", 60), pady=20)
speed_label.pack()

emoji_label = tk.Label(window, text="", font=("Arial", 170), pady=20)
emoji_label.pack()

status_label = tk.Label(window, text="", font=("Arial", 70), pady=20)
status_label.pack()

# Define emoji representations for happy and sad faces
happy_face = "😊"
sad_face = "😢"

# Function to update the displayed data
def update_data():
    data = ser.readline().decode().strip()  # Decode bytes to string and remove leading/trailing whitespace
    if data:
        velocity_mps = abs(float(data))
        
        # Update speed label
        speed_label.config(text=f"Current Speed: {int(velocity_mps)} km/h")

        # Define speed limit here (adjust as needed)
        speed_limit = 50  # Adjust this value (in km/h or mph)

        # Show happy face if within limit
        if velocity_mps <= speed_limit:
            emoji_label.config(text=happy_face)
            status_label.config(text="Speed within limit", fg="green")
        # Show sad face if exceeding limit
        else:
            emoji_label.config(text=sad_face)
            status_label.config(text="SPEED LIMIT EXCEEDED", fg="red")

    window.after(100, update_data)  # Update every 100 milliseconds

# Call the update_data function to start displaying data
update_data()

# Center the window on the screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f'{width}x{height}+{x}+{y}')

# Run the Tkinter event loop
window.mainloop()

# Remember to close the serial connection when you're done
ser.close()
