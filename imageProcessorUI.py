import tkinter as tk
from tkinter import filedialog, Scale
from PIL import Image, ImageTk

def applyAdjustments():
    pass

def openImage():
    pass

root = tk.Tk()
root.title("Astrophotography RGB and Brightness Enhancer")

frame = tk.Frame(root)
frame.pack()

originalLabel = tk.Label(frame, text="Original Image")
originalLabel.pack(side=tk.LEFT)

adjustedLabel = tk.Label(frame, text="Enhanced Image")
adjustedLabel.pack(side=tk.RIGHT)

redSlider = Scale(root, from_=-50, to=50, orient=tk.HORIZONTAL, label='Red Intensity')
redSlider.pack()

greenSlider = Scale(root, from_=-50, to=50, orient=tk.HORIZONTAL, label='Green Intensity')
greenSlider.pack()

blueSlider = Scale(root, from_=-50, to=50, orient=tk.HORIZONTAL, label='Blue Intensity')
blueSlider.pack()

brightnessSlider = Scale(root, from_=-50, to=50, orient=tk.HORIZONTAL, label='Brightness')
brightnessSlider.pack()

openButton = tk.Button(root, text="Open Image", command=openImage)
openButton.pack()

applyButton = tk.Button(root, text="Apply Changes", command=applyAdjustments)
applyButton.pack()

root.mainloop()