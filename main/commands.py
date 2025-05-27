import win32gui, win32con
'''
Command Library
'''

def maximize(master, button) -> None:
    '''
    Custom maximize function

    Args:
        master(tkinter.tk): root tkinter window
        button(tk.Button): button to override
    '''
    #Was using the inbuilt tkinter geometry commands, but they aren't as good as win32, and less reliable
    window = win32gui.GetForegroundWindow()

    if not master.maximized:
        win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
        #boolean switch
        master.maximized = True

    else:
        #Back to default/before maximized
        master.maximized = False
        win32gui.ShowWindow(window, win32con.SW_NORMAL)

def minimize(master) -> None:
    '''
    Custom minimize function

    Args:
        master(tkinter.tk): root tkinter window
    '''
    Window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Window, win32con.SW_MINIMIZE)



def check_window_status(master_list) -> None:

    '''
    Checks window position

    Args:
        master(tkinter.Tk): Tkinter window
    '''
    #Only changes if state has changed
    for master in master_list:
        #master_list is all my current note windows. Checks all states
        if master.current_state == master.wm_state():
            pass
        else:
            #Finds the window using win32
            Window = win32gui.FindWindow(None, master.wm_title())
            if Window:
                #GetWindowPlacement returns a tuple
                is_maximized = win32gui.GetWindowPlacement(Window)
                #Idx 1 determines if it's maximized or not, and returns logic
                if is_maximized[1] == win32con.SW_SHOWMAXIMIZED:
                    master.maximized = True
                    #Changes to the windows icon (to look better yknow)
                    master.maximize_button.configure(text="🗗")
                else:
                    master.maximized = False
                    master.maximize_button.configure(text="🗖")
                master.current_state = master.wm_state()
