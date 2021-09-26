import tkinter

# make the window
root = tkinter.Tk()
# change the title of the window
root.title("Calculator")
# make the window not resizeable
root.resizable(False, False)
# change the icon
root.iconbitmap(
    "C:\\Users\\milan\\OneDrive - Malostranské gymnázium\\Programming\\calculator\\calculator_icon.ico"
)


# make a function that inserts a character to the entry widget
def button_insert(character):
    entry.insert(tkinter.END, character)


# make an equals function
def equals(event=None):
    global calculation
    try:
        if entry.get() == "mamka":

            calculation.config(text=f"{entry.get()}=")

            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, "🤍🤍🤍🤍")
        elif entry.get() == "spamik":

            calculation.config(text=f"{entry.get()}=")

            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, "🤍")
        elif entry.get() == "kaka":

            calculation.config(text=f"{entry.get()}=")

            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, "🍣")
        elif entry.get() == "milanu":

            calculation.config(text=f"{entry.get()}=")

            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, "🍺")
        elif entry.get() == "mani":

            calculation.config(text=f"{entry.get()}=")

            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, "zlobišo")

        else:
            result = eval(entry.get())

            calculation.config(text=f"{entry.get()}=")

            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, result)
    except (NameError, SyntaxError):
        calculation.config(text=f"{entry.get()}=")

        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, "Error")


# make a "backspace" function
def ce():
    entry.delete(len(entry.get()) - 1, tkinter.END)


# make a clear function
def c(event=None):
    entry.delete(0, tkinter.END)
    calculation.config(text=entry.get())


# make a save function
def MS():
    global M
    M = entry.get()


# make a function to display and delete the saved number
def MRC():
    global M
    if entry.get() == M:
        M = ""

    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, M)


# make a M+ function
def M_plus():
    global M
    insert = f"{M}+{entry.get()}"

    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, eval(insert))
    calculation.config(text=f"{insert}=")


# make a M- function
def M_minus():
    global M
    insert = f"{M}-{entry.get()}"

    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, eval(insert))
    calculation.config(text=f"{insert}=")


# bind keys to functions
root.bind("<Return>", equals)
root.bind("<Escape>", c)
root.bind("<End>", c)
root.bind("<Home>", lambda x: root.quit())

# define a label that displays the calculation
calculation = tkinter.Label(text="", anchor=tkinter.W, bg="white", font="Calibri 15")

# define the entry widget
entry = tkinter.Entry(font="Calibri 19", borderwidth=10)

# define the buttons
button_0 = tkinter.Button(
    text="0",
    width=6,
    height=2,
    command=lambda: button_insert(0),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_1 = tkinter.Button(
    text="1",
    width=6,
    height=2,
    command=lambda: button_insert(1),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_2 = tkinter.Button(
    text="2",
    width=6,
    height=2,
    command=lambda: button_insert(2),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_3 = tkinter.Button(
    text="3",
    width=6,
    height=2,
    command=lambda: button_insert(3),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_4 = tkinter.Button(
    text="4",
    width=6,
    height=2,
    command=lambda: button_insert(4),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_5 = tkinter.Button(
    text="5",
    width=6,
    height=2,
    command=lambda: button_insert(5),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_6 = tkinter.Button(
    text="6",
    width=6,
    height=2,
    command=lambda: button_insert(6),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_7 = tkinter.Button(
    text="7",
    width=6,
    height=2,
    command=lambda: button_insert(7),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_8 = tkinter.Button(
    text="8",
    width=6,
    height=2,
    command=lambda: button_insert(8),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_9 = tkinter.Button(
    text="9",
    width=6,
    height=2,
    command=lambda: button_insert(9),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_dot = tkinter.Button(
    text=".",
    width=6,
    height=2,
    command=lambda: button_insert("."),
    font="Calibri 15",
    bg="#f9981d",
    activebackground="#f9981d",
)
button_divide = tkinter.Button(
    text="/",
    width=6,
    height=2,
    command=lambda: button_insert("/"),
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_C = tkinter.Button(
    text="C",
    width=6,
    height=2,
    command=c,
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_multiply = tkinter.Button(
    text="*",
    width=6,
    height=2,
    command=lambda: button_insert("*"),
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_subtract = tkinter.Button(
    text="-",
    width=6,
    height=2,
    command=lambda: button_insert("-"),
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_add = tkinter.Button(
    text="+",
    width=6,
    height=2,
    command=lambda: button_insert("+"),
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_equals = tkinter.Button(
    text="=",
    width=6,
    height=2,
    command=equals,
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_open = tkinter.Button(
    text="(",
    width=6,
    height=2,
    command=lambda: button_insert("("),
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_close = tkinter.Button(
    text=")",
    width=6,
    height=2,
    command=lambda: button_insert(")"),
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_CE = tkinter.Button(
    text="CE",
    width=6,
    height=2,
    command=ce,
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_MS = tkinter.Button(
    text="MS",
    width=6,
    height=2,
    command=MS,
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_M_plus = tkinter.Button(
    text="M+",
    width=6,
    height=2,
    command=M_plus,
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_M_minus = tkinter.Button(
    text="M-",
    width=6,
    height=2,
    command=M_minus,
    font="Calibri 15",
    bg="white",
    activebackground="white",
)
button_MRC = tkinter.Button(
    text="MRC",
    width=6,
    height=2,
    command=MRC,
    font="Calibri 15",
    bg="white",
    activebackground="white",
)

# put the calculation in the window
calculation.grid(row=0, column=0, sticky=tkinter.W + tkinter.E, columnspan=4)

# put the entry widget in the window
entry.grid(columnspan=4, row=1, column=0, ipady=11)

# put the buttons in the window
button_0.grid(row=7, column=0)
button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_dot.grid(row=7, column=1)
button_divide.grid(row=4, column=3)
button_C.grid(row=3, column=0)
button_multiply.grid(row=5, column=3)
button_subtract.grid(row=6, column=3)
button_add.grid(row=7, column=3)
button_equals.grid(row=7, column=2)
button_open.grid(row=3, column=2)
button_close.grid(row=3, column=3)
button_CE.grid(row=3, column=1)
button_MS.grid(row=2, column=3)
button_MRC.grid(row=2, column=0)
button_M_minus.grid(row=2, column=1)
button_M_plus.grid(row=2, column=2)

root.mainloop()
