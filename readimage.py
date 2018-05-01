import json
import requests
from pprint import pprint
from datetime import datetime


def get_text(image):
    image_key1='key'

    headers={'Ocp-Apim-Subscription-Key' : image_key1, 'Content-Type': 'application/octet-stream'}

    image_api = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/ocr"

    params={'handwriting':'false'}

    with open('static/tmp/{0}'.format(image), 'rb') as f:
        img_data=f.read()

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


def translate(text):
    translator_key1='key'

    translator_api="https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"

    translator_header={'Ocp-Apim-Subscription-Key' : translator_key1, 'Content-type':'application/json'}

    t_params="&to=en"

    translator_response = requests.post(translator_api, headers=translator_header, params=t_params, json=[{"Text":text}])
    t_result = translator_response.json()

    #pprint(t_result)
    translation = t_result[0]['translations'][0]['text']
    #print(translation)
    return translation
