from ultralytics import YOLO

# Load your trained model
model = YOLO("best.pt")

# Run inference on a single image
results = model("images/test/sample.jpg")  # or a directory

# Show results (bounding boxes, etc.)
results[0].show()

# Save output to file
results[0].save(filename="output.jpg")

# Optional: print detections
for box in results[0].boxes:
    print(f"Class: {int(box.cls[0])}, Confidence: {box.conf[0]:.2f}")
 