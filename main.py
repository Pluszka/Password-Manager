from tkinter import *
FONT_DESC = ("Courier", 10, 'bold')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Password Manager')
root.config(padx=50, pady=50)

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

website = Entry(width=55)
website.grid(row=1, column=1, columnspan=2, sticky='w')

login = Entry(width=55)
login.grid(row=2, column=1, columnspan=2, sticky='w')

password = Entry(width=25)
password.grid(row=3, column=1, sticky='w')

generate = Button(text='Generate Password', width=15)
generate.grid(row=3, column=2, sticky='w')

add = Button(text='Add', width=45)
add.grid(row=4, column=1, columnspan=2, sticky='w')

root.mainloop()
