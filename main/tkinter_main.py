import tkinter
from buttons import ButtonClass


from commands import maximize, minimize

class TkinterWindow(tkinter.Tk):
    num = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('600x400')
        self.remake_frame()
        self.create_frame()
        self.minimized = False
        self.maximized = False
        self.saved_size = ""
        self.current_state = self.wm_state()

        #Helpful for identifying the window. setting title to "Notes" + num
        TkinterWindow.num += 1


    def load_settings(self, *args, **kwargs):
        #change this to open the json file
        self.config(*args, **kwargs)

    def remake_frame(self):
        #rename this, for now just set alpha and remove frame
        # self.overrideredirect(True) #Remove frame
        self.wm_attributes("-alpha", 0.75)

    def create_frame(self):
        self.win_frame = tkinter.Frame(self, background="purple", bd=0)
        self.win_frame.pack(fill='x')

        self.exit_button = ButtonClass(master = self.win_frame, background="red", 
            command = lambda: self.destroy(), text="X")
        self.exit_button.pack(side='right')
        
        self.new_notepad = ButtonClass(master = self.win_frame, text="+")
        self.new_notepad.pack(side='left')

        self.maximize_button = ButtonClass(master = self.win_frame,
                                            text= "🗖", 
                                            command = lambda : maximize(self, self.maximize_button))
        self.maximize_button.pack(side='right')

        

        self.minimize_button = ButtonClass(master = self.win_frame, 
                                           text= "🗕",
                                           command = lambda : minimize(self))
        self.minimize_button.pack(side='right')





if __name__ == "__main__":
    tk = TkinterWindow()
    tk.geometry('600x400')

    print(tk.geometry)

    tk.mainloop()