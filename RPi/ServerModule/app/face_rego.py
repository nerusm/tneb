__author__ = 'suren'
from PIL import Image

from app.config import Config
import face_recognition
import cv2
import os
import time
from FaceEncodings import FaceEncodings
import numpy as np

class Face_Recog:

    def __init__(self, image_name):
        self.config = Config()
        self.image_name = image_name
        self.known_face_encds = []
        self.fr_tolerance_value = float(self.config.get_common_param('FR_TOLERANCE_VALUE') )

    def get_face_encodings(self,image_name):
        image = face_recognition.load_image_file(image_name)
        cv2.imshow("detected face",image)
        small_frame = cv2.resize(image, (0, 0), fx=0.50, fy=0.50)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encoding = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # print(face_encoding)

        return face_encoding

    def get_known_face_encodings(self,image_name):
        image = face_recognition.load_image_file(image_name)
        # cv2.imshow("KNown face",image)


        # face_locations = face_recognition.face_locations(image)
        face_encoding = face_recognition.face_encodings(image)[0]

        return face_encoding

    def get_known_faces_encodings_list(self,known_images_path):
        fe = FaceEncodings()
        data = fe.load_known_face_encodings()
        self.known_face_encds = data["encodings"]
        self.known_face_names = data["names"]
        # print(self.known_face_encds)

    # def get_known_faces_encodings_list(self,known_images_path):
    #     self.known_face_encds = []
    #     self.known_face_names = []
    #     for root, dirs, files in os.walk(known_images_path):
    #         for name in files:
    #             if name.endswith((".jpeg",".png", ".JPG")):
    #                 # print (name)
    #                 # print(known_images_path+name)
    #                 face_enc = self.get_known_face_encodings(known_images_path+name)
    #                 self.known_face_encds.append(face_enc)
    #                 self.known_face_names.append(name)

    def g_emp_name(self, in_str):
        return in_str.split("_")[0]


    # def main_method(self):
    #     self.get_known_faces_encodings_list(self.config.get_common_param('KNOWN_IMG_STORE_PATH'))
    #     # print("********************************** KNOWN FACES ENC **************************************")
    #     # print(self.known_face_encds)
    #     # print("********************************** Names *******************")
    #     print(self.known_face_names)
    #     detected_face_encodings = self.get_face_encodings(self.image_name)
    #     # print(detected_face_encodings)
    #     # print("*****************************************************************************************")
    #     # matches = face_recognition.compare_faces(known_face_encodings=self.known_face_encds,face_encoding_to_check=detected_face_encodings[0])
    #     # print(matches)
    #     localtime = time.localtime(time.time())
    #     timestamp = time.strftime('%d-%b-%Y %H:%M:%S',localtime)
    #     emp_name = 'Unknown'
    #     status = False
    #     for face_encoding in detected_face_encodings:
    #         # print("****************************** DETECTED FACES ENC ***********************************")
    #         # print(face_encoding)
    #         # print(self.known_face_encds)
    #         print("***********************************")
    #         # print(face_encoding)
    #         matches = face_recognition.compare_faces(known_face_encodings=self.known_face_encds, face_encoding_to_check=face_encoding)
    #         dist = face_recognition.face_distance(face_encodings=self.known_face_encds,face_to_compare=face_encoding)
    #         print(dist)
    #         print(matches)
    #
    #         if True in matches:
    #             emp_name = self.g_emp_name(self.known_face_names[matches.index(True)])
    #             status= True
    #         else:
    #             print("NO Match")
    #             status  = False
    #     status_dict = {'Name': emp_name, 'Status': status, 'Time' : timestamp}
    #     print(status_dict)
    #     return status_dict

    def main_method(self):
            self.get_known_faces_encodings_list(self.config.get_common_param('KNOWN_IMG_STORE_PATH'))
            # print("********************************** KNOWN FACES ENC **************************************")
            # print(self.known_face_encds)
            # print("********************************** Names *******************")
            print(self.known_face_names)
            detected_face_encodings = self.get_face_encodings(self.image_name)
            # print(detected_face_encodings)
            # print("*****************************************************************************************")
            # matches = face_recognition.compare_faces(known_face_encodings=self.known_face_encds,face_encoding_to_check=detected_face_encodings[0])
            # print(matches)
            localtime = time.localtime(time.time())
            timestamp = time.strftime('%d-%b-%Y %H:%M:%S',localtime)
            emp_name = 'Unknown'
            status = False
            for face_encoding in detected_face_encodings:
                # print("****************************** DETECTED FACES ENC ***********************************")
                # print(face_encoding)
                # print(self.known_face_encds)
                print("***********************************")
                # print(face_encoding)
                matches = face_recognition.compare_faces(known_face_encodings=self.known_face_encds, face_encoding_to_check=face_encoding)
                face_distances = face_recognition.face_distance(face_encodings=self.known_face_encds,face_to_compare=face_encoding)
                matches = list(face_distances<=self.fr_tolerance_value) # Using a appropriate tolerance value .Lower is more strict. 0.6 is typical best performance.
                print(face_distances)
                print(matches)

                if True in matches:
                    match_index = np.argmin(face_distances)
                    emp_name = self.g_emp_name(self.known_face_names[match_index])
                    status= True
                else:
                    print("NO Match")
                    status  = False
            status_dict = {'Name': emp_name, 'Status': status, 'Time' : timestamp}
            print(status_dict)
            return status_dict

