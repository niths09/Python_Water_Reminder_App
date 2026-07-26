# 💧 Python Water Reminder App

## 📌 About

This project is a desktop water reminder application built with Python and Tkinter that displays an animated avatar reminder at regular intervals to encourage healthy hydration habits.

The application appears as a small popup on the desktop with a custom animated avatar, fade-in/fade-out effects, and system tray support. Users can configure the reminder interval and manage the application directly from the Windows system tray.

---

## ✨ Features

- 💧 Hourly water reminder popup
- 🎬 Animated avatar using PNG frame animation
- 🖥️ Lightweight desktop popup
- 🎨 Transparent popup window
- 🌟 Smooth fade-in and fade-out animation
- 📌 Windows system tray integration
- ⚙️ Configurable reminder interval through `settings.json`
- ▶ Show reminder instantly from the tray
- ⏸ Pause and resume reminders
- ❌ Exit application from the system tray

---

## 🛠️ Technologies Used

- Python
- Tkinter
- Pillow (PIL)
- PyStray
- JSON

---

## 📁 Project Structure

```
WaterReminder/
│
├── frames/
│   ├── frame01.png
│   ├── ...
│   └── frame09.png
│
├── icons/
│   └── water.ico
│
├── main.py
├── settings.json
└── README.md
```

---

## ⚙️ Configuration

The reminder settings can be modified in `settings.json`.

Example:

```json
{
    "interval_minutes": 60,
    "display_seconds": 0,
    "animation_speed": 300,
    "frame_delay": 500
}
```

---

## 🚀 How to Run

1. Install the required libraries:

```
pip install pillow pystray
```

2. Run the application:

```
python main.py
```

---

## 📸 Preview

The application displays an animated desktop popup reminding users to stay hydrated while running quietly in the Windows system tray.

---

## 🎯 Purpose

This project was created as a personal desktop utility to promote healthy hydration habits through simple, lightweight, and non-intrusive reminders.

---

## 👩‍💻 Author

**Nithu Lakshmi**

GitHub: https://github.com/niths09
