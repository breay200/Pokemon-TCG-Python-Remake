from tkinter import *
def messageWindow():
    win = Toplevel()
    win.title('warning')
    message = "This will delete stuff"
    Label(win, text=message).pack()
    Button(win, text='Delete', command=win.destroy).pack()
root = Tk()
Button(root, text='Bring up Message', command=messageWindow).pack()
root.mainloop()