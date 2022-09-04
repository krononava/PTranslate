from tkinter import *
from googletrans import Translator
import threading
from pynput import keyboard
import time
import ctypes

translator = Translator()
set_to_foreground = ctypes.windll.user32.SetForegroundWindow

counter = False
default = False
mode = 'en'
t = 0

def trans(event):
    global mode
    global counter
    words = entry.get()
    from_bm = translator.translate(words, src='ms', dest=mode).text
    to_bm = translator.translate(words, src=mode, dest='ms').text
    if from_bm != words:    # check if words is english or bm
        result = from_bm
    else:
        result = to_bm
    entry.delete(0, END)
    entry.insert(string=result, index=0)
    counter = True

def ontop():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    keyboard.Controller().press(keyboard.Key.alt)
    keyboard.Controller().release(keyboard.Key.alt)
    set_to_foreground(window.winfo_id())
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

def delay():
    global t
    time.sleep(0.4)
    t = 0

def on_release(key):
    global t
    if key == keyboard.Key.ctrl_l:
        if t == 0:
            timer = threading.Thread(target=delay, daemon=True)
            timer.start()
        t += 1
        if t >= 2:
            ontop()

listener = keyboard.Listener(on_release=on_release)
listener.start()

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