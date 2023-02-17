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
1. Image_Processing_Tool_Main.py (this file, the Main file to execute first to launch/run the program) &
2. Image_Processing_Tool_Functions.py

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
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import cv2
import matplotlib.pyplot as plt
from matplotlib import rcParams
from Image_Processing_Tool_Functions import *

plt.style.use('seaborn')
fname = "./Dog.jfif"

#=============================================================
# Local Functions
#=============================================================
def openfn(current_file):
    filename = filedialog.askopenfilename(title='open')
    #print ("filename:from openfn():::::",filename)
    #print ("filename:from openfn():::::",current_file)
    if (filename == ""):
        #print("We got None")
        filename = current_file
    return filename

def open_img():
    global fname, bg_new
    fname = openfn(fname)
    # Open the Image File
    bg_new = ImageTk.PhotoImage(file=fname)
    print("Opening New file:",fname)
    # Create a Canvas
    #canvas = Canvas(mainWindow, width=700, height=3500)
    #canvas = Canvas(mainWindow, width=None, height=None)
    #canvas.pack(fill=BOTH, expand=True)

    # Add Image inside the Canvas
    #canvas.create_image(0, 0, image=bg, anchor='nw')
    canvas.itemconfig(image_container,image=bg_new)

def resize_image(e):
   global image, resized, image2
   # open image to resize it
   ##image = Image.open("./pic01.JPG")
   image = Image.open(fname)
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')
   
#=============================================================
# Calling Function in other file: ""
#=============================================================
def img_to_grayscale(): #using PIL,MatPlotLib
    image2gray(fname)

def img_to_invert_in_color(): #using PIL,MatPlotLib
    image2invertInColor(fname)

def img_to_invert_in_gray(): #using PIL,MatPlotLib
    image2invertInGray(fname)
    
def img_to_smoothing_in_color(): #using PIL,MatPlotLib
    image2smoothingInColor(fname)
    
def img_to_smoothing_in_gray(): #using PIL,MatPlotLib
    image2smoothingInGray(fname)
    
def img_to_emboss(): #using PIL,MatPlotLib
    image2Emboss(fname)

def img_to_sketch_in_color(): #using CV2,PIL,MatPlotLib
    image2sketchColorUsingCV2andBrightness(fname)

def img_to_sketch_in_gray(): #using CV2,PIL,MatPlotLib
    image2sketchGrayUsingCV2andBrightness(fname)
    
def img_transformation(): #using PIL,MatPlotLib
    imageTransformation(fname)

def about_this_application():
    aboutTheApplication()

def close_win():
    closeAllPlots()
    mainWindow.destroy()

#=============================================================
# Code in Public
#=============================================================
# Create an instance of Tkinter Frame
mainWindow = Tk()
mainWindow.title('Image Processing Tool: An Image Processing Application by Rithvika T (Reg.Num: 21BCE5554) BTech I Sem CSE @SCOPE,VIT Chennai')

# Set the geometry of Tkinter Frame
#mainWindow.geometry("700x450")
# Making main Window resizable
mainWindow.resizable(height = None, width = None)

# Open the Image File
fname = "./Dog.jfif"
bg = ImageTk.PhotoImage(file=fname)

# Create a Canvas
#canvas = Canvas(mainWindow, width=700, height=3500)
canvas = Canvas(mainWindow, width=None, height=None)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
image_container = canvas.create_image(0, 0, image=bg, anchor='nw')
#tk.Button(mainWindow, text="click", command=openImage).pack()

#==Creating Menubar Start==============
menubar = Menu(mainWindow)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
#file.add_command(label ='Open File', command = None)
file.add_command(label ='Open File', command=lambda:open_img())
file.add_separator()
#file.add_command(label ='Exit', command = mainWindow.destroy)
file.add_command(label ='Exit', command=lambda:close_win())

#==Adding Image Process Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Image Processing', menu = edit)

 
edit.add_command(label ='Convert Image to Grayscale', command = lambda:img_to_grayscale())
edit.add_command(label ='RGB Inverted Image (in Color)', command = lambda:img_to_invert_in_color())
edit.add_command(label ='RGB Inverted Image (in Gray)', command = lambda:img_to_invert_in_gray())
edit.add_command(label ='Smoothing/Blurring the Image (in Color)', command = lambda:img_to_smoothing_in_color())
edit.add_command(label ='Smoothing/Blurring the Image (in Gray)', command = lambda:img_to_smoothing_in_gray())
edit.add_command(label ='Convert Image to Emboss', command = lambda:img_to_emboss())
edit.add_command(label ='Convert Image to Sketch (in Gray)', command = lambda:img_to_sketch_in_gray())
edit.add_command(label ='Convert Image to Sketch (in Color)', command = lambda:img_to_sketch_in_color())
edit.add_command(label ='Image Transformation (Org to Sketch)', command = lambda:img_transformation())

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='About', menu = help_)
help_.add_command(label ='About This Application', command = lambda:about_this_application())

mainWindow.config(menu = menubar)
#==Creating Menubar End==============


# Bind the function to configure the parent window
# And, Calling function to resize the image
mainWindow.bind("<Configure>", resize_image)
mainWindow.mainloop()
#==========================================================================================
# End of the File
#==========================================================================================
