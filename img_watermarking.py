from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog

# Initialize the selected_image variable
selected_image = None

# Create a font for the watermark
font = ImageFont.load_default()

def load_image():
    global selected_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if file_path:
        selected_image = Image.open(file_path)

def add_watermark():
    global selected_image
    if selected_image:
        width, height = selected_image.size
        draw = ImageDraw.Draw(selected_image)
        text = "sample watermark"

        # Calculate the x, y coordinates of the text
        margin = 10
        x = width - 30 - margin
        y = height - 40 - margin

        # Draw watermark in the bottom right corner
        draw.text((x, y), text, font=font)
        selected_image.show()

# Create a Tkinter window
window = Tk()
window.title("Watermarking App")

# Create a button to load an image
load_image_button = Button(window, text="Load Image", command=load_image)
load_image_button.pack()

# Create a button to add watermark
add_watermark_button = Button(window, text="Add Watermark", command=add_watermark)
add_watermark_button.pack()

# Start the Tkinter event loop
window.mainloop()
