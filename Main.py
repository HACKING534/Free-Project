import pyttsx3
import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from time import sleep

voice = pyttsx3.init()

window = tk.Tk()
window.geometry("300x300")
window.title("My App ")
window.resizable(width=False, height=False)

def On_click():
    voice.say("Hello Python ")
    voice.runAndWait()
    sleep(2)
    voice.say("Welcome to Python")
    voice.runAndWait()

button = tk.Button(window, text="Click Me", command=On_click)
button.pack()
if __name__ == '__main__':
    window.mainloop()