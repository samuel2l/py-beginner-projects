# importing all libraries
from tkinter import messagebox

from tkinter import *
from timeit import default_timer as timer
import random

# creating window using gui
window = Tk()

# the size of the window is defined
window.geometry("450x200")

x = 0


# defining the function for the test
def game():
    global x

    # loop for destroying the window
    # after on test
    if x == 0:
        window.destroy()
        x = x + 1

    # defining function for results of test
    def check_result():
        global end
        if entry.get() == words[word]:
            end = timer()
            # score = Tk()
            # score.geometry("450x200")

            # use label method of tkinter for labeling in window
            messagebox.showinfo(title="Typing Test result", message=f'completed in {end - start}s')
        else:

            messagebox.showerror(title="Invalid input",
                                 message=" You entered something different from what the test specified")

    words = {
        '100 words': ('Τhe quick brοwn fοx jumps οver the lazy dοg.Νοw is the time fοr all gοοd men tο cοme tο the '
                      'aid οf their cοuntry. '
                      'Ρack my bοx with five dοzen liquοr jugs Α jοurney οf a thοusand miles begins with a single step '
                      'Α hοuse which is divided against itself cannοt stand Τhοse whο fοrget histοry are cοndemned tο '
                      'repeat it '
                      'Ρeοple whο live in glass hοuses shοuld nοt thrοw stοnes Τhe prοοf οf the pudding is always in '
                      'the eating '
                      'Dο nοt cοunt yοur chickens befοre they are hatched Fοr want οf a nail the kingdοm was lοst'),
        '50 words': "The serene sunset painted the sky in hues of orange and pink, casting a warm glow over the tranquil beach. Waves gently kissed the shore as seagulls soared above. People strolled hand in hand, savoring the moment. Laughter filled the air, creating a perfect evening to cherish.",
        '10 words': "The serene sunset over the tranquil beach cast a warm glow.",


    }

    dict_keys = [key for key, value in words.items()]
    word=random.choice(dict_keys)
    # start timer using timeit function
    start = timer()
    windows = Tk()
    windows.geometry("600x600")

    # use label method of tkinter for labeling in window
    x2 = Label(windows, text=words[word], font="times 10", wraplength=400)
    # place of labeling in window
    x2.place(x=150, y=10)
    x3 = Label(windows, text="Start Typing", font="times 20")
    x3.place(x=10, y=250)

    entry = Entry(windows)
    entry.place(x=280, y=255,width=300, height=30)

    # buttons to submit output and check results
    b2 = Button(windows, text="Done",
                command=check_result, width=12, bg='blue')
    b2.place(x=150, y=300)

    b3 = Button(windows, text="Try Again",
                command=game, width=12, bg='blue')
    b3.place(x=250, y=300)
    windows.mainloop()


x1 = Label(window, text="", font="times 20")
x1.place(x=10, y=50)

b1 = Button(window, text="Start whenever you are ready", command=game, width=25, bg='grey')
b1.place(x=150, y=100)

# calling window
window.mainloop()
