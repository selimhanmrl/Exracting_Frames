import cv2
import os

main_path = os.getcwd()
import os
for root, dirs, files in os.walk(main_path):
    for file in files:
        if file.endswith(".mp4"):
            video_name = file
            filename, file_extension = os.path.splitext(video_name)
            vidcap = cv2.VideoCapture(video_name)
            if not os.path.exists(filename):
                os.mkdir(filename)
                success,image = vidcap.read()
                count = 0
                path = os.getcwd()+"\\"+filename
                while success:
                    cv2.imwrite(path +f"\\img{count}.jpg ", image)     # save frame as JPEG file
                    #cv2.imwrite(os.path.join(path , 'waka.jpg'), img)      
                    success,image = vidcap.read()
                    #print(f'Read a new frame: ', success)
                    count += 1
