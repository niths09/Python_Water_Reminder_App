import os
import tkinter as tk
from PIL import Image, ImageTk
import json
import threading
import pystray

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ======================================
# Load Settings
# ======================================

settings_path = os.path.join(
    BASE_DIR,
    "settings.json"
)

with open(settings_path, "r") as file:
    settings = json.load(file)


INTERVAL = settings["interval_minutes"]
DISPLAY_TIME = settings["display_seconds"]
ANIMATION_SPEED = settings["animation_speed"]
FRAME_DELAY = settings["frame_delay"]


# ======================================
# Window Settings
# ======================================

WIDTH = 350
HEIGHT = 420

root = tk.Tk()

root.withdraw()

root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-alpha", 0.0)

TRANSPARENT = "magenta"

root.config(bg=TRANSPARENT)
root.wm_attributes("-transparentcolor", TRANSPARENT)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = screen_width - WIDTH - 30
y = screen_height - HEIGHT - 60

root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")


# ======================================
# Title
# ======================================

title = tk.Label(
    root,
    text="Time  to  drink  some  water!",
    font=("Edu VIC WA NT Hand", 13),
    fg="#4A90E2",
    bg=TRANSPARENT,
    bd=0,
    highlightthickness=0
)

title.pack(pady=(8, 2))


# ======================================
# Load Frames
# ======================================

frames = []

for i in range(1, 10):

    filename = os.path.join(
    BASE_DIR,
    "frames",
    f"frame{i:02}.png"
)

    image = Image.open(filename)

    image.thumbnail((240, 300), Image.LANCZOS)

    frames.append(ImageTk.PhotoImage(image))


# ======================================
# Avatar
# ======================================

avatar = tk.Label(
    root,
    bg=TRANSPARENT,
    bd=0,
    highlightthickness=0
)

avatar.pack()


# ======================================
# Bottom Text
# ======================================

bottom = tk.Label(
    root,
    text="Stay  hydrated",
    font=("Edu VIC WA NT Hand", 11),
    fg="#F4A261",
    bg=TRANSPARENT,
    bd=0,
    highlightthickness=0
)

bottom.pack(pady=(4, 10))


# ======================================
# Animation
# ======================================

frame_index = 0
paused = False


def animate():

    global frame_index

    avatar.config(image=frames[frame_index])

    frame_index += 1

    if frame_index < len(frames):

        root.after(
            FRAME_DELAY,
            animate
        )

    else:

        # Small pause after final frame
        root.after(
            1000,
            hide_popup
        )


# ======================================
# Fade In
# ======================================

def fade_in(alpha=0):

    alpha += 0.05

    root.attributes("-alpha", alpha)

    if alpha < 1:

        root.after(
            30,
            lambda: fade_in(alpha)
        )



# ======================================
# Fade Out
# ======================================

def fade_out(alpha=1):

    alpha -= 0.05

    root.attributes("-alpha", alpha)

    if alpha > 0:

        root.after(
            30,
            lambda: fade_out(alpha)
        )

    else:

        root.withdraw()



# ======================================
# Show Popup
# ======================================

def show_popup():

    print("Popup is showing...")

    global frame_index

    if paused:

        return


    frame_index = 0

    root.attributes("-alpha", 0)

    root.deiconify()

    fade_in()

    animate()



# ======================================
# Hide Popup
# ======================================

def hide_popup():

    fade_out()

    root.after(
        INTERVAL * 60 * 1000,
        show_popup
    )



# ======================================
# Tray Menu Functions
# ======================================

def show_now(icon=None, item=None):

    root.after(
        0,
        show_popup
    )



def pause_reminder(icon=None, item=None):

    global paused

    paused = True



def resume_reminder(icon=None, item=None):

    global paused

    paused = False



def quit_app(icon):

    icon.stop()

    root.quit()

    root.destroy()



# ======================================
# Create Tray
# ======================================

def create_tray():

    print("Tray icon is starting...")


    image = Image.open(
    os.path.join(
        BASE_DIR,
        "icons",
        "water.ico"
    )
)


    menu = pystray.Menu(

        pystray.MenuItem(
            "💧 Show Reminder Now",
            show_now
        ),

        pystray.MenuItem(
            "⏸ Pause Reminder",
            pause_reminder
        ),

        pystray.MenuItem(
            "▶ Resume Reminder",
            resume_reminder
        ),

        pystray.Menu.SEPARATOR,


        pystray.MenuItem(
            "Exit",
            quit_app
        )

    )


    icon = pystray.Icon(

        "Water Reminder",

        image,

        "Water Reminder",

        menu

    )


    icon.run()



# ======================================
# First Reminder
# ======================================

root.after(
    10000,
    show_popup
)


threading.Thread(
    target=create_tray,
    daemon=True
).start()


root.mainloop()