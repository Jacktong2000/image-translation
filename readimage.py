import json
import requests
from pprint import pprint
from datetime import datetime
import cv2
import argparse
import os



def get_text(image):
    image_key1='KEYS'

    headers={'Ocp-Apim-Subscription-Key' : image_key1, 'Content-Type': 'application/octet-stream'}

    image_api = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/ocr"

    params={'handwriting':'false'}

    img = cv2.imread('static/tmp/{0}'.format(image))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('static/tmp/gray{0}'.format(image),img)

    with open('static/tmp/gray{0}'.format(image), 'rb') as f:
    #with open(img, 'rb') as f:
        img_data=f.read()

    os.system('rm static/tmp/gray{0}'.format(image))

    response = requests.post(image_api, headers=headers, params=params, data=img_data)
    result = response.json()

    endtext = ''
    try:
        lines = result['regions'][0]['lines']
    except:
        return ('Not a valid image.')

    for i in lines:
        for x in i['words']:
            endtext += (x['text'] + ' ')
        endtext += ','
    return endtext


def translate(text, language):
    translator_key1='KEYS'

    translator_api="https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"

    translator_header={'Ocp-Apim-Subscription-Key' : translator_key1, 'Content-type':'application/json'}


    t_params="&to={0}".format(language)

    translator_response = requests.post(translator_api, headers=translator_header, params=t_params, json=[{"Text":text}])
    t_result = translator_response.json()

    #pprint(t_result)
    try:
        translation = t_result[0]['translations'][0]['text']
    except:
        translation = 'You need to select a language.'
    #print(translation)
    return translation
