


import tkinter as tk
from tkinter import ttk
import time
import threading

root = tk.Tk()
root.title("Threaded Progress Bar")
root.geometry("400x200")

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

percent_label = tk.Label(root, text="0%")
percent_label.pack()

stop_thread= False

def run_progress():
    global stop_thread
    for i in range(101):
        if stop_thread:
            break
        progress["value"] = i
        percent_label.config(text=f"{i}%")
        time.sleep(1.2)
        root.update()
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)


def start():
    global stop_thread
    stop_thread = False
    progress["value"] = 0
    t = threading.Thread(target=run_progress)
    t.start()
    percent_label.config(text="0%")
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
   


def stop():
    global stop_thread
    stop_thread = True
    progress["value"] = 0
    percent_label.config(text="0%")
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    

start_button = tk.Button(root, text="Start",command=start)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(pady=10)




start_button.config(command=start)
stop_button.config(command=stop)


root.mainloop()
