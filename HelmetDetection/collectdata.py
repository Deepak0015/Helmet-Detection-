import cv2 
import os
import time  

output_dir =  '/home/saaho/THYTECH/HelmetDetection/HelmetDetection/Data/CaptureImages'

num_samples =  25

cap = cv2.VideoCapture(0)

for image_num in range(num_samples):
    print("Collecting the images")
    ret , frame = cap.read()
    file_path = os.path.join(output_dir , f'saahohelmetimage_{image_num}.jpg')
    cv2.imwrite(file_path , frame)
    cv2.imshow('frame' , frame)
    time.sleep(0.5)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 



cap.release()
cv2.destroyAllWindows()
 
