from Pages import startpage
from Navigation import create_canvas, create_window



def main():
    window = create_window()
    canvas = create_canvas(window)
    window.resizable(False, False)
    window.title("Concert Ticket Management")
    startpage(window, canvas)


main()