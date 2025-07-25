from thinker import *

window = Tk()
lbl1 = Label(window, text="Enter")
btn1 = Button(window, text="1", command=lambda: print("1"))
btn2 = Button(window, text="2", command=lambda: print("2"))

lbl1.pack()
btn1.pack()
btn2.pack()
window.mainloop()