from thinker import *

def callback():
    button["text"] = "클릭됨"

window = Tk()
lbl1 = Label(window, text="Enter")
btn1 = Button(window, text="1", command=lambda: callback())
btn2 = Button(window, text="2", command=lambda: callback())


lbl1.pack()
btn1.pack(side=LEFT, padx=5)
btn2.pack(side = RIGHT, padx=5)
window.mainloop()