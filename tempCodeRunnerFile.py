import tkinter as tk
import random
import time

# Define emoji representations for happy and sad faces
happy_face = "😊"
sad_face = "😢"

# Define the simulated serial port data
def get_simulated_serial_data():
    # Simulate random speed within a range (adjust as needed)
    return random.uniform(0, 80)

# Function to update the displayed data
def update_data():
    velocity_mps = get_simulated_serial_data()
    
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

    # Schedule the next update
    window.after(1000, update_data)  # Update every 1000 milliseconds (1 second)

# Create a Tkinter window
window = tk.Tk()
window.title("Speed Data Display")

# Create labels for speed, emoji, and status
speed_label = tk.Label(window, text="Current Speed: 0 km/h", font=("Arial Black", 60))
speed_label.pack(pady=20)

emoji_label = tk.Label(window, text="", font=("Arial", 100))
emoji_label.pack()

status_label = tk.Label(window, text="", font=("Arial", 70))
status_label.pack()

# Call the update_data function to start displaying data
update_data()

# Run the Tkinter event loop
window.mainloop()
