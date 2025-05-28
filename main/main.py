from secondary_windows import NoteWindow
from commands import check_window_status

from tkinter_main import TkinterWindow



if __name__ == "__main__":
    tk = NoteWindow()

    def do_thing():
        check_window_status(TkinterWindow.windows)
        try:
            tk.after(20, do_thing)
        except Exception as e:
            print(e)

    do_thing()

    tk.mainloop()