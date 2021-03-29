
try:
    # Importing Pillow for  image processing
    from PIL import Image
except ImportError:
    import Image
    # Importing Tesseract  for OCR engine
try:
     import pytesseract
except:
    print("No Module Zakaria")

def ocr_core(filename):
    #  Path of the tesseract engine
    pytesseract.pytesseract.tesseract_cmd = r'E:\\patternproject\\tesseract22\\tesseract.exe'
      #Pillow's Image class to open the image and pytesseract to detect the string in the image
      #Extracts when both English and Tamil language present in the image
    text = pytesseract.image_to_string(Image.open(filename), lang='eng+tam+ben+hin')
    return text

 #print(ocr_core(r"E:\pythonProject\Images\sample_image.PNG"))