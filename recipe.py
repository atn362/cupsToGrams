from tkinter import *

# entry widget = textbox that accepts a single line of user input


def submit():
    userInput = entry.get()
    print("Hello "+userInput)


def clear():
    entry.delete(0, END)


def delete():
    entry.delete(0, 1)


def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()

entry = Entry(window,
              font=("Courier", 50),
              fg="blue",
              bg="white")

# entry.insert(0,'Spongebob')
# entry.config(show="*")
# entry.config(state=DISABLED)

entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

clear_button = Button(window, text="clear", command=clear)
clear_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
