import mtcnn 
from mtcnn.mtcnn import MTCNN
import cv2 
import os
import numpy as np

confidence_threshold = 0.97

detector = MTCNN()
def detection(input):
    #gray_input = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
    results = detector.detect_faces(input)
    face_count = len(results)
    
    for res in results:
        x1, y1, width, height = res['box']
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height

        confidence = res['confidence']
        if confidence < confidence_threshold:
            face_count -= 1
            continue

        cv2.rectangle(input, (x1, y1), (x2, y2), (255, 0, 0), thickness=2)    
        cv2.putText(input, f'conf: {confidence:.3f}', (x1, y1), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)
        
    print("Number of faces : ",face_count)
    return results,input

def labels_for_training_data(directory):
    faces =[]
    faceID =[]

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filenames.startswith("."):
                print("Skipping System files")
                continue
            
            id = os.path.basename(path)
            img_path = os.path.join(path,filenames)
            print("Image path :" , img_path)
            print("Id: ",id)
            input = cv2.imread(img_path)

            if input is None:
                print("Image no loaded properly")
                # skipping if image is not proper
                continue
            faces_rect,img = detection(input)
            if len (faces_rect!=1):
                # if training image consist more than one face skip it
                continue
            (x,y,w,h) = faces_rect[0]
            # taking region of interest
            roi = img[y:y+w, x:x+h]
            faces.append()
            faceID.append(int(id)) 
return faces,faceID