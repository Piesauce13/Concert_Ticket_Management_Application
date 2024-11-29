from tkinter import Canvas, Tk


def create_canvas(window):
    canvas = Canvas(
        window,
        bg="#6E2D85",
        height=768,
        width=1024,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    return canvas


def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def create_window():
    window = Tk()
    window.geometry("1024x768")
    window.configure(bg="#6E2D85")
    return window


def navigate(window, destination):
    clear_window(window)
    canvas = create_canvas(window)
    destination(window, canvas)

def overlay(window, destination):
    destination(window)