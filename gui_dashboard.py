# GUI dashboard script
import tkinter as tk
import os

root = tk.Tk()
root.title("Automation Suite Dashboard")
root.geometry("400x350")
root.config(bg="#1e1e1e")

def run_script(script):
    os.system(f"python {script}")

tk.Label(root, text="Automation Suite", fg="white", bg="#1e1e1e", font=("Segoe UI", 18, "bold")).pack(pady=20)

buttons = [
    ("Run File Organizer", "file_organizer.py"),
    ("Run Web Scraper", "web_scraper.py"),
    ("Send Email", "email_automation.py"),
    ("Monitor System", "system_monitor.py"),
    ("Run All Tasks", "scheduler_runner.py")
]

for text, script in buttons:
    tk.Button(root, text=text, width=25, height=2, command=lambda s=script: run_script(s), bg="#0078D7", fg="white", relief="flat").pack(pady=5)

root.mainloop()
