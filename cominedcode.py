import tkinter as tk
import random
import time
import cv2
import datetime

# Define emoji representations for happy and sad faces
happy_face = "😊"
sad_face = "😢"

# Define the simulated serial port data
def get_simulated_serial_data():
    # Simulate random speed within a range (adjust as needed)
    return random.uniform(0, 80)

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

# Function to update the displayed data and check speed limit
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
        
        # Capture image on speed limit exceeded
        capture_image()

    # Schedule the next update
    window.after(1000, update_data)  # Update every 1000 milliseconds (1 second)

# Function to capture image and save with timestamp
def capture_image():
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture image from webcam")
        return

    # Generate a unique filename using timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"captured_image_{timestamp}.jpg"

    # Save the captured image
    cv2.imwrite(filename, frame)

    print(f"Image captured successfully as '{filename}'")

# Create a Tkinter window
window = tk.Tk()
window.title("Speed Data Display")

# Create labels for speed, emoji, and status
speed_label = tk.Label(window, text="Current Speed: 0 km/h", font=("Arial Black", 60))
speed_label.pack(pady=20)

emoji_label = tk.Label(window, text="", font=("Arial", 170))
emoji_label.pack(pady=20)

status_label = tk.Label(window, text="", font=("Arial", 70))
status_label.pack()

# Call the update_data function to start displaying data
update_data()

# Run the Tkinter event loop
window.mainloop()

# Release the webcam at the end
cap.release()
