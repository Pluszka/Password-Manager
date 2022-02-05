from tkinter import *
from tkinter import messagebox
from generator import gen
import pyperclip
FONT_DESC = ("Courier", 10, 'bold')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def random_password():
    generated = gen()
    password.delete(0, END)
    password.insert(1,generated)
    pyperclip.copy(generated)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    input_website = website.get()
    input_login = login.get()
    input_password = password.get()

    if check_input(input_website, input_login, input_password):
        with open('Password_data.txt', 'a') as file:
            file.write(f'{input_website} | {input_login} | {input_password}\n\n')
        website.delete(0, END)
        password.delete(0, END)
    else:
        messagebox.showinfo(title='Error', message='Founded blank field.')


def check_input(web, log, passw):
    if len(web) > 1 and len(log) > 1 and len(passw) > 1:
        return True
    return False


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
website.focus()

login = Entry(width=55)
login.grid(row=2, column=1, columnspan=2, sticky='w')
login.insert(END, 'youremail@gmail.com')

password = Entry(width=25)
password.grid(row=3, column=1, sticky='w')

generate = Button(text='Generate Password', width=15, command=random_password)
generate.grid(row=3, column=2, sticky='w')

add = Button(text='Add', width=45, command=save)
add.grid(row=4, column=1, columnspan=2, sticky='w')

root.mainloop()
