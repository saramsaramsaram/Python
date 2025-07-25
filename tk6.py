from thinker import *

window = Tk()
lbl1 = Label(window, text="Enter")
btn1 = Button(window, text="1", command=lambda: print("1"))
btn2 = Button(window, text="2", command=lambda: print("2"))


lbl1.pack()
btn1.pack(side=LEFT, padx=5)
btn2.pack(side = RIGHT, padx=5)
window.mainloop()