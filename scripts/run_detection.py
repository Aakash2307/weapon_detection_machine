from ultralytics import YOLO
import cv2
import os

# Load your trained model
model = YOLO("best.pt")  # replace with your trained weights

# Input and output folders
input_folder = "frames/test_video2"
output_folder = "frames_detected/test_video3"
os.makedirs(output_folder, exist_ok=True)

# Process all frames
frame_files = sorted(os.listdir(input_folder))  # ensure correct order
for frame_file in frame_files:
    img_path = os.path.join(input_folder, frame_file)
    
    # Run detection
    results = model(img_path)
    
    # Get the image with boxes drawn
    detected_img = results[0].plot()  # returns image with bounding boxes
    
    # Save output frame
    cv2.imwrite(os.path.join(output_folder, frame_file), detected_img)

print(f"All frames processed and saved in {output_folder}")
