from tkinter import *
from tkinter import messagebox

import random
import pyperclip
import json


def save_data():
    web = web_input.get()
    passs = pass_inp.get()
    name = name_input.get()
    json_data = {
        web: {
            "email": name,
            "password": passs,
        }

    }

    if name == "" or passs == "" or web == "":
        messagebox.showinfo(title="Invalid Request", message="sia you no enter anything you want save what?")
        return
    # messagebox.showinfo(title="Save data",message="Are you sure the details are correct")
    # line abv issa type of dialog with only one option- OK
    pop_up = messagebox.askokcancel(title=web, message=f"mail: {name}, password: {passs}, save the data?")
    # dialog returns a bool
    if pop_up:
        # to update you need 3 operations
        # read update and then write
        try:
            with open('entered_data_json.json', 'r') as json_file:
                data = json.load(json_file)

        except FileNotFoundError:
            with open('entered_data_json.json', 'w') as json_file:
                json.dump(json_data, json_file, indent=4)

        else:
            data.update(json_data)
            with open('entered_data_json.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            # LINE BELOW  to clear all inp fields so you can enter other data
            web_input.delete(0, END)
            pass_inp.delete(0, END)


# we will not clear the email input cos  its yours
# and you are saving your data for various sites

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for i in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for j in range(nr_symbols)]
    pass_nums = [random.choice(numbers) for k in range(nr_numbers)]

    password_list = pass_letters + pass_symbols + pass_nums
    random.shuffle(password_list)

    password = ''.join(password_list)

    # in order to give this password to the user we will use the insert func
    # just like how we used it to insert a base email same can be done here too
    pass_inp.insert(0, password)
    pyperclip.copy(password)
#line abv allos you to automatically copy the generated password
#first import will not import message box since message
#box is not a class or constant
web_input=Entry(width=35)
web_input.grid(column=1,columnspan=2,row=1)
web_input.focus()
def search_site():
    web = web_input.get()

    #web = web_input.get()

    sites_list=[]
    with open('entered_data_json.json') as file:
        jsonn=json.load(file)
        for key,value in jsonn.items():
            print(key,value)
            sites_list.append(key)
    if web in sites_list:
        messagebox.showinfo(title=f" Your info for {web}  ", message=f" {jsonn[web]['email']} \n {jsonn[web]['password']}")
    else:
        messagebox.showinfo(title=" Unavailable",
                            message="sia you never go that site how you go get credentials?")

window= Tk()
window.title("Password Manager")
window.config(pady=100,padx=224)
#to create the timer we use the after function
#after a specific amnt of time it will call a func
# it takes the time,func and the args of the func

#to add img we need canvas
# and PhotoImage
canvas= Canvas(width=200,height=224)
lock=PhotoImage(file='logo.png')
canvas.create_image(101,112,image=lock)
canvas.grid(column=1,row=0)

website= Label( text="Website: ")
website.grid(column=0,row=1)
user_name= Label( text="Email/Username: ")
user_name.grid(column=0,row=2)
password= Label( text="Password: ")
password.grid(column=0,row=3)


name_input=Entry(width=35)
name_input.grid(column=1,columnspan=2,row=2)
name_input.insert(0,'sama29571@gmail.com')
#insert func takes an index where cursor should be and the string that should be at that particular input
#val for index can also be END
pass_inp=Entry(width=21)
pass_inp.grid(column=1,columnspan=2,row=3)

search = Button(text="Search",command=search_site)
search.grid(column=2,row=1)

gen_password= Button(text=" Generate Password",command=generate_password)
gen_password.grid(column=2,row=3)


add_password = Button(text=" ADD",width=36,command=save_data)
add_password.grid(column=1,columnspan=2,row=4)

# timer= Label(width=10, text="Timer")
# timer.grid(column=1,row=0)
# reset= Button(width=10, text="Reset")
# reset.grid(column=2,row=2)
#
# check_marks= Label(text=" ✔")
# check_marks.grid(column=1,row=2)






window.mainloop()