"""
################################################################################
WHAT IS THIS?: AN IMAGE PROCESSING APPLICATION, NAMELY:
"IMAGE PROCESSING TOOL"
developed
by 
Student Name : (C)RITHVIKA TIRUVEEDHULA (Reg.Num: 21BCE5554)
A B.Tech. CSE Student in I Semester in the
SCOPE, The School of Computer Science and Engineering, @VIT Chennai    

This is done towards the fullfilment of   
Do It Yourself (DIY) Project  of the
'Introduction to Engineering' subject in the I Semester

27th December, 2021
################################################################################
################################################################################
APPLICATION NAME: "IMAGE PROCESSING TOOL"

WHAT IT DOES & WHAT IS IT'S FUNCTIONALITY?:
Convert the given Image to:
- Grayscale
- RGB Color Inverting (Inverting in Color)
- RGB Color Inverting (Inverting in Gray)
- Blurring/Smoothing the Image (Blurring in Color)
- Blurring/Smoothing the Image (Blurring in Gray)
- Converting into Embossing form of the image
- Converting Image into Sketch/Pencil Drawing (Drawing in Color)
- Sketch/Pencil Drawing (Drawingin Gray)
- Showing the Image Transformation (Shows How it Processes from the
                        given Orginal Image to Sketch/Drawing form of it)

The Input:
Any Image file (it takes all image formats: JPG,JPEG,PNG,GIF etc.,)

The Output:
Gives the Processosed Image after applying any of the feature listed above
(Please see the Functionality above)

This "IMAGE PROCESSING TOOL" Application consits of 2 files:
1. Image_Processing_Tool_Main.py &
2. Image_Processing_Tool_Functions.py (this file)

How To Run:
1. Make sure the above two files will be available in the same folder
2. Make sure the image files what you want to apply the above image processing techniques will be in the same folder
3. Open the file "Image_Processing_Tool_Main.py" with in the IDLE shell & Run

################################################################################
"""

#=============================================================
# Import the required Libraries
#=============================================================
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk, Image
from PIL import Image, ImageFilter,ImageEnhance
#import PIL.ImageOps
from PIL import *
import PIL as PIL
from tkinter import ttk
import cv2
from sketchify import sketch

#1. Importing Modules
import matplotlib.pyplot as plt
plt.style.use('seaborn')

global img_org, img_gray,img_invert,img_smoothing_gray,img_in_sketch
#=============================================================
# Implementation of Functions of my Library
#=============================================================

def closeAllPlots():
    plt.close("all")

def aboutTheApplication():
    messagebox.showinfo(title= 'About Image Processing Tool', message= '\n  27th Dec, 2021\n (C) Rithvika Tiruveedhula (Reg.Num: 21BCE5554) \n  BTech I Semester CSE Student in SCOPE, @VIT Chennai\n \n This is done towards the fullfilment of \n Do It Yourself (DIY) Project \n of the \'Introduction to Engineering\' subject', icon= 'info')  
def image2gray(givenfile):
    print("image2gray():",givenfile) 
    img_org = Image.open(givenfile)
    img_org = img_org.convert(mode="RGB")
    imgGray = img_org.convert('L')
    #imgGray.save('test_gray.jpg')    

    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.canvas.manager.set_window_title('Rithvika Project : Image in Gray')

    plt.imshow(imgGray,cmap="gray")

    plt.axis("off")
    plt.title("Gray Scale Image")
    plt.show(block=False)
    #plt.close("all")
    
def image2invertInColor(givenfile):
    print("image2invertInColor():",givenfile)
    img_org = Image.open(givenfile)
    img_org = img_org.convert(mode="RGB")
    invertedInColor = PIL.ImageOps.invert(img_org)

    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.canvas.manager.set_window_title('Rithvika Project : RGB Inverted Image in Color')

    plt.imshow(invertedInColor,cmap="gray")

    plt.axis("off")
    plt.title("RGB Inverted Color Image")
    plt.show(block=False)
    #plt.close("all")

    
