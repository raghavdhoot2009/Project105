import os
import cv2

vid = cv2.VideoCapture(0)

if(vid.isOpened()==False):
    print("UNABLE")

path = "images/"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images[0])

Height = (vid.get(cv2.Cap_PROP_FRAME_HEIGHT))
Width = (vid.get(cv2.Cap_PROP_FRAME_WIDTH))
fps = (vid.get(cv2.Cap_PROP_FPS))
frame.shape = (Height,Width,fps)

size = (Width,Height)

out = cv2.VideoWriter('Video with friends by RD',
  cv2.VideoWriter_fourcc(*'DIVX'),
  0.8,size)

for i in range(0,count-1):
    cv2.imread()
    out.write()

print("Done")