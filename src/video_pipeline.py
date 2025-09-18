import cv2
import torch
import torchvision.transforms as transforms
from torchvision import models

# Load pretrained ResNet as dummy classifier
model = models.resnet18(pretrained=True)
model.eval()

# Image preprocessing (match training input size)
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        # Only process every 30th frame for speed
        if frame_count % 30 == 0:
            img_tensor = transform(frame).unsqueeze(0)
            with torch.no_grad():
                outputs = model(img_tensor)
                _, predicted = torch.max(outputs, 1)

            print(f"Frame {frame_count}: Predicted class {predicted.item()}")

    cap.release()
    cv2.destroyAllWindows()
