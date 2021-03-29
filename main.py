from flask import Flask, render_template,request

# importing 'ocr_core' function from the 'OCR' python File

from ocr import  ocr_core
# importing 'language_detector' function from the 'api_detect' python File
from api_detect import  language_detector
# importing 'translate' function from the 'api_translate' python File
# from api_translate import  translate
from gltrans import trans_papa
# define a folder to store and later serve the Images

##zakaria
# UPLOAD_FOLDER = "E:\\Coding\\Python\\OCR\\ocr_image_process"

UPLOAD_FOLDER = "E:\pythonProject\Images\sample_image.PNG"
# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

app =  Flask(__name__)
# app.debug = True


# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the upload page
@app.route('/', methods=['GET', 'POST'])
def upload_page():
    index = 0
    if request.method == 'POST':
        # check if there is a file in the request
        if ('file' in request.files) or ('file1' in request.files):
            # This condition will execute when user tries to extracts the text along with translation
            if request.files['file'].filename == "":
                index = 1
                file = request.files['file1']
            else:
                file = request.files['file']
            # Check language choose by the user to translate
            if request.form['languages']:
                translate_language = request.form['languages']

            if file and allowed_file(file.filename):

                # call the OCR function on it
                extracted_text = ocr_core(file)
                # Condition to both text extraction and translation
                if index == 1:
                    detected_language = language_detector(extracted_text)
                    translated_text = trans_papa(extracted_text, detected_language, translate_language)
                    return render_template('upload.html',
                                           extracted_text=extracted_text,
                                           detected_language= detected_language,
                                           translated_text=translated_text)
                # Extracts the text from the image
                else:
                    return render_template('upload.html',
                                           extracted_text=extracted_text)
        # Condition for only translation from the text
        if 'translate' in request.form:
            # Check language choose by the user to translate
            if request.form['languages']:
                translate_language = request.form['languages']
            text = request.form['translate']
            # Calling 'language_detector' function to detect the language
            detected_language = language_detector(text)
            # Condition when the API fails to detect the language
            if detected_language == "":
                detected_language = "English"
            # Calling 'translate' function to translate the text
            translated_text = trans_papa(text, detected_language, translate_language)
            return render_template('upload.html', translated_text=translated_text,detected_language=detected_language)
    # 'GET' request
    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)

