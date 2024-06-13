import cv2
import datetime

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

try:
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture image from webcam")
            continue

        # Simulate speed data (replace with actual data reading logic if available)
        velocity_mps = 60  # Example: simulate speed of 60 km/h

        # Define speed limit here (adjust as needed)
        speed_limit = 50  # Adjust this value (in km/h or mph)

        # Capture image on speed limit exceeded
        if velocity_mps > speed_limit:
            # Generate a unique filename using timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"captured_image_{timestamp}.jpg"

            # Save the captured image
            cv2.imwrite(filename, frame)

            print(f"Image captured successfully as '{filename}'")

            # Optional: You can break out of the loop if you only want to capture one image
            break

finally:
    # Release the webcam
    cap.release()
