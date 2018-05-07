import requests
import json
from pprint import pprint
from datetime import datetime
from flask import Flask, request, render_template
import selenium
import cv2

image_key1='KEYS'

translator_key1='KEYS'

headers={'Ocp-Apim-Subscription-Key' : image_key1,'Content-type':'application/octet-stream'}

translator_api="https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"

translator_header={'Ocp-Apim-Subscription-Key' : translator_key1, 'Content-type':'application/json'}

image_api = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/ocr"

image_url ="http://desert-utility.com/documents/AsbestosSignSpanish.jpg"

google_translate_url="https://translate.google.com/?hl=en&tab=wT&authuser=0"

images = cv2.imread("static/images/corny.jpg")
gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
#gray = cv2.threshold(gray, 0, 159, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.medianBlur(gray,3)
cv2.imwrite('static/tmp/grayscale.jpg', gray)
with open('static/tmp/grayscale.jpg', 'rb') as f:
    img_data = f.read()


params={'handwriting':'false'}
#params   = {'visualFeatures': 'Categories,Description,Color'}

response = requests.post(image_api, headers=headers, params=params, data=img_data)
result = response.json()
#pprint(result)
endtext = ''
lines = result['regions'][0]['lines']
language_code = result['language']

for i in lines:
    for x in i['words']:
        endtext += (x['text'] + ' ')
    endtext += ','
print (endtext)

"""t_params="&to=en"
translator_response = requests.post(translator_api, headers=translator_header, params=t_params, json=[{"Text":endtext}])
t_result = translator_response.json()
pprint(t_result)
translation = t_result[0]['translations'][0]['text']
print(translation)


app = Flask(__name__)

@app.route("/", methods=['GET'])
def homepage():
    return (translation)


if __name__ == '__main__':
    app.run(debug=True)"""
