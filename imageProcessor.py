#Import necessary libraries.
import tkinter as tk  #Import tkinter for UI creation.
from tkinter import filedialog, Scale  #Import for file selection and scale for sliders.
from PIL import Image, ImageTk, ImageEnhance  #Import PIL for image altering/processing.

#Define a function to change image based on RGB and brightness slider values.
def enhanceImage(image, rScale, gScale, bScale, brightness):
    #Iterate through each pixel in the image.
    width, height = image.size  #Get the dimensions of image.
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))  #Get the current pixel's RGB values.
            #Adjust the RGB values based on the UI slider positions.
            r = int(r * ((rScale / 100) + 1))
            g = int(g * ((gScale / 100) + 1))
            b = int(b * ((bScale / 100) + 1))
            #Ensure the new RGB values are within the valid range (0-255).
            r = min(255, max(0, r))
            g = min(255, max(0, g))
            b = min(255, max(0, b))
            image.putpixel((x, y), (r, g, b))  #Update the pixel with new RGB values.
    
    #Adjust the overall brightness of the image.
    enhancer = ImageEnhance.Brightness(image)  #Create a brightness changer.
    image = enhancer.enhance((brightness / 50) + 1)  #Adjust the brightness based on the slider.
    return image  #Return the changed image.

#Define a function to apply the adjustments to the image.
def applyAdjustments():
    #Get the current positions of the sliders.
    rScale = redSlider.get()
    gScale = greenSlider.get()
    bScale = blueSlider.get()
    brightness = brightnessSlider.get()
    
    #Apply changes to a copy of the original image.
    enhancedImage = enhanceImage(originalImage.copy(), rScale, gScale, bScale, brightness)
    #Convert the enhanced image to a format that can be displayed in Tkinter, hence importing ImageTk.
    enhancedPhoto = ImageTk.PhotoImage(enhancedImage.resize((displayWidth, displayHeight)))
    #Update the label to show the enhanced image.
    adjustedLabel.configure(image=enhancedPhoto)
    adjustedLabel.image = enhancedPhoto  #Keep a reference.

#Define a function to open an image file.
def openImage():
    global originalImage, displayWidth, displayHeight  #Declare global variables.
    
    filePath = filedialog.askopenfilename()  #To select an image file.
    if not filePath:  #If no file is selected, return nothing.
        return
    
    #Load the selected image, if file is selected.
    originalImage = Image.open(filePath)
    #Calculate display dimensions to maintain aspect ratio.
    displayWidth, displayHeight = 400, 300
    aspect = originalImage.width / originalImage.height
    if originalImage.width / originalImage.height > displayWidth / displayHeight:
        displayHeight = int(displayWidth / aspect)
    else:
        displayWidth = int(displayHeight * aspect)
    
    #Convert the original image for display in the UI with tkinter and show it in both labels initially.
    originalPhoto = ImageTk.PhotoImage(originalImage.resize((displayWidth, displayHeight)))
    originalLabel.configure(image=originalPhoto)
    originalLabel.image = originalPhoto
    adjustedLabel.configure(image=originalPhoto)
    adjustedLabel.image = originalPhoto
    
    #Reset the sliders to their initial positions and values.
    redSlider.set(0)
    greenSlider.set(0)
    blueSlider.set(0)
    brightnessSlider.set(0)

#Setup the UI.
root = tk.Tk()  #Create the main UI window.
root.title("RGB and Brightness Enhancer")  #Set the window title.

frame = tk.Frame(root)  #Create a frame to hold the labels.
frame.pack()  #Add the frame to the window.

#Create labels to display the original and enhanced images.
originalLabel = tk.Label(frame, text="Original Image")
originalLabel.pack(side=tk.LEFT)
adjustedLabel = tk.Label(frame, text="Enhanced Image")
adjustedLabel.pack(side=tk.RIGHT)

#Create sliders for adjusting color intensity and brightness.
redSlider = Scale(root, from_=-50, to=50, orient=tk.HORIZONTAL, label='Red Intensity')
greenSlider = Scale(root, from_=-50, to=50, orient=tk.HORIZONTAL, label='Green Intensity')
blueSlider = Scale(root, from_=-50, to=50, orient=tk.HORIZONTAL, label='Blue Intensity')
brightnessSlider = Scale(root, from_=-50, to=50, orient=tk.HORIZONTAL, label='Brightness')
# Add the sliders to the window
redSlider.pack()
greenSlider.pack()
blueSlider.pack()
brightnessSlider.pack()

#Create buttons for opening an image and applying changes.
openButton = tk.Button(root, text="Open Image", command=openImage)
applyButton = tk.Button(root, text="Apply Changes", command=applyAdjustments)
#Add the buttons to the window.
openButton.pack()
applyButton.pack()

root.mainloop()  #Start the UI loop.
