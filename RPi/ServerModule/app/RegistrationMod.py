__author__ = 'suren'

from FaceEncodings import FaceEncodings


class Registration:

    def __init__(self):
        self.fe = FaceEncodings()

    def register_users_bulk(self):
        self.fe.store_known_face_encodings_bulk()
    def register_user(self, image_file):
        self.fe.store_known_face_encodings_file(image_file=image_file)

    def load_print(self):
        data = self.fe.load_known_face_encodings()
        enc = data["encodings"]
        names = data["names"]
        print("Names: %s"%names)
        print("Encodings:%s"%enc)


reg = Registration()
reg.register_users_bulk()
# reg.register_user("SatishRaj_1.jpeg")
reg.load_print()
