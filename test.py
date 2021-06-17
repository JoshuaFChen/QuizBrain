from tkinter import *

windows1 = Tk()
windows1.title("TestTitle")
windows1.config(padx=20, pady=20, bg="BLACK")

score_label = Label(text="Score: 0", fg="white", bg="BLACK")
score_label.grid(row=0, column=1)


windows1.mainloop()
