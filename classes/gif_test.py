from tkinter import *
import time
import os
from PIL import Image, ImageSequence

class Sprites():
    def __init__(self) -> None:
        pass

    def extract_images(profile_img):
        location = profile_img
        img = Image.open(location)
        print(img.n_frames)
        counter = 0
        for frame in ImageSequence.Iterator(img):
            print(counter)
            frame.save(f"temp/avatar{counter}.png")
            counter += 1


    # def play_gif(self):
    #     def update(ind):
    #         frame = frames[ind]
    #         ind += 1
    #         if ind == frameCnt:
    #             ind = 0
    #         label.configure(image=frame)
    #         root.after(delta, update, ind)

    #     frameCnt = len(os.listdir(dir))
    #     frames = [PhotoImage(file=f'images/temp/{i}.png') for i in range(frameCnt)]
    #     delta = int(3000/frameCnt)
    #     label = Label(root)
    #     label.pack()
    #     update(0)
    #     root.mainloop()

## ITERATING THROUGH IMAGES IN FOLDER AND UPDATING THE ELEMENT

# ## SETTING THE ICON OF TKINTER ROOT

# icon = PhotoImage(file="images/temp/1.png")
# root.iconphoto(True, icon)