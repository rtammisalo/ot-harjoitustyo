from tkinter import Tk
from ui.ui import UI
from services.main_service import MainService
from database import Database
from repositories.user_repository import UserRepository

def main():
    window = Tk()
    window.title("Arithmetician")
    database = Database()
    gui = UI(window, MainService(UserRepository(database)))
    gui.start()
    window.geometry("350x350")
    window.mainloop()


if __name__ == "__main__":
    main()
