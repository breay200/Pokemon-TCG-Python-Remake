import tkinter as tk
import time

master = tk.Tk()
width = int(master.winfo_screenwidth() * 0.75)
height = int(master.winfo_screenheight() * 0.75)
master.geometry(f"{width}x{height}")
master.title("TCG REMAKE")

canvas = tk.Canvas(master, width=width, height=height)
canvas.place(x=0,y=0)

rec = canvas.create_rectangle(0, 0, 100, 100, fill="red")
def test(event=None, x=0):
    x = 12
    canvas.move(rec, x, 0)
    x1, y1, x2, x2 = canvas.coords(rec)
    if x1 >= 400:
        print("done")
        master.unbind("<Return>")
    else:
        canvas.after(16, test)

x = 0
master.bind("<Return>", lambda event: test(event))
# canvas.after(1000, lambda: canvas.move(rec, 0, 400))
# #canvas.move(rec, 400, 400)
master.mainloop()


