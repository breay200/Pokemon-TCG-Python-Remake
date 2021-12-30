import tkinter as tk
import re

def get_coords_on_enter(a, b, c, d):
    coords = (a-c, b-d)
    print(coords)

def get_btn_dimensions(geo, a, b, c, d, wid, height):
    print(geo)
    coords = (a-c, b-d)
    print(coords)
    print(wid, height)

def split_geo(geo):
    print(geo)
    width, height, x, y = re.split(r'[x+]', geo)
    print(width, height, x, y)


master = tk.Tk()
width = int(master.winfo_screenwidth() * 0.75)
height = int(master.winfo_screenheight() * 0.75)
master.geometry(f"{width}x{height}")
master.title("TCG REMAKE")
button1=tk.Button(master, text="hello")
button2=tk.Button(master, text="hello2")
buttons = [button1, button2]
for btn in buttons:
    #print(buttons.index(btn))
    # if buttons.index(btn) == 0:
        #btn.bind("<Enter>", lambda event: get_coords_on_enter(master.winfo_pointerx(), master.winfo_pointery(), master.winfo_rootx(), master.winfo_rooty()))
        #btn.bind("<Enter>", lambda event: get_btn_dimensions(button2.winfo_geometry(), button2.winfo_rootx(), button2.winfo_rooty(), master.winfo_rootx(), master.winfo_rooty(), button2.winfo_width(), button2.winfo_height()))
    btn.bind("<Enter>", lambda event: split_geo(button2.winfo_geometry()))
    btn.grid()
# master.update()
master.mainloop()