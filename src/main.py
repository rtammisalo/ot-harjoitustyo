from tkinter import Tk
from ui.ui import UI
from services.main_service import MainService
from database import Database
from repositories.user_repository import UserRepository
from config import Config


def main():
    """Call this to start the program.
    """
    window = Tk()
    window.title("Arithmetician")
    database = Database()

    if not database.is_db_connection_ok():
        print(
            f"Failed to connect to database: {Config.DB_FILENAME}. Exiting..")
        return

    gui = UI(window, MainService(UserRepository(database)))
    gui.start()
    window.geometry("350x500")
    window.mainloop()


if __name__ == "__main__":
    main()
