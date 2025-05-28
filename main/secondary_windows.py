from tkinter_main import TkinterWindow
from PIL import Image
from tkinter import PhotoImage

from random import randrange

class NoteWindow(TkinterWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_settings()
        self.bind_new_notepad()

        self.wm_iconbitmap("notepad.ico", default="notepad.ico")


    def load_settings(self, *args, **kwargs):
        self.title('Notes'+ str(TkinterWindow.num))
        return super().load_settings()
    
    @staticmethod
    def create_new_notepad(window, event = None):
        new = NoteWindow()
        #Can fix this logic a little, but works as intended for now
        location = (window.winfo_width(), window.winfo_height())
        x, y = window.winfo_x()+location[0]+4, window.winfo_y()

        new.geometry(f"{location[0]}x{location[1]}+{x}+{y}")


    def bind_new_notepad(self):
        self.new_notepad.configure(command = lambda: NoteWindow.create_new_notepad(self))


class SaveWindow(TkinterWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def load_settings(self, *args, **kwargs):
        self.title('save'+ str(TkinterWindow.num))
        return super().load_settings()

if __name__ == "__main__":
    pass