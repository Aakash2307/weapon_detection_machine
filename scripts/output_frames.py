import cv2
import os

input_folder = "frames_detected/"
output_video_1 = "output_detected_video.mp4"

# Get sorted list of frames
frame_files = sorted(os.listdir(input_folder))
first_frame = cv2.imread(os.path.join(input_folder, frame_files[0]))
height, width, layers = first_frame.shape

# Define video writer
fps = 30  # use the original video fps, change if different
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec
out = cv2.VideoWriter(output_video_1, fourcc, fps, (width, height))

# Write frames to video
for frame_file in frame_files:
    frame = cv2.imread(os.path.join(input_folder, frame_file))
    out.write(frame)

out.release()
print(f"Video saved as {output_video_1}")
