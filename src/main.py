from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("TkInter")
    gui = UI(window)
    gui.start()
    window.mainloop()

if __name__ == "__main__":
    main()
