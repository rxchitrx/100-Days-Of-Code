from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers

  shuffle(password_list)

  password = "".join(password_list)
  pyperclip.copy(password)

  password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website = website_entry.get()
    username = user_entry.get()
    password = password_entry.get()

    if len(website) or len(password) == 0:
        messagebox.showwarning(title="OOPS!", message="You can't leave any fields empty.")
    else:
        if messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it okay to save?"):
            with open("data.txt", "a") as data:
                data.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width = 200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text = "Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "email@email.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width = 21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Add", width=36, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()


