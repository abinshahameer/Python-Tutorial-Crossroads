from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Abinshah")
window.configure(bg="#79D02D")


def hello():
    print("Button Clicked")


button1 = Button(window, text="ok", command=hello)  # width calculated based on zero
button2 = Button(window, text="ok", command=hello)
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
label = Label(window, text="welcome")
# button1.pack()
# button2.pack()
# label.pack()
window.mainloop()
