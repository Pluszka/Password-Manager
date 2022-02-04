from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Password Manager')
root.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock)
canvas.grid(row=1, column=1)





root.mainloop()