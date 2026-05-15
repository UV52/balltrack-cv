from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Run detection
results = model("test.jpg", save=True)

print("Detection complete")