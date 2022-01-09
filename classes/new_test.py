from PIL import Image
import tkinter as tk
from PIL import ImageSequence

master = tk.Tk()

location = "images/001.gif"
location1 = "images/649.gif"

img = Image.open(location)
print(img.n_frames)
counter = 0
for frame in ImageSequence.Iterator(img):
    print(counter)
    frame.save(f"images/temp/{counter}.png")
    counter += 1

# print(img.n_frames)
# print(img.format, img.size, img.mode)

# tk_img = tk.PhotoImage(file = location)
# width, height = tk_img.width(), tk_img.height()
# print(tk_img)

# canvas = tk.Canvas(master, width=500, height=500)
# canvas.pack()

# delta = int(3000/99)
# i = 1
# delay =0

# images = canvas.create_image(file="images/temp/1.png")

# for i in range(1, 100):
#     print(i)
#     img = tk.PhotoImage(file=f"images/temp/{i}.png")
#     update = lambda img: canvas.itemconfig(images,image=img)
#     canvas.after(delay, update, img)
#     delay += delta
# image = canvas.create_image(width,height, image = tk_img)

# # l = tk.Label(master, image=tk_img)
# # l.pack()
master.mainloop()