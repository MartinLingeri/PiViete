import math
from tkinter import Tk, END, Entry, Button


def approximationPi(steps):
    if steps == 0:
        return 2
    result = 2 * (2 / math.sqrt(2))
    root = math.sqrt(2)
    i = 0
    while i < steps - 1:
        j = i
        while j < steps - 1:
            root = math.sqrt(2 + root)
            j += 1
        result *= (2 / root)
        root = math.sqrt(2)
        i += 1
    return result


class Approximation:
    def __init__(self, window):
        self.master = window
        window.title("Viete Approximation Pi")
        window.iconbitmap('Pi_icon.ico')
        self.entry = Entry(window, width=33, borderwidth=3)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.createButton()
        self.before = ''

    def createButton(self):
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_clear = self.addButton('C')
        b_equal = self.addButton('=')

        row1 = [b7, b8, b9]
        row2 = [b4, b5, b6]
        row3 = [b1, b2, b3]
        row4 = [b_clear, b0, b_equal]

        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for button in row:
                button.grid(row=r, column=c, columnspan=1)
                c += 1
            r += 1

    def addButton(self, value):
        return Button(self.master, text=value, width=9, command=lambda: self.clickButton(str(value)))

    def clickButton(self, value):
        steps = str(self.entry.get())

        if value == 'C':
            self.before = 'C'
            self.entry.delete(-1, END)
        elif value == '=':
            self.before = '='
            answer = str(approximationPi(int(steps)))
            self.entry.delete(-1, END)
            self.entry.insert(0, answer)
        elif self.before == '=' and value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            self.before = value
            self.entry.delete(-1, END)
            self.entry.insert(0, value)
        else:
            self.before = value
            self.entry.delete(0, END)
            self.entry.insert(0, steps + value)


if __name__ == '__main__':
    myWindow = Tk()

    my_gui = Approximation(myWindow)

    myWindow.mainloop()
