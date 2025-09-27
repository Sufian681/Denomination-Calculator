from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("400x300")
root.title("Denomination")
root.configure(bg='lightblue')

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='lightblue')
label.place(x=50, y=20)  # Adjusted x to fit image in window

label1 = Label(root,
               text="Hey! Welcome to Denomination",
               bg='lightblue', )
label1.place(relx=0.5, y=250, anchor=CENTER)  # Adjusted y to fit in window

def topwin():
    top = Toplevel()
    top.geometry("400x300")
    top.title("Denomination")
    top.configure(bg='lightgreen')

    label = Label(top, text="Enter Total amount", bg='lightgreen')
    entry = Entry(top)
    lbl = Label(top, text="Denominations", bg='lightgreen')  # Fixed typo: Labbel -> Label

    l1 = Label(top, text="2000", bg='lightgreen')
    l2 = Label(top, text="500", bg='lightgreen')
    l3 = Label(top, text="200", bg='lightgreen')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note200 = amount // 200

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note200))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid amount")

    label.place(x=130, y=30)
    entry.place(x=130, y=60)
    lbl.place(x=130, y=90)
    l1.place(x=80, y=130)
    l2.place(x=160, y=130)
    l3.place(x=240, y=130)
    t1.place(x=80, y=160)
    t2.place(x=160, y=160)
    t3.place(x=240, y=160)
    btn = Button(top, text="Calculate", command=calculator, bg='blue', fg='white')
    btn.place(x=170, y=200)

def msg():
    MsgBox = messagebox.askokcancel(
        "Alert", "Do you want to proceed?")  # Changed to askokcancel for Yes/No
    if MsgBox:
        topwin()

button1 = Button(root,
                 text="Let's Start",
                 command=msg,
                 bg='blue',
                 fg='white')
button1.place(x=150, y=270)  # Adjusted y to fit in window

root.mainloop()