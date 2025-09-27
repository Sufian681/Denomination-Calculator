from tkinter import *

def check_strength():
    pwd = entry.get()
    if len(pwd) == 0:
        result_label.config(text="Please enter a password", fg="red")
    elif len(pwd) < 6:
        result_label.config(text="Weak Password", fg="red")
    elif len(pwd) < 10:
        result_label.config(text="Moderate Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")

root = Tk()
root.geometry("350x200")
root.title("Password Strength Checker")
root.configure(bg='lightblue')

label = Label(root, text="Enter your password:", bg='lightblue')
label.pack(pady=10)

entry = Entry(root, show="*", width=30)
entry.pack(pady=5)

check_btn = Button(root, text="Check Strength", command=check_strength, bg='blue', fg='white')
check_btn.pack(pady=10)

result_label = Label(root, text="", bg='lightblue', font=('Arial', 12, 'bold'))
result_label.pack(pady=10)

root.mainloop()