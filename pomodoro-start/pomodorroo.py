from tkinter import *
from constants import *

window= Tk()
window.title("Pomodoroooo")
window.config(pady=100,padx=224,bg=YELLOW)
#to create the timer we use the after function
#after a specific amnt of time it will call a func
# it takes the time,func and the args of the func

#to add img we need canvas
# and PhotoImage
canvas= Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file='tomato.png')
canvas.create_image(101,112,image=tomato)
canvas.create_text(110,135,text="00:00", font=(FONT_NAME,26))
canvas.grid(column=1,row=1)


#fg=font color
start= Button(width=10, text="Start")
start.grid(column=0,row=2)
timer= Label(width=10, text="Timer",bg=YELLOW,highlightthickness=0,font=(FONT_NAME,50))
timer.grid(column=1,row=0)
reset= Button(width=10, text="Reset")
reset.grid(column=2,row=2)

check_marks= Label(text=" ✔")
check_marks.grid(column=1,row=2)







window.mainloop()