from pydoc import text
import tkinter as tk
from tkinter import *
from tkinter import font

### - Initialization
Violet = '#b7b1b2'
Purple = '#4b3d8f'
Green = '#37a987'

root = Tk()
root.config(bg=Violet)

Font_Comic_Sans = tk.font.Font(family = 'Proxima Nova', weight = 'bold', size = 32)
Font_Comic_Sans_Lower = tk.font.Font(family = 'Proxima Nova', weight = 'bold', size = 18)
Font_Comic_Sans_Ultra_Lower = tk.font.Font(family = 'Proxima Nova', weight = 'bold', size = 14)


### - Break

sign_up_canvas = tk.Canvas(root, bg=Violet, highlightthickness=0)
sign_up_canvas.grid()

welcome = Label(sign_up_canvas, text = 'Username', bg = Violet, fg=Purple)
welcome.config(font=Font_Comic_Sans_Ultra_Lower)
welcome.grid(pady=8)

new_username = tk.Entry(sign_up_canvas, text='Username', bg=Violet)
new_username.grid(padx=10, pady=5)



root.mainloop()