def image2invertInGray(givenfile):
    print("image2invertInGray():",givenfile)

    img_org = Image.open(givenfile)
    img_org = img_org.convert(mode="RGB")
    imgGray = img_org.convert('L')

    invertedInGray = PIL.ImageOps.invert(imgGray)

    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.canvas.manager.set_window_title('Rithvika Project : RGB Inverted Image in Gray')

    plt.imshow(invertedInGray,cmap="gray")

    plt.axis("off")
    plt.title("RGB Inverted Gray Image")
    plt.show()

def image2smoothingInColor(givenfile):

    print("image2smoothingInColor():",givenfile)
    img_org = Image.open(givenfile)
    img_org = img_org.convert(mode="RGB") #mode org place1
    
    GaussianBlurImage = img_org.filter(ImageFilter.GaussianBlur(5))

    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.canvas.manager.set_window_title('Rithvika Project : Blured/Smoothing Image in Color')

    plt.imshow(GaussianBlurImage,cmap="gray")

    plt.axis("off")
    plt.title("Blured/Smoothing Color Image")
    plt.show()

def image2smoothingInGray(givenfile):

    print("image2smoothingInGray():",givenfile)
    img_org = Image.open(givenfile)
    img_org = img_org.convert(mode="RGB") #mode org place2
    imgGray = img_org.convert('L')
    
    GaussianBlurImage = imgGray.filter(ImageFilter.GaussianBlur(5))

    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.canvas.manager.set_window_title('Rithvika Project : Blured/Smoothing Image in Gray')

    plt.imshow(GaussianBlurImage,cmap="gray")

    plt.axis("off")
    plt.title("Blured/Smoothing Gray Image")
    plt.show()

def image2Emboss(givenfile):

    print("image2Emboss():",givenfile)
    img_org = Image.open(givenfile)
    img_org = img_org.convert(mode="RGB") #mode org place3
    imgGray = img_org.convert('L')

    invertedInGray = PIL.ImageOps.invert(imgGray)

    #imageInEmboss = imgGray.filter(ImageFilter.CONTOUR)
    imageInEmboss = invertedInGray.filter(ImageFilter.EMBOSS)

    #----------------------
    #image brightness enhancer
    enhancer = ImageEnhance.Contrast(imageInEmboss)

    factor = 5.5 #increase contrast
    image_output = enhancer.enhance(factor)
    #----------------------

    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.canvas.manager.set_window_title('Rithvika Project : Image in Emboss')

    #plt.imshow(imageInEmboss,cmap="gray")
    plt.imshow(image_output,cmap="gray")

    plt.axis("off")
    plt.title("Image in Emboss")
    plt.show()

