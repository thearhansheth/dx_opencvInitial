# you have to install tesseract in your laptop
# how to run ? --> python script_images.py <folder_paht>
# this is script is for ocr. a folder containing images will be converted to text and it will be stored in output.txt within that folder

#from pdf2image import convert_from_path
import pytesseract
import sys
import os
import cv2 as cv
from PIL import Image

# Path to the folder containing images
folder_path = "/Users/arhan.sheth/Documents/Codes/DX/Basics/dx_opencvInitial/arhan_ocr_task/images/sample_input_images" #sys.argv[1]

# Prepare the path for the output text file within the same folder
output_file_path = os.path.join(folder_path, 'output.txt')

# List all image files in the directory assuming they are in JPG format. Modify the extension if different.
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpeg')]

# Open the output file to write the extracted text
with open(output_file_path, 'w') as file:
    # Iterate through each image file
    for image_path in image_files:
        print(image_path)
        # Open the image file
        img = Image.open(image_path)

        # Extract text from image using pytesseract
        text = pytesseract.image_to_string(img,config="-l san") # changes it for using other languages

        # Write the extracted text to the output file
        file.write(text)

# Print 'done' to indicate completion
print('done')
