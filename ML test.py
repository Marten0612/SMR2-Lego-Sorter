import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
model = torch.hub.load('../yolov5', 'custom', path="Models/labels.pt", source='local')  # local repo
# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)
results.pandas().xyxy[0].to_json(orient="records")
# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.cl