from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import numpy as np
import cv2
import dlib
from math import *
import json
import ast 


class combination:

        def narrowEyebrow(self):
            x_dist = abs(self.shape.part(22).x - self.shape.part(21).x)
            y_dist = abs(self.shape.part(22).y - self.shape.part(21).y)

            dist1 = pow(x_dist,2) + pow(y_dist,2)
            dist = sqrt(dist1)
            self.featureDist.update({'eyeBrowNarrow' : dist})


        def farEyebrow(self):
            x_dist = abs(self.shape.part(26).x - self.shape.part(17).x)
            y_dist = abs(self.shape.part(26).y - self.shape.part(17).y)

            dist1 = pow(x_dist,2) + pow(y_dist,2)
            dist = sqrt(dist1)
            self.featureDist.update({'eyeBrowFar' : dist})

        def eyeHeight(self):
            x_dist = abs(self.shape.part(43).x - self.shape.part(47).x)
            y_dist = abs(self.shape.part(43).y - self.shape.part(47).y)

            dist1 = pow(x_dist,2) + pow(y_dist,2)
            dist = sqrt(dist1)
            self.featureDist.update({'eyeHeight' : dist})

        def noseLength(self):
            x_dist = abs(self.shape.part(27).x - self.shape.part(33).x)
            y_dist = abs(self.shape.part(27).y - self.shape.part(33).y)

            dist1 = pow(x_dist,2) + pow(y_dist,2)
            dist = sqrt(dist1)
            self.featureDist.update({'noseLength' : dist})
            
        def noseWidth(self):
            x_dist = abs(self.shape.part(35).x - self.shape.part(31).x)
            y_dist = abs(self.shape.part(35).y - self.shape.part(31).y)

            dist1 = pow(x_dist,2) + pow(y_dist,2)
            dist = sqrt(dist1)
            self.featureDist.update({'noseWidth' : dist})
            
        def lipWidth(self):
            x_dist = abs(self.shape.part(54).x - self.shape.part(48).x)
            y_dist = abs(self.shape.part(54).y - self.shape.part(48).y)

            dist1 = pow(x_dist,2) + pow(y_dist,2)
            dist = sqrt(dist1)
            self.featureDist.update({'lipWidth' : dist})

        def lipHeight(self):
            x_dist = abs(self.shape.part(50).x - self.shape.part(58).x)
            y_dist = abs(self.shape.part(50).y - self.shape.part(58).y)

            dist1 = pow(x_dist,2) + pow(y_dist,2)
            dist = sqrt(dist1)
            self.featureDist.update({'lipHeight' : dist})

        def jawWidth(self):
            x_dist = abs(self.shape.part(12).x - self.shape.part(4).x)
            y_dist = abs(self.shape.part(12).y - self.shape.part(4).y)

            dist1 = pow(x_dist,2) + pow(y_dist,2)
            dist = sqrt(dist1)
            self.featureDist.update({'jawWidth' : dist})

        def headWidth(self):
            x_dist = abs(self.shape.part(15).x - self.shape.part(1).x)
            y_dist = abs(self.shape.part(15).y - self.shape.part(1).y)

            dist1 = pow(x_dist,2) + pow(y_dist,2)
            dist = sqrt(dist1)
            self.featureDist.update({'headWidth' : dist})
            
        def execute_test(self, filename, dict_name):
                detect = dlib.get_frontal_face_detector() 
                predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

                vs = VideoStream(-1).start()
                time.sleep(2.0)
                self.featureDist = {}

                while 1:
                    frame = vs.read()
                    frame = imutils.resize(frame, width=400)
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
                    clahe_image = clahe.apply(gray)
                    faces = detect(clahe_image, 0)
                    for a,b in enumerate(faces):
                        self.shape = predictor(clahe_image, b)
                
                        for i in range(1,68):
                            cv2.circle(frame, ((self.shape.part(i).x), (self.shape.part(i).y)), 1, (0,0,255), thickness = 1)
                    
                        enter_key = cv2.waitKey(1) & 0xFF
                
                        if (enter_key == 10):
                            self.narrowEyebrow()
                            self.farEyebrow()
                            self.eyeHeight()
                            self.noseLength()
                            self.noseWidth()
                            self.lipWidth()
                            self.lipHeight()
                            self.jawWidth()
                            self.headWidth()
                            
                            self.file_object = open(filename + '.txt' ,"a")
                            self.final_dict = {}
                            self.final_dict[dict_name]=self.featureDist
                            self.file_object.write(json.dumps({self.final_dict}))
                            self.file_object.close()
                            enter_key = ord('q')
                            break
                            
                    cv2.imshow("Frame",frame) 
                    if enter_key == ord('q'):
                        cv2.destroyAllWindows()
                        break
        

        def execute_train(self, filename, dict_name):
                detect = dlib.get_frontal_face_detector() 
                predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

                vs = VideoStream(-1).start()
                time.sleep(2.0)
                self.featureDist = {}

                while 1:
                    frame = vs.read()
                    frame = imutils.resize(frame, width=400)
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
                    clahe_image = clahe.apply(gray)
                    faces = detect(clahe_image, 0)
                    self.final_dict = {}
                    for a,b in enumerate(faces):
                        self.shape = predictor(clahe_image, b)
                
                        for i in range(1,68):
                            cv2.circle(frame, ((self.shape.part(i).x), (self.shape.part(i).y)), 1, (0,0,255), thickness = 1)
                    
                        enter_key = cv2.waitKey(1) & 0xFF

                        if enter_key == 10:
                            self.narrowEyebrow()
                            self.farEyebrow()
                            self.eyeHeight()
                            self.noseLength()
                            self.noseWidth()
                            self.lipWidth()
                            self.lipHeight()
                            self.jawWidth()
                            self.headWidth()

                            with open(filename + '.txt', "a+") as f:
                                    data_dict = f.readlines()

                            data_dict = ast.literal_eval(json.dumps(data_dict))
                            
                            self.final_dict = eval(data_dict[0])
                            self.final_dict[dict_name] = self.featureDist
                            
                            self.file_object = open(filename + '.txt' , 'w+')
                            self.file_object.write((str(self.final_dict)))
                            self.file_object.close()

                            enter_key = ord('q')
                            break
                            
                    cv2.imshow("Frame",frame) 
                    if enter_key == ord('q'):

                        vs.stop()
                        cv2.destroyAllWindows()
                        break
            
    
