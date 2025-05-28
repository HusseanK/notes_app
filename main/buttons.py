import tkinter

class ButtonClass(tkinter.Button):        
    dark_background = "#323232"
    button_background = "#414141"
    text_colour = "#A2A2A2"

    def __init__(self, *args, **kwargs):
        base_look = {
            "takefocus": 1,
            "font": ("Segoe MDL2 Assets 16", 8, "normal"),
            "bg": "#414141",
            'fg':"#A2A2A2",
            'activebackground':"#4D4D4D",
            'activeforeground':"#BABABA",
            "justify":"center",
            'relief':'flat',
            'padx':'5',
            'pady':'5'
            }
        base_look.update(kwargs)

        super().__init__(*args, **base_look)
        self.config()


    @staticmethod
    def on_default(event):
        event.widget.configure(bg="#414141", fg="#A2A2A2")
    @staticmethod
    def on_hover(event):
        event.widget.configure(bg="#888888", fg="#B7B7B7")
