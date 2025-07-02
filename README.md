# Inference Instructions

## Requirements

Install the required Python packages:
```sh
pip install ultralytics opencv-python
```

## Running Inference on Images

1. Place your trained YOLO model file (`best.pt`) in the project directory.
2. Place your test image in a folder, e.g., `images/test/sample.jpg`.
3. Use the provided `inference.py` script to run inference on an image:
    ```sh
    python inference.py
    ```
   - The script will display the detection results and save an output image as `output.jpg`.
   - Detected classes and confidence scores will be printed in the terminal.

## Run on Webcam
1. To run on webcam:
   ```sh
   python cam.py
   ```

## Notes

- Edit the image path in `inference.py` if your test image is in a different location.
- Ensure `best.pt` is the path to your trained YOLO model.
- Both scripts assume you are using the
