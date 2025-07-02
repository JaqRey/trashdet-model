from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("best.pt")

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model.predict(source=frame, save=False, conf=0.3, stream=True)

    # Visualize results on frame
    for r in results:
        annotated_frame = r.plot()

    # Display the frame
    cv2.imshow("YOLOv10 Webcam Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
