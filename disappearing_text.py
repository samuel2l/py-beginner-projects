from tkinter import *

# LOGIC
user_text = ""
timer = None


def start_calculating(event):
    global timer, user_text

    if timer is not None:
        window.after_cancel(timer)

    if event.keysym == "BackSpace":
        user_text = user_text[0: len(user_text) - 1]

    elif event.char:
        user_text += event.char
        timer = window.after(4000, reset_app)

    return


def reset_app():
    global timer, user_text
    typing_area.delete('1.0', 'end')
    user_text = ""
    timer = None
    return


def save_text():
    global user_text
    if user_text == "":
        return
    try:
        f = open('writeups.txt', 'r')
    except FileNotFoundError:
        f = open('writeups.txt', 'w')
        f.write(user_text)
        user_text = ""
        return
    else:
        cont = f.read()
        if cont == "":
            text_to_write = user_text
        else:
            text_to_write = f'\n{user_text}'

        with open('writeups.txt', 'a') as f:
            f.write(text_to_write)
            user_text = ""
    finally:
        return


# UI SETUP








window = Tk()
window.title('Disappearing Text Desktop App')
window.config( padx=20, pady=10)


instruction = Label(text="After 4 seconds of inactivity your text disappears" ,pady=10)
typing_area = Text(
                   width=100, height=15, wrap='w',

                   padx=5, pady=5)
typing_area.bind('<KeyPress>', start_calculating)
reset_btn = Button(text='Restart',

                   command=reset_app, width=20)

save_btn = Button(text='Save work', border=3,
                  command=save_text, width=20)
instruction.grid(row=2, column=0,columnspan=3)
typing_area.grid(row=3, column=0,columnspan=3)
reset_btn.grid(row=4, column=0)
save_btn.grid(row=4, column=2)

window.mainloop()