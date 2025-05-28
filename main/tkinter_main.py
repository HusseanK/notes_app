import tkinter
from buttons import ButtonClass
from ctypes import windll


from commands import maximize, minimize


class TkinterWindow(tkinter.Tk):
    num = 0
    windows = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Geometry needs to be fixed and loaded independently
        self.geometry('600x400+300+300')
        
        self.remove_windows_default_frame()
        self.create_frame()
        self.minimized = False
        self.maximized = False
        self.saved_size = ""
        self.current_state = self.wm_state()
        #Useful for refreshing state of window
        TkinterWindow.windows.append(self)
        #Helpful for identifying the window. setting title to "Notes" + num
        TkinterWindow.num += 1



        #Creates the taskbar on the explorer, refreshes every 10ms
        self.after(10, lambda: self.taskbar_window())



    def destroy(self):
        TkinterWindow.windows.remove(self)
        #Need to rewrite destroy to removeself from outerscope
        return super().destroy()

    def load_settings(self, *args, **kwargs):
        #change this to open the json file
        self.config(bg= "#414141", *args, **kwargs)


    def remove_windows_default_frame(self):
        self.overrideredirect(True) #Remove frame


    def create_frame(self):
        buttons=[]
        self.win_frame = tkinter.Frame(self, relief="raised", background=ButtonClass.dark_background,
                                        bd=0, highlightbackground="black", highlightthickness=1)
        self.win_frame.pack(fill='x', pady=(0,1))

        self.exit_button = ButtonClass(master = self.win_frame,
                                       command = lambda: self.destroy(), text="X")
        self.exit_button.pack(side='right')

        self.new_notepad = ButtonClass(master = self.win_frame, text="➕")
        self.new_notepad.pack(side='left')

        self.maximize_button = ButtonClass(master = self.win_frame,
                                            text= "🗖",
                                            command = lambda : maximize(self, self.maximize_button))
        self.maximize_button.pack(side='right')


        self.minimize_button = ButtonClass(master = self.win_frame,
                                           text= "_",
                                           anchor='n',
                                           command = lambda : minimize(self))
        self.minimize_button.pack(side='right')

        self.settings_button = ButtonClass( master = self.win_frame,
                                    text="⚙")
        self.settings_button.pack(side="left")

        buttons.extend([self.exit_button,self.maximize_button, self.minimize_button, self.new_notepad, self.settings_button])
        self.bind_buttons(buttons)

    

    def bind_buttons(self, buttons):
        for button in buttons:
            button.bind("<Enter>", ButtonClass.on_hover)
            button.bind("<Leave>", ButtonClass.on_default)

    
    def taskbar_window(self):
        '''
        Sets the taskbar according to windows settings
        '''
        #Most of this is just Windows default logic for the taskbar
        try:
            


            GWL_EXSTYLE = -20
            WS_EX_APPWINDOW = 0x00040000
            WS_EX_TOOLWINDOW = 0x00000080

            hwnd = windll.user32.GetParent(self.winfo_id())
            stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            stylew = stylew & ~WS_EX_TOOLWINDOW
            stylew = stylew | WS_EX_APPWINDOW
            res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)


            #final logic that places the iconbar
            self.wm_withdraw()
            self.after(20, lambda: self.wm_deiconify())



        except StopIteration:
            pass








if __name__ == "__main__":
    tk = TkinterWindow()

    tk.mainloop()