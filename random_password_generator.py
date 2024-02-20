import random
import string
import tkinter as tk
import pyperclip

class PasswordGeneratorApp():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title = ('Password Generator')
        self.window.geometry = ('300*220')
        
        length_label = tk.Label(self.window, text= "password length:", font = ('',12))
        length_label.grid(row=0,column=0,
        sticky= tk.W)
        self.length_Var = tk.IntVar(value=12)
        self.length_Spinbox= tk.Spinbox(self.window,from_=1,to=100,width= 5 ,font=('',12),textvariable= self.length_Var)
        self.length_Spinbox.grid(row=0,column=1)
        
        self.lowercase_var= tk.BooleanVar()
        lowercase_checkbox= tk.Checkbutton(self.window,text="lowercase",
        variable=self.lowercase_var,font=('',12))
        lowercase_checkbox.grid(row=1,column=0 ,sticky= tk.W)
        
        self.uppercase_var= tk.BooleanVar()
        uppercase_checkbox= tk.Checkbutton(self.window,text="uppercase",
        variable=self.uppercase_var,font=('',12))
        uppercase_checkbox.grid(row=2,column=0 ,sticky= tk.W)
        
        
        self.digits_var= tk.BooleanVar()
        digits_checkbox= tk.Checkbutton(self.window,text="digit",
        variable=self.digits_var,font=('',12))
        digits_checkbox.grid(row=3,column=0 ,sticky= tk.W)
        
        self.symbols_var= tk.BooleanVar()
        symbols_checkbox= tk.Checkbutton(self.window,text="symbol",
        variable=self.symbols_var,font=('',12))
        lowercase_checkbox.grid(row=4,column=0 ,sticky= tk.W)
        
        generate_button = tk.Button(self.window,text= 'Generate',command=self.generate_password,font=('',12))
        generate_button.grid(row=5,column=0,sticky=tk.W)
        
        self.password_display = tk.Entry(self.window,width=30)
        self.password_display.grid(row=5,column=1)
        
        copy_button= tk.Button(self.window,text='copy',command= self.copy_password,font=('',12))
        copy_button.grid(row=6,column=0,columnspan=2,sticky=tk.W+tk.E)
        
        self.window.mainloop()
        
    def generate_password(self):
        length = int(self.length_Var.get())
        lowercase = self.lowercase_var.get()
        uppercase = self.uppercase_var.get()
        digits= self.digits_var.get()
        symbols=self.symbols_var.get()
        try:
            characters= ""
            if lowercase:
                characters+=string.ascii_lowercase
            if uppercase:
                characters+=string.ascii_uppercase
            if digits:
                characters+=string.digits
            if symbols:
                characters+=string.punctuation
            if not characters:
                raise ValueError("at least one of the options must be chosen")
            
            password = " ".join(random.choice(characters)for x in range(length))
            
            self.password_display.delete(0,tk.END)
            self.password_display.insert(0,password)
        
        except ValueError as error:
            self.password_display.delete(0,tk.END)
            self.password_display.insertt(0,str(error))
                
        
        
        
        
    def copy_password(self):
        password= self.password_display.get()
        
        if password:
            pyperclip.copy(password)
        
    
    
if __name__== '__main__':
    
    app = PasswordGeneratorApp()
    