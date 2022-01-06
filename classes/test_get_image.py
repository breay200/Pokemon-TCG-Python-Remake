import tkinter as tk
import time

master = tk.Tk()
width = int(master.winfo_screenwidth() * 0.75)
height = int(master.winfo_screenheight() * 0.75)
master.geometry(f"{width}x{height}")
master.title("TCG REMAKE")

canvas = tk.Canvas(master, width=width, height=height)
canvas.place(x=0,y=0)

# button = tk.Button(canvas, width=100, height=100, bg="red")
# button.place(x=0, y=0)
points = {
    0: [0, 0, 100, 0, 100, 150, 0, 150, 30, 120, 70, 120, 70, 30, 30, 30, 30, 120, 0, 150],
    1: [0],
    7: [0, 0, 100, 0, 70, 150, 45, 150, 65, 30, 0, 30],
    8: [0, 30, 20, 30, 40, 30, 40, 60, 60, 60, 60, 30, 40, 30, 20, 30, 20, 0, 80, 0, 80, 30, 100, 30, 100, 60, 80, 60, 80, 90, 100, 90, 100, 120, 80, 120, 80, 150, 20, 150, 20, 120, 40, 120, 60, 120, 60, 90, 40, 90, 40, 120, 20, 120, 0, 120, 0, 90, 20, 90, 20, 60, 0, 60, 0, 30]
}

attack = 870
digits = [int(digit) for digit in str(attack)]

for digit in range (0, len(digits)):
    if digit == 0:
        canvas.create_polygon(points[digits[digit]], fill="red")
    else: 
        for index in range (0, len(points[digits[digit]])):
            if (index == 0) or (index %2 == 0):
                points[digits[digit]][index] += (110*digit)
        canvas.create_polygon(points[digits[digit]], fill="red")
    

# canvas.create_polygon(points[8], fill="red")
# for index in range (0, len(points[0])):
#     print(index)
#     if (index == 0) or (index %2 == 0):
#         points[0][index] += 110
# canvas.create_polygon(points[0], fill="red")


# rec = canvas.create_rectangle(0, 0, 100, 100, fill="red")

# def test(event=None, x=0):
#     x = 12
#     canvas.move(rec, x, 0)
#     x1, y1, x2, x2 = canvas.coords(rec)
#     if x1 >= 400:
#         print("done")
#         master.unbind("<Return>")
#     else:
#         canvas.after(16, test)

# x = 0
#master.bind("<Return>", lambda event: test(event))
# canvas.after(1000, lambda: canvas.move(rec, 0, 400))
# #canvas.move(rec, 400, 400)
master.mainloop()


