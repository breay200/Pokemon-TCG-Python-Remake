from tkinter import *
import time
import os
root = Tk()

# EXTRACTION OF IMAGES FROM GIF INTO TEMP

# location = "images/001.gif"
# location1 = "images/649.gif"

# img = Image.open(location)
# print(img.n_frames)
# counter = 0
# for frame in ImageSequence.Iterator(img):
#     print(counter)
#     frame.save(f"images/temp/{counter}.png")
#     counter += 1


## ITERATING THROUGH IMAGES IN FOLDER AND UPDATING THE ELEMENT

frameCnt = 99
frames = [PhotoImage(file=f'images/temp/{i}.png') for i in range(frameCnt)]
delta = int(3000/99)
def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(delta, update, ind)
label = Label(root)
label.pack()
update(0)
root.mainloop()


# ## SETTING THE ICON OF TKINTER ROOT

# icon = PhotoImage(file="images/temp/1.png")
# root.iconphoto(True, icon)