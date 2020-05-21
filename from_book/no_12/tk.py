import tkinter as tk
top=tk.Tk()
tk.mainloop()
btn = tk.Button()
btn.pack()
btn['text'] = 'Click me'
def clicked():
    print("I was clicked!")
#btn['command'] = clicked


btn.config(text="click",command=clicked)
