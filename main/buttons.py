import tkinter

class ButtonClass(tkinter.Button):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.config()

    def config(self):
        base_look = {
            "takefocus": 1,
            "font": ("Arial", 26, "bold"),
            "fg":"#1E38FF"
            }
        super().config(base_look)