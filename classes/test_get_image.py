import tkinter as tk
import time
import random

master = tk.Tk()
width = int(master.winfo_screenwidth() * 0.75)
height = int(master.winfo_screenheight() * 0.75)
master.geometry(f"{width}x{height}")
master.title("TCG REMAKE")

canvas = tk.Canvas(master, width=width, height=height)
canvas.place(x=0,y=0)

# points = {
#     0: [(0, 0), (100, 0), (100, 150), (0, 150), (30, 120), (70, 120), (70, 30), (30, 30), (30, 120), (0, 150)],
#     1: [(10,30), (40, 30), (40, 0), (70, 0), (70, 120), (100, 120), (100, 150), (10, 150), (10, 120), (40, 120), (40, 60), (10, 60)],
#     2: [(0, 0), (100, 0), (100, 90), (30, 90), (30, 120), (100, 120), (100, 150), (0, 150), (0, 60), (70, 60), (70, 30), (0, 30), (0, 0)],
#     3: [(0, 0), (100, 0), (100, 150), (0, 150), (0, 120), (70, 120), (70, 90), (0, 90), (0, 60), (70, 60), (70, 30), (0, 30)],
#     4: [(0, 0), (30, 0), (30, 60), (70, 60), (70, 0), (100, 0), (100, 150), (70, 150), (70, 90), (0, 90)], 
#     "4 original": [(0, 60), (50, 0), (80, 0), (80, 60), (100, 60), (100, 90), (80, 90), (80, 150), (50, 150), (50, 90), (0, 90), (30, 60), (50, 60), (50, 30), (30, 60), (0, 90)],
#     5: [(0, 0), (100, 0), (100, 30), (30, 30), (30, 60), (100, 60), (100, 150), (0, 150), (0, 120), (70, 120), (70, 90), (0, 90)],
#     6: [(0, 0), (100, 0), (100, 30), (30, 30), (30, 60), (100, 60), (100, 150), (0, 150), (30, 120), (70, 120), (70, 90), (30, 90), (30, 120), (0, 150)],
#     7: [(0, 0), (100, 0), (100, 90), (70, 90), (70, 150), (40, 150), (40, 90), (70, 90), (70, 30), (0, 30)],
#     "7 original": [(0, 0), (100, 0), (70, 150), (45, 150), (65, 30), (0, 30)],
#     8: [(0, 0), (30, 30), (30, 60), (70, 60), (70, 30), (30, 30), (0, 0), (100, 0), (100, 150), (0, 150), (30, 120), (70, 120), (70, 90), (30, 90), (30, 120), (0, 150)],
#     "8bit": [(0, 30), (20, 30), (40, 30), (40, 60), (60, 60), (60, 30), (40, 30), (20, 30), (20, 0), (80, 0), (80, 30), (100, 30), (100, 60), (80, 60), (80, 90), (100, 90), (100, 120), (80, 120), (80, 150), (20, 150), (20, 120), (40, 120), (60, 120), (60, 90), (40, 90), (40, 120), (20, 120), (0, 120), (0, 90), (20, 90), (20, 60), (0, 60), (0, 30)],
#     9: [(0, 0), (100, 0), (100, 150), (70, 150), (70, 80), (0, 80), (30, 50), (70, 50), (70, 30), (30, 30), (30, 50), (0, 80)]
# }

# attack = random.randint(0, 999999999)
# digits = [int(digit) for digit in str(attack)]
# print(digits)
# for digit in range (0, len(digits)):
#     if digit == 0:
#         canvas.create_polygon(points[digits[digit]], fill="red")
#     else: 
#         coords_list = []
#         for tup in points[digits[digit]]:
#             for index in range(0, len(tup)):
#                 if index == 0:
#                     x = tup[index] + (110*digit)
#                     coords_list.append(x)
#                 else:
#                     coords_list.append(tup[index])
#         canvas.create_polygon(coords_list, fill="red")

max_health = 60
current_health = 40
ratio = current_health/max_health
max_x = int(100 * ratio)
green = [(0, 0), (max_x, 0), (max_x, 30), (0, 30)]
red = [(max_x, 0), (100, 0), (100, 30), (max_x, 30)]
canvas.create_polygon(green, fill="green")
canvas.create_polygon(red, fill="red")


# for index in range (0, len(points[digits[digit]])):
#     if (index == 0) or (index %2 == 0):
        
#         points[digits[digit]][index] += (110*digit)
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


