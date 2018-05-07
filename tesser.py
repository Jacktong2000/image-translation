import cv2
import pytesseract
from PIL import Image
from textblob import TextBlob
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
import readimage


#Old testing codes
"""img = cv2.imread('static/images/spanish.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img=cv2.medianBlur(img,3)
#img = cv2.threshold(img, 0, 100,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#cv2.imshow("show",img)

cv2.imwrite('static/images/delete.jpg',img)

text = pytesseract.image_to_string(img, lang='spa')

print(text)
text=TextBlob(text)

aftertext = text.translate(to='en')"""


app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/tmp'
configure_uploads(app, photos)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        img = cv2.imread('static/tmp/{0}'.format(filename))
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img = 'static/tmp/{0}'.format(filename)
        origin = request.form['origin']
        message = pytesseract.image_to_string(img, lang=origin)
        lang = request.form['language']

        text = TextBlob(message)
        after_translation = text.translate(to=lang)
        return render_template("tesser.html", message=message, translation=after_translation, image='static/tmp/{0}'.format(filename))

    else:
        message = 'Translations can be a bit off at times, use common sense when interpreting the message.'
        return render_template("tesser.html", message=message, image = 'static/images/Tokyo.jpg')



if __name__ == '__main__':
    app.run(debug=True)
