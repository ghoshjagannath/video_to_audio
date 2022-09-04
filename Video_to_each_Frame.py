import cv2  
from pathlib import Path 
import os
import easyocr


#reverse the video 
#reading any text in that file


###In this programe we will add a video file then we will segeregate frame by 
#frame and  try to find if there are any type of text in that frame


# os.chdir(r"C:/Users/ghosh/AppData/Local/Programs/Python/Python39/video_to_transcript_complete/photo_folder")
#video path 
path=r"C:/Users/ghosh/Downloads/demofile_youtube .mp4"

#reading the video format 
capture=cv2.VideoCapture(path)

#for naming purpose of frame  we will use frame no Pytho
#which will increase +1 each type of below mentioned loop 
frame_no=0
pre_result=''

reader = easyocr.Reader(['en'])

while (capture.isOpened()):
    # Capture frame-by-frame
    ret, frame = capture.read()
    frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,interpolation = cv2.INTER_CUBIC)
    path=f"C:/Users/ghosh/AppData/Local/Programs/Python/Python39/video_to_transcript_complete/photo_folder/photo{frame_no}.jpg"
    cv2.imwrite(path,frame)
    result = reader.readtext(path)
    # print(os.getcwd())
    os.remove(path)
    
    try:
        if result[0][2]>.5 and result!=pre_result:
            print(result)
        elif result==pre_result:
            pre_result=result
    except IndexError:
        print(result)
    frame_no+=1

    if cv2.waitKey() & 0xFF == ord('q'):
        break
 
capture.release()
 
# Closes all the windows currently opened.
cv2.destroyAllWindows()

