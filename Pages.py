from pathlib import Path
from Navigation import navigate
import pymysql.cursors
from Credentials import get_creds, get_admin_pw, get_staff_pw
import re
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import os
import shutil
from PIL import Image, ImageTk

def startpage(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame_start")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas.place(x=0, y=0)
    canvas.create_text(
        21.0,
        57.0,
        anchor="nw",
        text="Dontrey Concert",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    canvas.create_text(
        17.0,
        132.0,
        anchor="nw",
        text="Ticket Management",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    canvas.create_text(
        21.0,
        201.0,
        anchor="nw",
        text="Service",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    canvas.create_text(
        21.0,
        317.0,
        anchor="nw",
        text="Your go-to application for a quick and",
        fill="#FFFFFF",
        font=("Poppins Regular", 24 * -1)
    )

    canvas.create_text(
        21.0,
        353.0,
        anchor="nw",
        text="user-friendly concert management",
        fill="#FFFFFF",
        font=("Poppins Regular", 24 * -1)
    )

    canvas.create_text(
        23.0,
        390.0,
        anchor="nw",
        text="system for small concert venues",
        fill="#FFFFFF",
        font=("Poppins Regular", 24 * -1)
    )

    canvas.create_rectangle(
        550.0,
        0.0,
        1024.0,
        768.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        534.0,
        0.0,
        550.0,
        768.0,
        fill="#D9D9D9",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        787.0,
        384.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        17.0,
        287.0,
        512.0,
        291.0,
        fill="#D9D9D9",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_login.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, loginpage),
        relief="flat"
    )
    button_1.place(
        x=154.0,
        y=473.0,
        width=193.064453125,
        height=81.29032135009766
    )
    window.mainloop()

def loginpage(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame_login")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def login_button_click():
        username = entry_1.get()
        password = entry_2.get()

        # Check if the first entry is neither "staff" nor "admin"
        if username not in ("staff", "admin"):
            messagebox.showerror("Alert", "Please enter 'staff' or 'admin'")
            return

        # Check if the password field is empty
        if not password:
            messagebox.showerror("Alert", "Please enter a password")
            return

        # Check for incorrect passwords
        if username == "staff" and password != "password":
            messagebox.showerror("Alert", "Wrong password for staff")
            return
        elif username == "admin" and password != "admin":
            messagebox.showerror("Alert", "Wrong password for admin")
            return

        # Successful login cases
        if username == "staff" and password == get_staff_pw():
            messagebox.showinfo("Success", "Login Successful as staff")
            navigate(window, homepage)
        elif username == "admin" and password == get_admin_pw():
            messagebox.showinfo("Success", "Login Successful as admin")
            navigate(window, adminpage)


    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        126.0,
        235.0,
        891.0,
        633.0,
        fill="#270683",
        outline="")

    canvas.create_text(
        34.0,
        30.0,
        anchor="nw",
        text="Staff Login",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    canvas.create_rectangle(
        29.0,
        118.0,
        980.0,
        122.0,
        fill="#D9D9D9",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        507.5,
        323.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Poppins Regular", 37 * -1),
    )
    entry_1.place(
        x=180.0,
        y=295.0,
        width=655.0,
        height=54.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        507.5,
        450.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Poppins Regular", 37 * -1),
        show="*"
    )
    entry_2.place(
        x=180.0,
        y=423.0,
        width=655.0,
        height=52.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: login_button_click(),
        relief="flat"
    )
    button_1.place(
        x=159.0,
        y=521.0,
        width=124.0,
        height=63.0
    )

    canvas.create_text(
        165.0,
        249.0,
        anchor="nw",
        text="Admin or Staff",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )

    canvas.create_text(
        157.0,
        376.0,
        anchor="nw",
        text="Password",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )

    window.mainloop()

def adminpage (window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame_add")
    IMAGE_SAVE_PATH = OUTPUT_PATH / Path(r"assets\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def upload_poster(concert_index):
        TARGET_WIDTH = 306
        TARGET_HEIGHT = 379

        # Upload an image, resize and crop it to fit specified dimensions,and save it as image_1.png, image_2.png, or image_3.png.

        filename = filedialog.askopenfilename(
            title="Select Poster",
            filetypes=(("Image Files", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*"))
        )
        if filename:
            try:
                # Open the image
                img = Image.open(filename)

                # Calculate the aspect ratio of the image
                img_aspect_ratio = img.width / img.height
                target_aspect_ratio = TARGET_WIDTH / TARGET_HEIGHT

                # Resize and crop the image to maintain the aspect ratio
                if img_aspect_ratio > target_aspect_ratio:
                    # Image is wider than target aspect ratio
                    new_height = TARGET_HEIGHT
                    new_width = int(TARGET_HEIGHT * img_aspect_ratio)
                    img = img.resize((new_width, new_height), Image.LANCZOS)
                    left = (new_width - TARGET_WIDTH) // 2
                    img = img.crop((left, 0, left + TARGET_WIDTH, TARGET_HEIGHT))
                else:
                    # Image is taller or equal to target aspect ratio
                    new_width = TARGET_WIDTH
                    new_height = int(TARGET_WIDTH / img_aspect_ratio)
                    img = img.resize((new_width, new_height), Image.LANCZOS)
                    top = (new_height - TARGET_HEIGHT) // 2
                    img = img.crop((0, top, TARGET_WIDTH, top + TARGET_HEIGHT))

                # Save the resized and cropped image
                destination_file = IMAGE_SAVE_PATH / f"image_{concert_index}.png"
                img.save(destination_file, format="PNG")

                messagebox.showinfo("Success", f"Poster for concert {concert_index} uploaded successfully.")
            except Exception as e:
                print("UPLOAD ERROR:", e)
                messagebox.showerror("Error", "Failed to upload the image.")

    def add_button_clicked():
        date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        # Check if entries are empty
        if not entry_1.get().strip() or not entry_2.get().strip():
            messagebox.showerror("Error", "All fields must be filled.")
        # Validate date format for entry_2
        elif not re.match(date_pattern, entry_2.get().strip()):
            messagebox.showerror("Error", "Concert Date must be in YYYY-MM-DD format.")
        else:
            # Assign final values if no errors occurred
            concert_name = entry_1.get()
            concert_date = entry_2.get()

            conn = None
            try:
                conn = pymysql.connect(host="127.0.0.1", user="root", password=get_creds(), db="csa", )

            except Exception as ex:
                print("PROBLEM WITH Database Connection", ex)

            else:
                print("Database Connection SUCCESS")

            if conn is not None:
                cursor = conn.cursor()

                try:
                    # Check the total number of distinct concert names
                    query_check_names = "SELECT COUNT(DISTINCT Concert) FROM Concerts;"
                    cursor.execute(query_check_names)
                    distinct_names_count = cursor.fetchone()[0]

                    # Check the number of distinct dates for the specified concert name
                    query_check_dates_per_concert = "SELECT COUNT(DISTINCT ConcertDate) FROM Concerts WHERE Concert = %s;"
                    cursor.execute(query_check_dates_per_concert, (concert_name,))
                    distinct_dates_count_for_concert = cursor.fetchone()[0]

                    cursor.execute("SELECT DISTINCT Concert FROM Concerts;")
                    distinct_concerts = [row[0] for row in cursor.fetchall()]
                    print(distinct_concerts)

                    # Validate capacity
                    if distinct_names_count >= 3 and concert_name not in distinct_concerts:
                        messagebox.showerror("Capacity Reached",
                                             "You can no longer add more concert names. Capacity reached.")
                        return

                    if distinct_dates_count_for_concert >= 3:
                        messagebox.showerror("Capacity Reached",
                                             f"The concert '{concert_name}' already has 3 distinct dates. Cannot add more dates.")
                        return

                    # Insert the new concert or date
                    query_insert = """
                                   INSERT INTO Concerts (Concert, ConcertDate, ConcertSection, SectionAvailableSeats, Price)
                                   VALUES 
                                   (%s, %s, 'Section A', 5, 50),
                                   (%s, %s, 'Section B', 15, 75),
                                   (%s, %s, 'Section C', 5, 50),
                                   (%s, %s, 'Section D', 10, 25);
                               """
                    noofrecoredinsert = cursor.execute(
                        query_insert,
                        (concert_name, concert_date, concert_name, concert_date, concert_name, concert_date,
                         concert_name, concert_date)
                    )
                    conn.commit()

                except Exception as e:
                    print("INSERT PROBLEM", e)
                    messagebox.showerror("Error", "Failed to insert the concert. Please check the inputs.")
                else:
                    if noofrecoredinsert > 0:
                        print("RECORD INSERTED")
                        messagebox.showinfo("Success",
                                            f"Concert '{concert_name}' on {concert_date} inserted successfully.")
                finally:
                    conn.close()

    def remove_button_clicked():
        date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        # Check if entries are empty
        if not entry_1.get().strip() or not entry_2.get().strip():
            messagebox.showerror("Error", "All fields must be filled.")
        # Validate date format for entry_2
        elif not re.match(date_pattern, entry_2.get().strip()):
            messagebox.showerror("Error", "Concert Date must be in YYYY-MM-DD format.")
        else:
            # Assign final values if no errors occurred
            concert_name = entry_1.get()
            concert_date = entry_2.get()

            conn = None
            try:
                conn = pymysql.connect(host="127.0.0.1", user="root", password=get_creds(), db="csa", )

            except Exception as ex:
                print("PROBLEM WITH Database Connection", ex)

            else:
                print("Database Connection SUCCESS")

            if conn is not None:
                cursor = conn.cursor()

                try:
                    query_remove = """DELETE FROM Concerts WHERE Concert = (%s) AND ConcertDate = (%s);"""
                    noofrecoredremoved = cursor.execute(query_remove, (concert_name, concert_date))
                    conn.commit()

                    if noofrecoredremoved == 0:
                        print("No matching record found.")
                        messagebox.showerror("Error", "Concert does not exist or date mismatch.")
                    else:
                        print("RECORD REMOVED")
                        messagebox.showinfo("Success",
                                            f"Concert '{concert_name}' on {concert_date} removed successfully.")

                except Exception as e:
                    print("REMOVAL PROBLEM", e)
                    messagebox.showerror("Error", "Please Input Correct Date Format")
                finally:
                    conn.close()

    canvas.place(x=0, y=0)

    canvas.create_text(
        251.0,
        563.0,
        anchor="nw",
        text="Upload Concert Poster Image File",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_concert3.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: upload_poster(3),
        relief="flat"
    )
    button_4.place(
        x=693.0,
        y=644.0,
        width=151.0,
        height=63.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_concert2.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: upload_poster(2),
        relief="flat"
    )
    button_5.place(
        x=429.0,
        y=643.0,
        width=151.0,
        height=63.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_concert1.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: upload_poster(1),
        relief="flat"
    )
    button_6.place(
        x=165.0,
        y=643.0,
        width=151.0,
        height=63.0
    )

    canvas.create_rectangle(
        37.0,
        168.0,
        988.0,
        512.0,
        fill="#270683",
        outline="")

    canvas.create_text(
        111.0,
        30.0,
        anchor="nw",
        text="Add or Remove Concert",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    canvas.create_rectangle(
        29.0,
        118.0,
        980.0,
        122.0,
        fill="#D9D9D9",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        518.0,
        252.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins Regular", 37 * -1)
    )
    entry_1.place(
        x=98.0,
        y=224.0,
        width=840.0,
        height=54.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        518.0,
        379.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins Regular", 37 * -1)
    )
    entry_2.place(
        x=98.0,
        y=352.0,
        width=840.0,
        height=52.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_button_clicked(),
        relief="flat"
    )
    button_1.place(
        x=75.0,
        y=440.0,
        width=91.0,
        height=53.0
    )

    canvas.create_text(
        83.0,
        178.0,
        anchor="nw",
        text="Concert Name",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )

    canvas.create_text(
        75.0,
        305.0,
        anchor="nw",
        text="Concert Date",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, loginpage),
        relief="flat"
    )
    button_2.place(
        x=12.0,
        y=30.0,
        width=99.0,
        height=67.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_remove.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: remove_button_clicked(),
        relief="flat"
    )
    button_3.place(
        x=195.0,
        y=440.0,
        width=126.0,
        height=53.0
    )
    window.mainloop()

def homepage(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    concert1 = concert2 = concert3 = None
    conn = None
    try:
        conn = pymysql.connect(host="127.0.0.1", user="root", password=get_creds(), db="csa", )

    except Exception as ex:
        print("PROBLEM WITH Database Connection", ex)
    else:
        print("Database Connection SUCCESS")

    if conn is not None:
        try:
            # Query to select 3 unique concert names
            query = "SELECT DISTINCT Concert FROM Concerts LIMIT 3;"
            cursor = conn.cursor()
            cursor.execute(query)
            # Fetch results
            results = cursor.fetchall()  # This will be a tuple of tuples like (('Concert A',), ('Concert B',), ...)
            # Ensure at least 3 elements, using None if fewer
            temp_results = list(results) + [(None,)] * (3 - len(results))
            concert1, concert2, concert3 = temp_results[0][0], temp_results[1][0], temp_results[2][0]
        except Exception as e:
            print("PROBLEM WITH QUERY EXECUTION", e)
            results = []
        finally:
            conn.commit()

    def buy_button_click(concert):
        conn = None
        try:
            conn = pymysql.connect(host="127.0.0.1",user="root",password=get_creds(),db="csa", )

        except Exception as ex:
            print("PROBLEM WITH Database Connection", ex)
        else:
            print("Database Connection SUCCESS")

        if conn is not None:

            query = "insert into Customers(Concert) values(%s);"

            try:
                cursor = conn.cursor()
                noofrecoredinsert = cursor.execute(query,concert)
                conn.commit()
            except Exception as e:
                print("INSERT PROBLEM ", e)
            else:
                if noofrecoredinsert > 0:
                    print("RECORD INSERTED ")
                    messagebox.showinfo("Success", f"{concert} Selected")
                    navigate(window, datepage)

    canvas.place(x = 0, y = 0)

    try:
        try:
            image_1 = ImageTk.PhotoImage(Image.open(relative_to_assets("image_1.png")))
            canvas.create_image(180.0, 423.0, image=image_1)
        except Exception as e:
            print("ERROR LOADING IMAGE 1:", e)
            # Optionally, use a placeholder for missing images
            placeholder_1 = ImageTk.PhotoImage(Image.new("RGB", (306, 379), color="gray"))
            canvas.create_image(180.0, 423.0, image=placeholder_1)
            image_1 = placeholder_1

        try:
            image_2 = ImageTk.PhotoImage(Image.open(relative_to_assets("image_2.png")))
            canvas.create_image(512.0, 423.0, image=image_2)
        except Exception as e:
            print("ERROR LOADING IMAGE 2:", e)
            # Placeholder for missing images
            placeholder_2 = ImageTk.PhotoImage(Image.new("RGB", (306, 379), color="gray"))
            canvas.create_image(512.0, 423.0, image=placeholder_2)
            image_2 = placeholder_2

        try:
            image_3 = ImageTk.PhotoImage(Image.open(relative_to_assets("image_3.png")))
            canvas.create_image(844.0, 423.0, image=image_3)
        except Exception as e:
            print("ERROR LOADING IMAGE 3:", e)
            # Placeholder for missing images
            placeholder_3 = ImageTk.PhotoImage(Image.new("RGB", (306, 379), color="gray"))
            canvas.create_image(844.0, 423.0, image=placeholder_3)
            image_3 = placeholder_3

        # Keep references to prevent garbage collection
        window.poster_images = [image_1, image_2, image_3]

    except Exception as e:
        print("GENERAL ERROR LOADING IMAGES:", e)
        messagebox.showerror("Error", "An unexpected error occurred while loading images.")

    canvas.place(x=0, y=0)
    canvas.create_text(
        111.0,
        36.0,
        anchor="nw",
        text="Welcome to Dontrey Concert Hall",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    canvas.create_text(
        27.0,
        132.0,
        anchor="nw",
        text="Current Concerts",
        fill="#FFFFFF",
        font=("Poppins Bold", 36 * -1)
    )

    canvas.create_text(
        49.0,
        618.0,
        anchor="nw",
        text=concert1,
        fill="#FFFFFF",
        font=("Poppins Regular", 24 * -1)
    )

    canvas.create_text(
        428.0,
        618.0,
        anchor="nw",
        text=concert2,
        fill="#FFFFFF",
        font=("Poppins Regular", 24 * -1)
    )

    canvas.create_text(
        728.0,
        620.0,
        anchor="nw",
        text=concert3,
        fill="#FFFFFF",
        font=("Poppins Regular", 24 * -1)
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, loginpage),
        relief="flat"
    )
    button_6.place(
        x=12.0,
        y=36.0,
        width=99.0,
        height=67.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, ticketsearch),
        relief="flat"
    )
    button_4.place(
        x=683.0,
        y=136.0,
        width=295.0,
        height=44.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, member_registration),
        relief="flat"
    )
    button_5.place(
        x=428.0,
        y=136.0,
        width=242.0,
        height=44.0
    )

    canvas.create_rectangle(
        27.0,
        120.0,
        978.0,
        124.0,
        fill="#D9D9D9",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: buy_button_click(concert1),
        relief="flat"
    )

    button_1.place(
        x=101.0,
        y=670.0,
        width=158.0,
        height=80.2741928100586
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: buy_button_click(concert3),
        relief="flat"
    )
    button_2.place(
        x=769.0,
        y=670.0,
        width=158.0,
        height=80.2741928100586
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: buy_button_click(concert2),
        relief="flat"
    )
    button_3.place(
        x=428.0,
        y=670.0,
        width=158.0,
        height=80.2741928100586
    )

    window.mainloop()

def datepage(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame_date")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    conn = None
    try:
        conn = pymysql.connect(host="127.0.0.1", user="root", password=get_creds(), db="csa", )
    except Exception as ex:
        print("PROBLEM WITH Database Connection", ex)
        return
    else:
        print("Database Connection SUCCESS")

    if conn is not None:
        cursor = conn.cursor()

        # Fetch the most recent concert from the Customers table
        query_recent_concert = "SELECT Concert FROM Customers ORDER BY CustomerID DESC LIMIT 1;"
        cursor.execute(query_recent_concert)
        result_recent_concert = cursor.fetchone()
        if result_recent_concert:
            recent_concert = result_recent_concert[0]
            print(f"Most Recent Concert: {recent_concert}")
        else:
            print("No recent concert found.")
            return

        # Fetch up to 3 distinct ConcertDates for the recent concert
        query_concert_dates = """
                    SELECT DISTINCT ConcertDate 
                    FROM Concerts 
                    WHERE Concert = %s 
                    LIMIT 3;
                """
        cursor.execute(query_concert_dates, (recent_concert,))
        result_concert_dates = cursor.fetchall()

        # Pad the results to ensure 3 variables
        temp_dates = list(result_concert_dates) + [(None,)] * (3 - len(result_concert_dates))
        date1, date2, date3 = temp_dates[0][0], temp_dates[1][0], temp_dates[2][0]

        print(f"Concert Dates: {date1}, {date2}, {date3}")


    def date_button_click(date):
        # Check if the date is None
        if date is None:
            # Display a message box to inform the user
            messagebox.showwarning(
                "Date Not Available",
                "Date not available. Please select an available date."
            )
            return

        conn = None
        try:
            conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password=get_creds(),
                db="csa",
            )

        except Exception as ex:
            print("PROBLEM WITH Database Connection", ex)
        else:
            print("Database Connection SUCCESS")

        if conn is not None:
            query_find_incomplete = """
                    SELECT CustomerID
                    FROM Customers
                    WHERE CustomerName IS NULL
                       OR PhoneNumber IS NULL
                       OR Concert IS NULL
                       OR ConcertDate IS NULL
                       OR Section IS NULL
                    ORDER BY CustomerID DESC
                    LIMIT 1;
                """
            cursor = conn.cursor()
            cursor.execute(query_find_incomplete)
            result = cursor.fetchone()

            if result:
                # Incomplete row found, update it
                customer_id = result[0]
                query_update = """
                        UPDATE Customers
                        SET 
                            ConcertDate = COALESCE(ConcertDate, %s)

                        WHERE CustomerID = %s;
                    """
                try:
                    noofrecoredinsert = cursor.execute(query_update, (date, customer_id))
                    conn.commit()

                except Exception as e:
                    print("INSERT PROBLEM ", e)
                else:
                    if noofrecoredinsert > 0:
                        print("RECORD INSERTED ")
                        messagebox.showinfo("Success", f"{date} Selected")
                        navigate(window, seatpage)

    def home_button_click():

        conn = None
        try:
            conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password=get_creds(),
                db="csa",
            )

        except Exception as ex:
            print("PROBLEM WITH Database Connection", ex)
        else:
            print("Database Connection SUCCESS")

        # STEP 3 - CHECK Connection is Establish or not
        if conn is not None:
            query_find_incomplete = """
                    SELECT CustomerID
                    FROM Customers
                    WHERE CustomerName IS NULL
                       OR PhoneNumber IS NULL
                       OR Concert IS NULL
                       OR ConcertDate IS NULL
                       OR Section IS NULL
                    ORDER BY CustomerID DESC
                    LIMIT 1;
                """
            cursor = conn.cursor()
            cursor.execute(query_find_incomplete)
            result = cursor.fetchone()

            if result:
                # Incomplete row found, update it
                customer_id = result[0]
                query_update = """
                        DELETE FROM Customers
                        WHERE CustomerID = %s;
                    """
                try:
                    noofrecoredinsert = cursor.execute(query_update, (customer_id))
                    conn.commit()

                except Exception as e:
                    print("DELETE PROBLEM ", e)
                else:
                    if noofrecoredinsert > 0:
                        print("RECORD DELETED ")
                        messagebox.showinfo("Warning", "Restart Purchase")
                        navigate(window, homepage)

    canvas.place(x=0, y=0)
    canvas.create_text(
        89.0,
        31.0,
        anchor="nw",
        text="Select Date",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: home_button_click(),
        relief="flat"
    )
    button_1.place(
        x=30.0,
        y=39.0,
        width=45.0,
        height=46.0
    )

    canvas.create_rectangle(
        29.0,
        118.0,
        980.0,
        122.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        93.0,
        176.0,
        931.0,
        317.0,
        fill="#230672",
        outline="")

    canvas.create_text(
        467.0,
        210.0,
        anchor="nw",
        text=date1,
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    canvas.create_text(
        807.0,
        216.0,
        anchor="nw",
        text="6 pm",
        fill="#FFFFFF",
        font=("Poppins Bold", 36 * -1)
    )

    canvas.create_text(
        306.0,
        219.0,
        anchor="nw",
        text="Day 1",
        fill="#FFFFFF",
        font=("Poppins Bold", 36 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: date_button_click(date1),
        relief="flat"
    )
    button_2.place(
        x=120.0,
        y=216.0,
        width=124.0,
        height=63.0
    )

    canvas.create_rectangle(
        272.0,
        189.0,
        277.0,
        303.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        93.0,
        357.0,
        931.0,
        498.0,
        fill="#230672",
        outline="")

    canvas.create_text(
        467.0,
        391.0,
        anchor="nw",
        text=date2,
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    canvas.create_text(
        807.0,
        397.0,
        anchor="nw",
        text="6 pm",
        fill="#FFFFFF",
        font=("Poppins Bold", 36 * -1)
    )

    canvas.create_text(
        306.0,
        400.0,
        anchor="nw",
        text="Day 2",
        fill="#FFFFFF",
        font=("Poppins Bold", 36 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: date_button_click(date2),
        relief="flat"
    )
    button_3.place(
        x=120.0,
        y=397.0,
        width=124.0,
        height=63.0
    )

    canvas.create_rectangle(
        272.0,
        370.0,
        277.0,
        484.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        93.0,
        528.0,
        931.0,
        669.0,
        fill="#230672",
        outline="")

    canvas.create_text(
        467.0,
        562.0,
        anchor="nw",
        text=date3,
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    canvas.create_text(
        807.0,
        568.0,
        anchor="nw",
        text="6 pm",
        fill="#FFFFFF",
        font=("Poppins Bold", 36 * -1)
    )

    canvas.create_text(
        306.0,
        571.0,
        anchor="nw",
        text="Day 3",
        fill="#FFFFFF",
        font=("Poppins Bold", 36 * -1)
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: date_button_click(date3),
        relief="flat"
    )
    button_4.place(
        x=120.0,
        y=568.0,
        width=124.0,
        height=63.0
    )

    canvas.create_rectangle(
        272.0,
        541.0,
        277.0,
        655.0,
        fill="#D9D9D9",
        outline="")

    window.mainloop()

def seatpage(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame5")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def get_available_seats(section):
        conn = None
        try:
            conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password=get_creds(),
                db="csa",
            )

        except Exception as ex:
            print("PROBLEM WITH Database Connection", ex)
        else:
            print("Database Connection SUCCESS")

        if conn is not None:
            cursor = conn.cursor()
            # Get the most recent CustomerID (last inserted row)
            cursor.execute("SELECT CustomerID, Concert, ConcertDate FROM Customers ORDER BY CustomerID DESC LIMIT 1")
            result = cursor.fetchone()
            if result:
                customer_id, concert, concert_date = result

                # Check availability in concerts table
                cursor.execute("""
                                    SELECT SectionAvailableSeats 
                                    FROM concerts 
                                    WHERE Concert = %s AND ConcertDate = %s AND ConcertSection = %s
                                """, (concert, concert_date, section))
                section_result = cursor.fetchone()
                available_seats = section_result[0]
                return available_seats

    def seat_button_click(selected_section):

        conn = None
        try:
            conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password=get_creds(),
                db="csa",
            )

        except Exception as ex:
            print("PROBLEM WITH Database Connection", ex)
        else:
            print("Database Connection SUCCESS")

        if conn is not None:
            cursor = conn.cursor()
            # Get the most recent CustomerID (last inserted row)
            cursor.execute("SELECT CustomerID, Concert, ConcertDate FROM Customers ORDER BY CustomerID DESC LIMIT 1")
            result = cursor.fetchone()
            if result:
                customer_id, concert, concert_date = result

                # Check availability in concerts table
                cursor.execute("""
                            SELECT SectionAvailableSeats 
                            FROM concerts 
                            WHERE Concert = %s AND ConcertDate = %s AND ConcertSection = %s
                        """, (concert, concert_date, selected_section))
                section_result = cursor.fetchone()


                if section_result:
                    available_seats = section_result[0]

                    if available_seats > 0:
                        # Update the concerts table to reduce the seat count by 1
                        cursor.execute("""
                                    UPDATE concerts 
                                    SET SectionAvailableSeats = SectionAvailableSeats - 1
                                    WHERE Concert = %s AND ConcertDate = %s AND ConcertSection = %s
                                """, (concert, concert_date, selected_section))

                        query_find_incomplete = """
                                            SELECT CustomerID
                                            FROM Customers
                                            WHERE CustomerName IS NULL
                                               OR PhoneNumber IS NULL
                                               OR Concert IS NULL
                                               OR ConcertDate IS NULL
                                               OR Section IS NULL
                                            ORDER BY CustomerID DESC
                                            LIMIT 1;
                                        """

                        cursor.execute(query_find_incomplete)
                        result = cursor.fetchone()

                        if result:
                            # Incomplete row found, update it
                            customer_id = result[0]
                            query_update = """
                                                UPDATE Customers
                                                SET 
                                                    Section = COALESCE(Section, %s)

                                                WHERE CustomerID = %s;
                                            """
                            try:
                                noofrecoredinsert = cursor.execute(query_update, (selected_section, customer_id))
                                conn.commit()

                            except Exception as e:
                                print("INSERT PROBLEM ", e)
                            else:
                                if noofrecoredinsert > 0:
                                    print("RECORD INSERTED ")
                                    messagebox.showinfo("Success", f"{selected_section} Selected")
                                    navigate(window, customerpage)

                    else:
                        # Notify the user if the section is full
                        messagebox.showwarning("Section Full",
                                               f"{selected_section} is fully booked. Please select another section.")
                else:
                    messagebox.showerror("Error", "Section details not found in the database.")

    def home_button_click():
        conn = None
        try:
            conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password=get_creds(),
                db="csa",
            )
        except Exception as ex:
            print("PROBLEM WITH Database Connection", ex)
        else:
            print("Database Connection SUCCESS")

        if conn is not None:
            query_find_incomplete = """
                    SELECT CustomerID
                    FROM Customers
                    WHERE CustomerName IS NULL
                       OR PhoneNumber IS NULL
                       OR Concert IS NULL
                       OR ConcertDate IS NULL
                       OR Section IS NULL
                    ORDER BY CustomerID DESC
                    LIMIT 1;
                """
            cursor = conn.cursor()
            cursor.execute(query_find_incomplete)
            result = cursor.fetchone()

            if result:
                # Incomplete row found, update it
                customer_id = result[0]
                query_update = """
                        DELETE FROM Customers
                        WHERE CustomerID = %s;
                    """
                try:
                    noofrecoredinsert = cursor.execute(query_update, (customer_id))
                    conn.commit()

                except Exception as e:
                    print("DELETE PROBLEM ", e)
                else:
                    if noofrecoredinsert > 0:
                        print("RECORD DELETED ")
                        messagebox.showinfo("Warning", "Restart Purchase")
                        navigate(window, homepage)

    canvas.place(x=0, y=0)
    canvas.create_text(
        92.0,
        24.0,
        anchor="nw",
        text="Select Seat Section",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: seat_button_click('Section A'),
        relief="flat"
    )
    button_1.place(
        x=52.0,
        y=348.0,
        width=204.0,
        height=231.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: seat_button_click('Section B'),
        relief="flat"
    )
    button_2.place(
        x=283.0,
        y=294.0,
        width=457.0,
        height=285.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: seat_button_click('Section D'),
        relief="flat"
    )
    button_3.place(
        x=154.0,
        y=601.0,
        width=728.00439453125,
        height=102.15280151367188
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: seat_button_click('Section C'),
        relief="flat"
    )
    button_4.place(
        x=767.0,
        y=350.0,
        width=204.0,
        height=231.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: home_button_click(),
        relief="flat"
    )
    button_5.place(
        x=30.0,
        y=38.0,
        width=45.0,
        height=46.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        511.0,
        236.0,
        image=image_image_1
    )
    canvas.create_text(
        440.0,
        710.0,
        anchor="nw",
        text=f"Available Seats : {get_available_seats("Section D")}",
        fill="#FFFFFF",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        794.0,
        318.0,
        anchor="nw",
        text=f"Available Seats : {get_available_seats("Section C")}",
        fill="#FFFFFF",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        78.0,
        311.0,
        anchor="nw",
        text=f"Available Seats : {get_available_seats("Section A")}",
        fill="#FFFFFF",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        442.0,
        262.0,
        anchor="nw",
        text=f"Available Seats : {get_available_seats("Section B")}",
        fill="#FFFFFF",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        473.0,
        144.0,
        anchor="nw",
        text="Stage",
        fill="#FF53C0",
        font=("Poppins Regular", 32 * -1)
    )

    canvas.create_rectangle(
        29.0,
        118.0,
        980.0,
        122.0,
        fill="#D9D9D9",
        outline="")
    window.mainloop()

def customerpage(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def customer_button_click():
        if entry_1.get() == "":
            messagebox.showerror("Alert", "Please enter customer name")
        elif not re.match(r"^[A-Za-z]+(?: [A-Za-z]+)+$", entry_1.get()):
            messagebox.showerror("Alert", "Please enter a valid Full Name (e.g., John Doe)")

        elif entry_2.get() == "":
            messagebox.showerror("Alert", "Please enter customer phone number")
        elif not re.match(r"^0\d{2} \d{3} \d{3,4}$", entry_2.get()):
            messagebox.showerror("Alert", "Please enter a valid phone number (e.g., 012 345 678 or 012 345 6789)")
        else:

            name = entry_1.get()
            phone = entry_2.get()

            conn = None
            try:
                conn = pymysql.connect(
                    host="127.0.0.1",
                    user="root",
                    password=get_creds(),
                    db="csa",
                )

            except Exception as ex:
                print("PROBLEM WITH Database Connection", ex)
            else:
                print("Database Connection SUCCESS")

            if conn is not None:
                query_find_incomplete = """
                                 SELECT CustomerID
                                 FROM Customers
                                 WHERE CustomerName IS NULL
                                    OR PhoneNumber IS NULL
                                    OR Concert IS NULL
                                    OR ConcertDate IS NULL
                                    OR Section IS NULL
                                 ORDER BY CustomerID DESC
                                 LIMIT 1;
                             """
                cursor = conn.cursor()
                cursor.execute(query_find_incomplete)
                result = cursor.fetchone()

                if result:
                    # Incomplete row found, update it
                    customer_id = result[0]
                    query_update = """
                                     UPDATE Customers
                                     SET 
                                         CustomerName = COALESCE(CustomerName, %s),
                                         PhoneNumber = COALESCE(PhoneNumber, %s)

                                     WHERE CustomerID = %s;
                                 """
                    try:
                        noofrecoredinsert = cursor.execute(query_update, (name, phone, customer_id))
                        conn.commit()

                    except Exception as e:
                        print("INSERT PROBLEM ", e)
                    else:
                        if noofrecoredinsert > 0:
                            print("RECORD INSERTED ")
                            messagebox.showinfo("Success", "Payment Complete")
                            navigate(window, receiptpage)

    def home_button_click():

        conn = None
        try:
            conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password=get_creds(),
                db="csa",
            )

        except Exception as ex:
            print("PROBLEM WITH Database Connection", ex)
        else:
            print("Database Connection SUCCESS")

        if conn is not None:
            query_find_incomplete = """
                     SELECT CustomerID
                     FROM Customers
                     WHERE CustomerName IS NULL
                        OR PhoneNumber IS NULL
                        OR Concert IS NULL
                        OR ConcertDate IS NULL
                        OR Section IS NULL
                     ORDER BY CustomerID DESC
                     LIMIT 1;
                 """
            cursor = conn.cursor()
            cursor.execute(query_find_incomplete)
            result = cursor.fetchone()

            if result:
                # Incomplete row found, update it
                customer_id = result[0]
                query_update = """
                         DELETE FROM Customers
                         WHERE CustomerID = %s;
                     """
                try:
                    noofrecoredinsert = cursor.execute(query_update, (customer_id))
                    conn.commit()

                except Exception as e:
                    print("DELETE PROBLEM ", e)
                else:
                    if noofrecoredinsert > 0:
                        print("RECORD DELETED ")
                        messagebox.showinfo("Warning", "Restart Purchase")
                        navigate(window, homepage)

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        126.0,
        235.0,
        891.0,
        633.0,
        fill="#270683",
        outline="")

    canvas.create_text(
        92.0,
        24.0,
        anchor="nw",
        text="Customer Information",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: home_button_click(),
        relief="flat"
    )
    button_1.place(
        x=30.0,
        y=38.0,
        width=45.0,
        height=46.0
    )

    canvas.create_rectangle(
        29.0,
        118.0,
        980.0,
        122.0,
        fill="#D9D9D9",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        507.5,
        323.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Poppins Regular", 37 * -1)
    )
    entry_1.place(
        x=180.0,
        y=295.0,
        width=655.0,
        height=54.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        507.5,
        450.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Poppins Regular", 37 * -1)
    )
    entry_2.place(
        x=180.0,
        y=423.0,
        width=655.0,
        height=52.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: customer_button_click(),
        relief="flat"
    )
    button_2.place(
        x=154.0,
        y=515.0,
        width=137.0,
        height=76.0
    )

    canvas.create_text(
        165.0,
        249.0,
        anchor="nw",
        text="Full Name",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )

    canvas.create_text(
        157.0,
        376.0,
        anchor="nw",
        text="Phone Number",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )
    window.mainloop()

def receiptpage(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame6")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    conn = None
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password=get_creds(),
            db="csa",
        )

    except Exception as ex:
        print("PROBLEM WITH Database Connection", ex)
    else:
        print("Database Connection SUCCESS")

    if conn is not None:
        cursor = conn.cursor()
        # Get the most recent CustomerID (last inserted row)
        cursor.execute("SELECT CustomerID, CustomerName, PhoneNumber, Concert, ConcertDate, Section FROM Customers ORDER BY CustomerID DESC LIMIT 1")
        result = cursor.fetchone()
        customer_Id, customer_name, phone_number, concert_name, concert_date, seat_section = result
        # Get the price of the concert
        cursor.execute("SELECT Price FROM Concerts where ConcertSection = %s", seat_section)
        price_query_result = cursor.fetchone()
        if price_query_result:
            price = price_query_result[0]

            cursor.execute("Select memberName FROM membership where memberName = (%s) and memberPhoneNumber = (%s)",(customer_name,phone_number))
            member = cursor.fetchone()
            if member:
                price = float(price-(price*0.1))
                messagebox.showinfo("Special Offer", "Customer gets 10% off their purchase")
                cursor.execute("UPDATE customers SET cost = (%s) WHERE CustomerID = (%s)", (price, customer_Id))
                conn.commit()
            else:
                cursor.execute("UPDATE customers SET cost = (%s) WHERE CustomerID = (%s)", (price, customer_Id))
                conn.commit()

    canvas.place(x=0, y=0)
    canvas.create_text(
        105.0,
        29.0,
        anchor="nw",
        text="Purchase Summary",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, homepage),
        relief="flat"
    )
    button_1.place(
        x=30.0,
        y=38.0,
        width=45.0,
        height=46.0
    )

    canvas.create_rectangle(
        29.0,
        118.0,
        980.0,
        122.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        53.0,
        252.0,
        947.0,
        578.0,
        fill="#EDEDED",
        outline="")

    canvas.create_text(
        304.0,
        298.0,
        anchor="nw",
        text=concert_name,
        fill="#020202",
        font=("Poppins Bold", 24 * -1)
    )

    canvas.create_text(
        304.0,
        266.0,
        anchor="nw",
        text="Concert Ticket",
        fill="#020202",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        322.0,
        387.0,
        anchor="nw",
        text=customer_name,
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_text(
        322.0,
        435.0,
        anchor="nw",
        text=phone_number,
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_text(
        575.0,
        387.0,
        anchor="nw",
        text=concert_date,
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_text(
        575.0,
        435.0,
        anchor="nw",
        text=f"${price}",
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_text(
        322.0,
        488.0,
        anchor="nw",
        text=f"Customer ID : {customer_Id}",
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_text(
        575.0,
        488.0,
        anchor="nw",
        text=seat_section,
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_rectangle(
        312.0,
        375.0,
        783.0,
        377.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        313.0,
        423.0,
        784.0,
        425.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        312.0,
        474.0,
        783.0,
        476.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        312.0,
        524.0,
        783.0,
        526.0,
        fill="#000000",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        165.0,
        415.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        288.0,
        251.0,
        290.0,
        578.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        561.0,
        355.0,
        563.0,
        548.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        810.0,
        252.0,
        812.0,
        578.0,
        fill="#000000",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        876.0,
        413.0,
        image=image_image_2
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: messagebox.showinfo("Success", "Ticket Printed"),
        relief="flat"
    )
    button_2.place(
        x=443.0,
        y=624.0,
        width=137.0,
        height=76.0
    )
    window.mainloop()

def member_registration(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def customer_button_click():
        if entry_1.get() == "":
            messagebox.showerror("Alert", "Please enter customer name")
        elif not re.match(r"^[A-Za-z]+(?: [A-Za-z]+)+$", entry_1.get()):
            messagebox.showerror("Alert", "Please enter a valid Full Name (e.g., John Doe)")

        elif entry_2.get() == "":
            messagebox.showerror("Alert", "Please enter customer phone number")
        elif not re.match(r"^0\d{2} \d{3} \d{3,4}$", entry_2.get()):
            messagebox.showerror("Alert", "Please enter a valid phone number (e.g., 012 345 678 or 012 345 6789)")
        else:

            name = entry_1.get()
            phone = entry_2.get()

            conn = None
            try:
                conn = pymysql.connect(
                    host="127.0.0.1",
                    user="root",
                    password=get_creds(),
                    db="csa",
                )

            except Exception as ex:
                print("PROBLEM WITH Database Connection", ex)
            else:
                print("Database Connection SUCCESS")

            if conn is not None:
                cursor = conn.cursor()
                # Query to check if the member already exists
                check_query = """
                      SELECT * FROM membership WHERE memberName = %s AND memberPhoneNumber = %s;
                      """
                cursor.execute(check_query, (name, phone))
                result = cursor.fetchone()

                if result:
                    # Show a warning if the entry exists
                    messagebox.showwarning("Duplicate Entry", "This member already exists in the database.")
                else:
                    # Insert the new member
                    insert_query = "INSERT INTO membership (memberName, memberPhoneNumber) VALUES (%s, %s);"
                    try:
                        noofrecoredinsert = cursor.execute(insert_query, (name, phone))
                        conn.commit()
                        conn.close()

                    except Exception as e:
                        print("INSERT PROBLEM ", e)
                    else:
                        if noofrecoredinsert > 0:
                            print("RECORD INSERTED ")
                            messagebox.showinfo("Success", "Registration Complete")
                            navigate(window, homepage)

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        126.0,
        235.0,
        891.0,
        633.0,
        fill="#270683",
        outline="")

    canvas.create_text(
        92.0,
        24.0,
        anchor="nw",
        text="Membership Registration",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, homepage),
        relief="flat"
    )
    button_1.place(
        x=30.0,
        y=38.0,
        width=45.0,
        height=46.0
    )

    canvas.create_rectangle(
        29.0,
        118.0,
        980.0,
        122.0,
        fill="#D9D9D9",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        507.5,
        323.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Poppins Regular", 37 * -1)
    )
    entry_1.place(
        x=180.0,
        y=295.0,
        width=655.0,
        height=54.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        507.5,
        450.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Poppins Regular", 37 * -1)
    )
    entry_2.place(
        x=180.0,
        y=423.0,
        width=655.0,
        height=52.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: customer_button_click(),
        relief="flat"
    )
    button_2.place(
        x=154.0,
        y=515.0,
        width=137.0,
        height=76.0
    )

    canvas.create_text(
        165.0,
        249.0,
        anchor="nw",
        text="Full Name",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )

    canvas.create_text(
        157.0,
        376.0,
        anchor="nw",
        text="Phone Number",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )
    window.mainloop()

def ticketsearch(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame7")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def search_button_click():
        if entry_1.get() == "":
            messagebox.showerror("Alert", "Please enter customer name")
        elif not re.match(r"^[A-Za-z]+(?: [A-Za-z]+)+$", entry_1.get()):
            messagebox.showerror("Alert", "Please enter a valid Full Name (e.g., John Doe)")

        elif entry_2.get() == "":
            messagebox.showerror("Alert", "Please enter customer phone number")
        elif not re.match(r"^0\d{2} \d{3} \d{3,4}$", entry_2.get()):
            messagebox.showerror("Alert", "Please enter a valid phone number (e.g., 012 345 678 or 012 345 6789)")
        else:
            global namesearch, phonesearch
            namesearch = entry_1.get()
            phonesearch = entry_2.get()

            conn = None
            try:
                conn = pymysql.connect(
                    host="127.0.0.1",
                    user="root",
                    password=get_creds(),
                    db="csa",
                )

            except Exception as ex:
                print("PROBLEM WITH Database Connection", ex)
            else:
                print("Database Connection SUCCESS")

            if conn is not None:
                cursor = conn.cursor()
                query = """
                                    SELECT * FROM Customers
                                    WHERE CustomerName = %s AND PhoneNumber = %s
                                """
                cursor.execute(query, (namesearch, phonesearch))
                result = cursor.fetchone()
                conn.commit()

                if result:
                    messagebox.showinfo("SUCCESS", "Customer Ticket Found")
                    print(namesearch, phonesearch)
                    navigate(window, receiptsearchpage)
                else:
                    messagebox.showinfo("ALERT", "Customer Ticket Not Found")
                    return

    canvas.place(x=0, y=0)

    canvas.create_rectangle(
        30.0,
        144.0,
        980.0,
        380.0,
        fill="#270683",
        outline="")

    canvas.create_text(
        92.0,
        24.0,
        anchor="nw",
        text="Search Past Customers Tickets",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, homepage),
        relief="flat"
    )
    button_1.place(
        x=30.0,
        y=38.0,
        width=45.0,
        height=46.0
    )

    canvas.create_rectangle(
        29.0,
        118.0,
        980.0,
        122.0,
        fill="#D9D9D9",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        275.9019870040602,
        232.411440691341,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Poppins Regular", 37 * -1)
    )
    entry_1.place(
        x=75.97735595703125,
        y=203.72635189888683,
        width=399.84926209405785,
        height=55.37017758490833
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        741.5,
        232.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Poppins Regular", 37 * -1)
    )
    entry_2.place(
        x=549.0,
        y=205.0,
        width=385.0,
        height=52.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: search_button_click(),
        relief="flat"
    )
    button_2.place(
        x=53.0,
        y=281.0,
        width=137.0,
        height=76.0
    )

    canvas.create_text(
        58.0,
        150.0,
        anchor="nw",
        text="Name",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )

    canvas.create_text(
        523.0,
        150.0,
        anchor="nw",
        text="Phone Number",
        fill="#FFFFFF",
        font=("Poppins Regular", 32 * -1)
    )

    canvas.create_rectangle(
        65.0,
        409.0,
        959.0,
        735.0,
        fill="#EDEDED",
        outline="")

    canvas.create_text(
        316.0,
        455.0,
        anchor="nw",
        text="Concert Name",
        fill="#020202",
        font=("Poppins Bold", 24 * -1)
    )

    canvas.create_text(
        316.0,
        423.0,
        anchor="nw",
        text="Concert Ticket",
        fill="#020202",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        334.0,
        544.0,
        anchor="nw",
        text="Customer Name",
        fill="#020202",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        334.0,
        592.0,
        anchor="nw",
        text="Phone Number",
        fill="#020202",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        585.0,
        544.0,
        anchor="nw",
        text="Concert Date",
        fill="#020202",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        589.0,
        592.0,
        anchor="nw",
        text="Cost",
        fill="#020202",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        334.0,
        645.0,
        anchor="nw",
        text="Customer ID",
        fill="#020202",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        587.0,
        645.0,
        anchor="nw",
        text="Section",
        fill="#020202",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_rectangle(
        324.0,
        532.0,
        795.0,
        534.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        325.0,
        580.0,
        796.0,
        582.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        324.0,
        631.0,
        795.0,
        633.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        324.0,
        681.0,
        795.0,
        683.0,
        fill="#000000",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        177.0,
        572.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        300.0,
        408.0,
        302.0,
        735.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        573.0,
        512.0,
        575.0,
        705.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        822.0,
        409.0,
        824.0,
        735.0,
        fill="#000000",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        888.0,
        570.0,
        image=image_image_2
    )
    window.mainloop()

def receiptsearchpage(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame6")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    conn = None
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password=get_creds(),
            db="csa",
        )

    except Exception as ex:
        print("PROBLEM WITH Database Connection", ex)
    else:
        print("Database Connection SUCCESS")

    if conn is not None:
        cursor = conn.cursor()
        query = """
                        SELECT * FROM Customers
                        WHERE CustomerName = %s AND PhoneNumber = %s
                    """
        cursor.execute(query, (namesearch, phonesearch))
        result = cursor.fetchone()
        conn.commit()

        if result:
            # Assign result to variables
            customer_Id, customer_name, phone_number, concert_name, concert_date, seat_section, cost = result
        else:
            messagebox.showinfo("Alert", "Customer Not Found")
            return


    canvas.place(x=0, y=0)
    canvas.create_text(
        105.0,
        29.0,
        anchor="nw",
        text="Purchase Summary",
        fill="#FFFFFF",
        font=("Poppins Bold", 48 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, homepage),
        relief="flat"
    )
    button_1.place(
        x=30.0,
        y=38.0,
        width=45.0,
        height=46.0
    )

    canvas.create_rectangle(
        29.0,
        118.0,
        980.0,
        122.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        53.0,
        252.0,
        947.0,
        578.0,
        fill="#EDEDED",
        outline="")

    canvas.create_text(
        304.0,
        298.0,
        anchor="nw",
        text=concert_name,
        fill="#020202",
        font=("Poppins Bold", 24 * -1)
    )

    canvas.create_text(
        304.0,
        266.0,
        anchor="nw",
        text="Concert Ticket",
        fill="#020202",
        font=("Poppins Regular", 16 * -1)
    )

    canvas.create_text(
        322.0,
        387.0,
        anchor="nw",
        text=customer_name,
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_text(
        322.0,
        435.0,
        anchor="nw",
        text=phone_number,
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_text(
        575.0,
        387.0,
        anchor="nw",
        text=concert_date,
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_text(
        575.0,
        435.0,
        anchor="nw",
        text=f"${cost}",
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_text(
        322.0,
        488.0,
        anchor="nw",
        text=f"Customer ID : {customer_Id}",
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_text(
        575.0,
        488.0,
        anchor="nw",
        text=seat_section,
        fill="#020202",
        font=("Poppins SemiBold", 16 * -1)
    )

    canvas.create_rectangle(
        312.0,
        375.0,
        783.0,
        377.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        313.0,
        423.0,
        784.0,
        425.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        312.0,
        474.0,
        783.0,
        476.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        312.0,
        524.0,
        783.0,
        526.0,
        fill="#000000",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        165.0,
        415.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        288.0,
        251.0,
        290.0,
        578.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        561.0,
        355.0,
        563.0,
        548.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        810.0,
        252.0,
        812.0,
        578.0,
        fill="#000000",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        876.0,
        413.0,
        image=image_image_2
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: messagebox.showinfo("Success", "Ticket Printed"),
        relief="flat"
    )
    button_2.place(
        x=443.0,
        y=624.0,
        width=137.0,
        height=76.0
    )
    window.mainloop()
