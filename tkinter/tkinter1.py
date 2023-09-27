#MILES TO KM
#UI NOT NICE JUST FUNCTIONALITY WORKING
from tkinter import *

def on_entering_data():
    input_text=input.get()

    my_label.config(text=f"{int(input_text) *1.6}")
#window is equivalent of screen in turtle
window = Tk()
window.title("My first tkinter program")
window.minsize(width=500, height=300)
#to add padding to entire window:
window.config(padx=20,pady=20)
input= Entry(width=20)
input.get()
input.pack()

my_label= Label(text=" ", font=("Arial",24,"bold"))
my_label.pack()
#my_label.pack()
#this line abv alone will not print it unto screen
#cos we need to specify how it will be laid out unto screen
#eg using the pack() will pack it to the centre of screen( width wise)
#but in terms of length all components are laid out from the beginning of screen vertically downwards
# but you can change position and direction of laying out objs by passing a side="" argument
#it takes bottom, top etc
#so if you set side to left it means every element will be added from left horizontally
#problem with using pack though is precision in laying out components
#to address this the place function is used instead
# the font argument is optional

#to change configs of some components you have created

# eg the label
#my_label['text']="NEW TEXT"
#OR:

#BUTTONS:


def button_click():
    my_label.config(text="BTN CLICKEDD")
#to listen to events the command keyword is used and its val is a func name not func call like in turtle

btn2=Button(text="Calculate", command=on_entering_data)
btn2.pack()
#INPUT
#done using the entry class











window.mainloop()