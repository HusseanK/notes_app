from secondary_windows import NoteWindow
from commands import check_window_status

def create_new_notepad(event = None):
    tk = NoteWindow()
    note_list.append(tk)

def bind_buttons(tk):
    tk.new_notepad.configure(command = lambda: create_new_notepad())



note_list = []

if __name__ == "__main__":
    tk = NoteWindow()
    note_list.append(tk)
    bind_buttons(tk)

    

    def do_thing():
        check_window_status(note_list)
        tk.after(20, do_thing)

    do_thing()

    tk.mainloop()