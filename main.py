from tkinter import *
FONT_DESC = ("Courier", 12, 'bold')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Password Manager')
root.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock)
canvas.grid(row=0, column=1)


label1 = Label(text='Website:', font=FONT_DESC)
label1.grid(row=1, column=0)

label2 = Label(text='Email/Login:', font=FONT_DESC)
label2.grid(row=2, column=0)

label1 = Label(text='Password:', font=FONT_DESC)
label1.grid(row=3, column=0)

root.mainloop()
