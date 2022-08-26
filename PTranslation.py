from tkinter import *
from googletrans import Translator

translator = Translator()

counter = False
default = False
mode = 'en'

def trans(event, mode):
    global mode
    global counter
    words = entry.get()
    result = translator.translate(words, src='ms', dest=mode).text
    entry.delete(0, END)
    entry.insert(string=result, index=0)
    counter = True

def ontop():
    window.lift()
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    entry.focus_force()

def clear_field(event):
    global counter
    if counter == True:
        entry.delete(0, END)
        entry.insert(string=event.char, index=0)
        counter = False

def change_mode():
    global mode
    global default
    default = not default 
    if default == True:
        mode = 'zh-CN'
        button.configure(text="华语")
    else:
        mode = 'en'
        button.configure(text="English")

window = Tk()
window.title("PTranslate")
entry = Entry(fg="white", bg="black", width=37, font=(None, 18), justify='center')
button = Button(text="English", width=44, height=1, bg="purple", fg="white", command=lambda: change_mode())
window.bind("<Return>", lambda event: trans(event)) 
window.bind("<Key>", lambda event: clear_field(event))

entry.pack()
button.pack()
ontop()
window.mainloop()