def image2sketchColorUsingCV2andBrightness(givenfile):

    #PIL Sketch steps

    #open CV Sketch steps
    print("image2sketchColorUsingCV2andBrightness():",givenfile)
    img_org_inColor = cv2.imread(givenfile)
    img_org_inColor = cv2.cvtColor(img_org_inColor,cv2.COLOR_BGR2RGB)
    #img_gray = cv2.cvtColor(img_org_inColor,cv2.COLOR_RGB2GRAY)
    img_invert_inColor = cv2.bitwise_not(img_org_inColor)
    
    img_smoothing_gray_inColor = cv2.GaussianBlur(img_invert_inColor, (21, 21),sigmaX=0, sigmaY=0)
    img_in_sketch = cv2.divide(img_org_inColor, 255 - img_smoothing_gray_inColor, scale=255)

    #----------------------
    #CV2+BGR  to PIL+RGB
    # You may need to convert the color
    img = cv2.cvtColor(img_in_sketch, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    im_pil = Image.fromarray(img)

    #----------------------
    #image brightness enhancer
    enhancer = ImageEnhance.Contrast(im_pil)

    factor = 4.5 #increase contrast
    image_output = enhancer.enhance(factor)
    #----------------------
    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.canvas.manager.set_window_title('Rithvika Project : Drawing/Sketching of the given Image(in Color)')

    plt.imshow(image_output,cmap="gray")

    plt.axis("off")
    plt.title("Image in Sketch(in Color)")
    plt.show()

def image2sketchGrayUsingCV2andBrightness(givenfile):
    #PIL Sketch steps

    #open CV Sketch steps
    print("image2sketchGrayUsingCV2andBrightness():",givenfile)
    img_org = cv2.imread(givenfile)
    img_org = cv2.cvtColor(img_org,cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_org,cv2.COLOR_RGB2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    
    img_smoothing_gray = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    img_in_sketch = cv2.divide(img_gray, 255 - img_smoothing_gray, scale=255)

    #----------------------
    #CV2+BGR  to PIL+RGB
    # You may need to convert the color
    img = cv2.cvtColor(img_in_sketch, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    im_pil = Image.fromarray(img)

    #----------------------
    #image brightness enhancer
    enhancer = ImageEnhance.Contrast(im_pil)

    factor = 4.5 #increase contrast
    image_output = enhancer.enhance(factor)
    #----------------------
    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.canvas.manager.set_window_title('Rithvika Project : Drawing/Sketching of the given Image(in Gray)')

    plt.imshow(image_output,cmap="gray")

    plt.axis("off")
    plt.title("Image in Sketch(in Gray)")
    plt.show()

#Image Transformation (from Org to Sketch)
def imageTransformation(givenfile):
    #====================================================
    #Setting Plot & Figure Sizes to Dsiplay
    #====================================================
    fig = plt.figure(figsize=(50,50))
    fig.canvas.manager.set_window_title('Rithvika Project : Image Transformation (from Org to Sketch)')
    plt.tight_layout()
    fig.set_figwidth(10)
    fig.set_figheight(3)

    #================================================
    #Original Image
    #================================================
    plt.subplot(1,5,1)
    #img_org = cv2.imread(givenfile)
    img_org = Image.open(givenfile)
    plt.imshow(img_org)
    plt.axis("off")
    plt.title("Original Image")

    #================================================
    #GrayScale
    #================================================
    plt.subplot(1,5,2)

    #img_gray = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)
    img_org = img_org.convert(mode="RGB")
    img_gray = img_org.convert('L')
    
    plt.imshow(img_gray,cmap="gray")
    plt.axis("off")
    plt.title("GrayScale Image")

    #================================================
    #Inverted
    #================================================
    plt.subplot(1,5,3)

    #img_invert = cv2.bitwise_not(img_gray)
    img_invert = PIL.ImageOps.invert(img_gray)
    
    plt.imshow(img_invert,cmap="gray")
    plt.axis("off")
    plt.title("Inverted Image")
    
    #================================================
    #Smoothen/Blured
    #================================================
    plt.subplot(1,5,4)
    
    #img_smoothing_gray = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    #img_smoothing_gray = img_gray.filter(ImageFilter.GaussianBlur(5))
    img_smoothing_gray = img_invert.filter(ImageFilter.GaussianBlur(5))
    
    plt.imshow(img_smoothing_gray,cmap="gray")
    plt.axis("off")
    plt.title("Smoothen Image")
    
    #================================================
    #Sketch
    #================================================
    plt.subplot(1,5,5)

    img_org = cv2.imread(givenfile)
    img_org = cv2.cvtColor(img_org,cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_org,cv2.COLOR_RGB2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing_gray = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    img_in_sketch = cv2.divide(img_gray, 255 - img_smoothing_gray, scale=255)

    #----------------------
    #CV2+BGR  to PIL+RGB
    # You may need to convert the color
    img = cv2.cvtColor(img_in_sketch, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    im_pil = Image.fromarray(img)
    #----------------------
    #----------------------
    #image brightness enhancer
    enhancer = ImageEnhance.Contrast(im_pil)

    factor = 4.5 #increase contrast
    image_output = enhancer.enhance(factor)
    #----------------------

    plt.imshow(image_output,cmap="gray")
    plt.axis("off")
    plt.title("Sketch Image")

    plt.suptitle("Image Transformation (from Orginal to Sketch)")   
    plt.show()
#==========================================================================================
# End of the File
#==========================================================================================


