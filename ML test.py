import torch

#Global variables
conf_tresh = 0,9 #Confidence treshold

# Model
model = torch.hub.load('../yolov5', 'custom', path="best.pt", source='local')  # local repo

# Images
img1 = 'C:\Users\jipra\Documents\GitHub\SMR2-Lego-Sorter\img1.png'  # or file, Path, PIL, OpenCV, numpy, list
img2 = 'C:\Users\jipra\Documents\GitHub\SMR2-Lego-Sorter\img2.png'
img3 = 'C:\Users\jipra\Documents\GitHub\SMR2-Lego-Sorter\img3.png' 
imges = [img1,img2,img3]
class_names = [None]*3

#Go trough al the photo's
for i in range(3):
    img = imges[i]
    # Inference
    results = model(img)

    # Results
    results.print() # or .show(), .save(), .crop(), .pandas(), etc.

    data = results.pandas().xyxy[0]
    confidence = data.iloc[0]['confidence']
    class_names[i] = data.iloc[0]['name']
    print("Confidence = {}\nClass = {}".format(confidence, class_names[i]))
    if confidence < conf_tresh:
        class_names[i] = 'rest'


# Determine what class the part is
if (class_names[0] == class_names[1]) and (class_names[0] == class_names[2]):
    class_part = class_names[0]
elif (class_names[0] == class_names[0]):
    class_part = class_names[0]
elif (class_names[0] == class_names[2]):
    class_part = class_names[0]
elif (class_names[0] == class_names[2]):
    class_part = class_names[0]
else:
    class_part = 'rest'

