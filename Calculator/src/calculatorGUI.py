import tkinter as tk
import tkmacosx

#Definitions for calculator

calculations = []

#Keypresses
def keypress(value):
    calculations.extend(value)
    print(calculations)
    screen = tk.Label (
        text=calculations,
        height="1",
    )
    screen.grid(
        row=1,
        column=0,
        columnspan=4,
    )

def operatorpress(operator):
    calculations.extend(operator)
    print(calculations)
    screen = tk.Label (
        text=calculations,
        height="1",
    )
    screen.grid(
        row=1,
        column=0,
        columnspan=4,
    )
def deletepress():
    calculations.pop(-1)
    print(calculations)
    screen = tk.Label (
        text=calculations,
        height="1",
    )
    screen.grid(
        row=1,
        column=0,
        columnspan=4,
    )

def finalequation():
    finalcalculations = "".join(calculations)
    answer = eval(finalcalculations)
    print(answer)
    screen = tk.Label (
        text=answer,
        height="1",
        width="30"
    )
    screen.grid(
        row=1,
        column=0,
        columnspan=4,
    )

#Window Config
gui = tk.Tk()
gui.title("Calculator!!")
gui.configure(bg="white")
gui.resizable(0, 0)
gui.geometry("340x440+600+200")

#Screen!
screen = tk.Label (
    height="2",
)
screen.grid(
    row=1,
    column=0,
    columnspan=4,
)
#Buttons!
one = tk.Button(
    text="1",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command=lambda: keypress("1"),

)
one.grid(
    row=4,
    column=0,
)

two = tk.Button(
    text="2",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command=lambda: keypress("2"),

)
two.grid(
    row=4,
    column=1,
)

three = tk.Button(
    text="3",
    foreground="black",
    bg="grey36",
    width="10",
    height="5",
    command=lambda: keypress("3"),

)
three.grid(
    row=4,
    column=2,
)

four = tk.Button(
    text="4",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command=lambda: keypress("4"),

)
four.grid(
    row=3,
    column=0,
)

five = tk.Button(
    text="5",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command=lambda: keypress("5"),
)
five.grid(
    row=3,
    column=1,
)

six = tk.Button(
    text="6",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command=lambda: keypress("6"),
)
six.grid(
    row=3,
    column=2,
)

seven = tk.Button(
    text="7",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command=lambda: keypress("7"),
)
seven.grid(
    row=2,
    column=0,
)
eight = tk.Button(
    text="8",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command=lambda: keypress("8"),
)
eight.grid(
    row=2,
    column=1,
)

nine = tk.Button(
    text="9",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command=lambda: keypress("9"),

)
nine.grid(
    row=2,
    column=2,
)

zero = tk.Button(
    text="0",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command=lambda: keypress("0"),

)
zero.grid(
    row=5,
    column=1,
)

clear = tk.Button(
    text="DEL",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command= lambda: deletepress(),

)
clear.grid(
    row=5,
    column=0,
)

decimal = tk.Button(
    text=".",
    foreground="black",
    background="grey36",
    width="10",
    height="5",
    command= lambda: operatorpress("."),

)
decimal.grid(
    row=5,
    column=2,
)

plus = tk.Button(
    text="+",
    foreground="black",
    background="grey36",
    width="6",
    height="5",
    command=lambda: operatorpress("+"),
)
plus.grid(
    row=2,
    column=3,
)
minus = tk.Button(
    text="-",
    foreground="black",
    background="grey36",
    width="6",
    height="5",
    command= lambda: operatorpress("-"),

)
minus.grid(
    row=3,
    column=3,
)

multiply = tk.Button(
    text="x",
    foreground="black",
    background="grey36",
    width="6",
    height="5",
    command= lambda: operatorpress("*"),

)
multiply.grid(
    row=4,
    column=3,
)

divide = tk.Button(
    text="÷",
    foreground="black",
    background="grey36",
    width="6",
    height="5",
    command= lambda: operatorpress("/"),

)
divide.grid(
    row=5,
    column=3,
)

enter = tk.Button(
    text="=",
    foreground="black",
    background="grey36",
    width="37",
    height="4",
    command= lambda: finalequation(),

)
enter.grid(
    row=6,
    column=0,
    columnspan=4,
    sticky="N"
)
gui.mainloop()