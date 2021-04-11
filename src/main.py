from tkinter import Tk
from ui.ui import UI
from services.main_service import MainService


def main():
    window = Tk()
    window.title("Arithmetician")
    gui = UI(window, MainService())
    gui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
