from tkinter_main import TkinterWindow

class NoteWindow(TkinterWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_settings()

    def load_settings(self, *args, **kwargs):
        self.title('Notes'+ str(TkinterWindow.num))
        return super().load_settings()

class SaveWindow(TkinterWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def load_settings(self, *args, **kwargs):
        self.title('save'+ str(TkinterWindow.num))
        return super().load_settings()

if __name__ == "__main__":
    pass