import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def openImage():
    filePath = filedialog.askopenfilename()
    if not filePath:
        return

    # Open the selected image.
    image = Image.open(filePath)
    # Resize for display.
    displayWidth, displayHeight = 400, 300
    aspect = image.width / image.height
    if image.width / image.height > displayWidth / displayHeight:
        displayHeight = int(displayWidth / aspect)
    else:
        displayWidth = int(displayHeight * aspect)

    # Convert the image to Tkinter compatibility.
    photo = ImageTk.PhotoImage(image.resize((displayWidth, displayHeight)))

    # Configure the label to display the image
    imageLabel.configure(image=photo)
    imageLabel.image = photo  # Keep a reference.

# Setup the UI.
root = tk.Tk()
root.title("Open and Display Image")

# Create a label widget for displaying the image
imageLabel = tk.Label(root)
imageLabel.pack()

# Create a button widget for opening images
openButton = tk.Button(root, text="Open Image", command=openImage)
openButton.pack()

root.mainloop()