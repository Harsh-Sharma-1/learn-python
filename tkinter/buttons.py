from tkinter import *

count = 0


def click():
    global count
    count += 1
    print('you clicked the button', count)


window = Tk()
photo = PhotoImage(file='./assets/like.png')
button = Button(window, text='Click me', command=click,
                font=("Comic Sans", 30), fg="#00ff00", bg="black",
                activeforeground='green', activebackground='black',
                state=ACTIVE
                )
button.pack()

window.mainloop()
