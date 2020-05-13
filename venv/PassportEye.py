#import pytesseract
#from passporteye import read_mrz
#import cv2
#import numpy as np
#from matplotlib import pyplot as plt

#originalImage = cv2.imread('C:\\Users\\ashis\\Pictures\\Camera Roll\\RP_back.PNG')
#img = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#image_file = "C:\\Users\\ashis\\Pictures\\Camera Roll\\passport\\dutchpassport.png"
#mrz = read_mrz("C:\\Users\\ashis\\Pictures\\Camera Roll\\passport\\dutchpassport.png")


from PIL import Image
import pytesseract
from passporteye import read_mrz
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
im = Image.open("C:\\Users\\ashis\\Pictures\\Camera Roll\\passport\\dutch.png")

text = pytesseract.image_to_string(im, lang = 'eng')

#print(text)

print("-------This is machine readable code-------")
mrz = read_mrz("C:\\Users\\ashis\\Pictures\\Camera Roll\\passport\\dutch.png")
#mrz = read_mrz("C:\\Users\\ashis\\Pictures\\Camera Roll\\passport\\Indonesian.jpg")
#mrz = read_mrz("C:\\Users\\ashis\\Pictures\\Camera Roll\\passport\\us.jpg")
#mrz = read_mrz("C:\\Users\\ashis\\Pictures\\Camera Roll\\passport\\french.jpg")

mrz_data = mrz.to_dict()
print(mrz_data)

print("country: "+mrz_data['country'])
print("name: "+mrz_data['names'])
print("surname: "+mrz_data['surname'])
print("type: "+mrz_data['type'])
print("DOB: "+mrz_data['date_of_birth'])
print("SEX: "+mrz_data['sex'])
print("NUMBER: "+mrz_data['number'])
print("NATIONALITY: "+mrz_data['nationality'])
print("EXPIRATION DATE: "+mrz_data['expiration_date'])


