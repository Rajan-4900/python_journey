import tkinter as tk
import time
from PIL import Image, ImageTk

# Main Application Window
root = tk.Tk()
root.title("Photo Sliding Window")
root.geometry("900x900")

# List of Image path
image_path = [
    r"D:\Coding\Python\Project_1\Album Project\img1.jpg",        # Image path URL
    r"img2.jpg",
    r"img3.jpg",
    r"img4.jpg",
    r"img5.jpg",
    r"img6.jpg",
    r"img7.jpg",
    r"img8.jpg",
    r"img9.jpg",
    r"img10.jpg",
    r"img11.jpg",
    r"img12.jpg",
]

# Converting in the Image and storing the images in the "images variable list"
image_size = (900, 700)
images = []             # List
for path in image_path :
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img)              # Adding each image in the images list

# Converting PIL images into Tkinter Compatible Image
final_images = []       # Created the empty List
for img in images:
    photo = ImageTk.PhotoImage(img)             
    final_images.append(photo)

# Label widget to keep photo
image_label = tk.Label(root)
image_label.pack(pady=30)

# Slide Show Function
def start_slideShow():
    for photo in final_images:
        image_label.config(image= photo)
        image_label.image=photo
        root.update()
        time.sleep(2)

# Button
play_button = tk.Button(
    root,
    text = "Play the Slideshow",
    font = ("Arial", 17),
    command=start_slideShow
)

play_button.pack(pady=40)

root.mainloop()     # It is used keep the window open
