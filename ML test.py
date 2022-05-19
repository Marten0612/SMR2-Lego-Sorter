import torch

#Global variables
conf_tresh = 0.9 #Confidence treshold

#These are the groups we will put in our machine
brick = ['3005_1x1_Brick', '3004_1x2_Brick', '3622_1x3_Brick', '3010_1x4_Brick', \
          '3009_1x6_Brick', '3008_1x8_Brick', '6111_1x10_Brick']
block = ['3003_2x2_Block', '3002_2x3_Block', '3001_2x4_Block', '2456_2x6_Block', \
          '3007_2x8_Block', '3006_2x10_Block']
plate = ['3024_1x1_Plate', '3023_1x2_Plate', '3623_1x3_Plate', '3710_1x4_Plate', \
         '78329_1x5_Plate', '3666_1x6_Plate', '3460_1x8_Plate', '4477_1x10_Plate']
sheet = ['3022_2x2_Sheet', '3021_2x3_Sheet', '3020_2x4_Sheet', '3795_2x6_Sheet', \
         '3034_2x8_Sheet', '3832_2x10_Sheet', '11212_3x3_Sheet', '3031_4x4_Sheet', \
         '3032_4x6_Sheet', '3035_4x8_Sheet', '3030_4x10_Sheet']
tile = ['3070_1x1_Tile', '3069_1x2_Tile', '63864_1x3_Tile', '2431_1x4_Tile', \
         '6636_1x6_Tile', '4162_1x8_Tile', '3068_2x2_Tile', '26603_2x3_Tile', \
         '87079_2x4_Tile', '69729_2x6_Tile', '6934a_3x6_Tile']

#These are all the classes of the groups, we will only use an selection of these
all_brick = ['3005_1x1_Brick', '3004_1x2_Brick', '3622_1x3_Brick', '3010_1x4_Brick', \
              '3009_1x6_Brick', '3008_1x8_Brick', '6111_1x10_Brick', '6112_1x12_Brick', \
              '2465_1x16_Brick']
all_block = ['3003_2x2_Block', '3002_2x3_Block', '3001_2x4_Block', '2456_2x6_Block', \
              '3007_2x8_Block', '3006_2x10_Block']
all_plate = ['3024_1x1_Plate', '3023_1x2_Plate', '3623_1x3_Plate', '3710_1x4_Plate', \
             '78329_1x5_Plate', '3666_1x6_Plate', '3460_1x8_Plate', '4477_1x10_Plate', \
             '60479_1x12_Plate']
all_sheet = ['3022_2x2_Sheet', '3021_2x3_Sheet', '3020_2x4_Sheet', '3795_2x6_Sheet', \
             '3034_2x8_Sheet', '3832_2x10_Sheet', '2445_2x12_Sheet', '91988_2x14_Sheet', \
             '4282_2x16_Sheet', '11212_3x3_Sheet', '3031_4x4_Sheet', '3032_4x6_Sheet', \
             '3035_4x8_Sheet', '3030_4x10_Sheet', '3029_4x12_Sheet', '3958_6x6_Sheet', \
             '3036_6x8_Sheet', '3033_6x10_Sheet', '3028_6x12_Sheet', '3456_6x14_Sheet', \
             '3027_6x16_Sheet', '3026_6x24_Sheet', '41539_8x8_Sheet', '728_8x11_Sheet', \
             '92438_8x16_Sheet', '91405_16x16_Sheet']
all_tile = ['3070_1x1_Tile', '3069_1x2_Tile', '63864_1x3_Tile', '2431_1x4_Tile', \
            '6636_1x6_Tile', '4162_1x8_Tile', '3068_2x2_Tile', '26603_2x3_Tile', \
            '87079_2x4_Tile', '69729_2x6_Tile', '6934a_3x6_Tile', '6881_6x6_Tile', \
            '90498_8x16_Tile'] 

# Model
model = torch.hub.load('../yolov5', 'custom', path="best.pt", source='local', _verbose=False)  # local repo
#../yolov5 betekend, pak uit het mapje hierboven (../) het bestandje yolov5.
#custom means that we use a model trained by ourselves, instead of a pretrained one.
#path is the model we use, located in the same file as this code.
#source='local' means that the model used is on this computer.
#_verbose=False, zorgt dat het model niet in de terminal wordt laten zien.

# Images
img0 = 'C:\Users\jipra\Documents\GitHub\SMR2-Lego-Sorter\img0.png'  
img1 = 'C:\Users\jipra\Documents\GitHub\SMR2-Lego-Sorter\img1.png'
img2 = 'C:\Users\jipra\Documents\GitHub\SMR2-Lego-Sorter\img2.png' 
images = [img0, img1, img2]
class_names = [None] * 3

# Go trough all the photo's
for i in range(3):
    img = images[i]
    # Inference
    results = model(img)

    # Results
    data = results.pandas().xyxy[0]
    if len(data) > 1:
        class_names[i] = 'rest'
        continue #He will still check all pictures. Change to break to stop immediately.

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

group = ""
for x in brick:
    if class_part == x:
        group = 'brick'
        break
for x in block:
    if class_part == x:
        group = 'block'
        break
for x in plate:
    if class_part == x:
        group = 'plate'
        break
for x in sheet:
    if class_part == x:
        group = 'sheet'
        break
for x in tile:
    if class_part == x:
        group = 'tile'
        break
if group == 'brick' or group == 'block' or group == 'plate' or group == 'sheet' or group == 'tile':
    pass
else:
    group = 'rest'

print(group)