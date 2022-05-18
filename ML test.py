import torch

#Global variables
conf_tresh = 0.9 #Confidence treshold
 
# Model
model = torch.hub.load('../yolov5', 'custom', path="best.pt", source='local')  # local repo
#path is the model we use

# Images
img0 = 'C:\Users\jipra\Documents\GitHub\SMR2-Lego-Sorter\img0.png'  
img1 = 'C:\Users\jipra\Documents\GitHub\SMR2-Lego-Sorter\img1.png'
img2 = 'C:\Users\jipra\Documents\GitHub\SMR2-Lego-Sorter\img2.png' 
images = [img0, img1, img2]
class_names = [None] * 3

#Go trough al the photo's
for i in range(3):
    img = images[i]
    # Inference
    results = model(img)

    # Results
    data = results.pandas().xyxy[0]
    confidence = data.iloc[0]['confidence']
    if confidence < conf_tresh:
        class_names[i] = 'rest'
    else:
        class_names[i] = data.iloc[0]['name']

# Determine what class the part is
if (class_names[0] == class_names[1]) and (class_names[1] == class_names[2]):
    class_part = class_names[0]
elif (class_names[0] == class_names[1]):
    class_part = class_names[0]
elif (class_names[1] == class_names[2]):
    class_part = class_names[1]
elif (class_names[0] == class_names[2]):
    class_part = class_names[0]
else:
    class_part = 'rest'

print(class_part)