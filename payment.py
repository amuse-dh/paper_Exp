from tksheet import Sheet
import tkinter as tk
import pandas as pd
from tkinter import messagebox


def payment():
    class demo(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)
            self.title("결제화면")
            self.geometry("720x480")
            self.grid_columnconfigure(100, weight=1)
            self.grid_rowconfigure(100, weight=1)
            self.frame = tk.Frame(self)
            self.frame.grid_columnconfigure(0, weight=1)
            self.frame.grid_rowconfigure(0, weight=1)
            self.sheet = Sheet(
                self.frame,
                data=pd.read_csv("count.csv").values.tolist(),
            )
            self.sheet.enable_bindings()
            self.frame.grid(row=0, column=0, sticky="nswe")
            self.sheet.grid(row=0, column=0, sticky="nswe")
            accept_btn = tk.Button(text = '결제', width= 20, height=5, background='gray')
            tk.Button.grid_configure(accept_btn, column=100)
            accept_btn.config(command = decide)
            cancel_btn = tk.Button(text='취소', width=20, height=5, background='gray')
            tk.Button.grid_configure(cancel_btn, column=100)
            cancel_btn.config(command=cancel)


    def decide():
        data = pd.read_csv("count.csv")
        data.to_csv("result.csv", index=False, mode='w')
        messagebox.showinfo(title='결제', message='결제완료')

    def cancel():
        messagebox.showinfo(title='결제', message='취소완료')



    app = demo()
    app.mainloop()