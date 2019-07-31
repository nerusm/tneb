__author__ = 'suren'
from face_rego import Face_Recog

filename = "/home/suren/Projects/TNEB/RPi/ServerModule/SatishRaj_1.jpeg"
print(filename)
face_reco = Face_Recog(filename)
face_reco.main_method()