__author__ = 'suren'
from config import Config
import face_recognition
import pickle
import os

class FaceEncodings:

    def __init__(self):
        self.config = Config()
        self.known_images_path = self.config.get_common_param('KNOWN_IMG_STORE_PATH')


    def get_known_face_encodings(self,image_name):
        image = face_recognition.load_image_file(image_name)
        face_encoding = face_recognition.face_encodings(image)[0]
        return face_encoding

    def get_known_faces_encodings_list(self,known_images_path):
        self.known_face_encds = []
        self.known_face_names = []
        for root, dirs, files in os.walk(known_images_path):
            for name in files:
                if name.endswith((".jpeg",".png", ".JPG")):
                    # print (name)
                    # print(known_images_path+name)
                    face_enc = self.get_known_face_encodings(known_images_path+name)
                    self.known_face_encds.append(face_enc)
                    self.known_face_names.append(name)
    def get_known_faces_encodings_file(self,known_image_name):
        self.known_face_encds = []
        self.known_face_names = []
        # print (name)
        # print(known_images_path+name)
        face_enc = self.get_known_face_encodings(self.known_images_path+known_image_name)
        self.known_face_encds.append(face_enc)
        self.known_face_names.append(known_image_name)
        # print(self.known_face_encds)
        # print(self.known_face_names)

    def store_known_face_encodings_bulk(self):
        self.get_known_faces_encodings_list(self.known_images_path)
        data = {"encodings": self.known_face_encds, "names": self.known_face_names}
        f = open("encodings.pickle", "wb")

        f.write(pickle.dumps(data))
        f.close()
        print(data)

    def store_known_face_encodings_file(self, image_file):
        self.get_known_faces_encodings_file(image_file)
        stored_data = self.load_known_face_encodings()
        stored_encodings = stored_data["encodings"]
        stored_names = stored_data["names"]
        # print("***")
        # print(stored_encodings)
        # print(stored_names)
        stored_encodings.append(self.known_face_encds)
        stored_names.append(self.known_face_names)
        print("*****************************************************************************************")
        # print(stored_encodings)
        # print(stored_names)
        data = {"encodings": stored_encodings, "names": stored_names}
        f = open("encodings.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()
        # print(data)

    def load_known_face_encodings(self):
        data = pickle.loads(open("encodings.pickle", "rb").read())
        return data

