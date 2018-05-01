from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
import readimage

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/tmp'
configure_uploads(app, photos)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        message = readimage.get_text(filename)
        after_translation = readimage.translate(message)
        return render_template("index.html", message=message, translation=after_translation, image='static/tmp/{0}'.format(filename))

    else:
        message = 'Translations can be a bit off at times, use common sense when interpreting the message.'
        return render_template("index.html", message=message, image = 'static/images/Tokyo.jpg')


if __name__ == '__main__':
    app.run(debug=True)
