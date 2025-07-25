from tkinter import *

root = Tk()
root.geometry("300x200")

top_btn = Button(root, text="Top")
top_btn.pack(side=TOP, fill=X)

bottom_btn = Button(root, text="Bottom")
bottom_btn.pack(side=BOTTOM, fill=X)
left_btn = Button(root, text="Left")
left_btn.pack(side=LEFT, fill=Y)
right_btn = Button(root, text="Right")
right_btn.pack(side=RIGHT, fill=Y)

center_label = Label(root, text="Center Area", bg="lightblue")
center_label.pack(expand=True, fill=BOTH)

root.mainloop()


