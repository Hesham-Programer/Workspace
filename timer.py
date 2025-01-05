import threading
import time
import tkinter as tk
from tkinter import ttk
from win10toast import ToastNotifier # type: ignore


class CountDownTimer:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("266x80")
        self.root.title("Countdown Timer")

        self.time_label = ttk.Label(master=self.root, text="Timer", font=("italic", 13, "bold"))
        self.time_label.grid(column=1, row=1)

        self.time_entry = ttk.Entry(master=self.root, width=20)
        self.time_entry.grid(column=1, row=2)

        self.plus_button = ttk.Button(master=self.root, width=10, text="Start", command=self.start_thread)
        self.plus_button.grid(column=2, row=2)

        self.negative_button = ttk.Button(master=self.root, width=10, text="Stop", command=self.stop)
        self.negative_button.grid(column=0, row=2)
        self.stop_loop = False

        self.root.mainloop()

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    def start(self):
        self.stop_loop = False

        hours, minutes, seconds = 0, 0, 0
        string_split = self.time_entry.get().split(":")
        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes = int(string_split[1])
            seconds = int(string_split[2])

        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])

        elif len(string_split) == 1:
            seconds = int(string_split[0])
        else:
            print("Invalid Time Formate")

        full_seconds = hours * 3600 + minutes * 60 + seconds

        while full_seconds > 0 and not self.stop_loop:
            full_seconds -= 1

            minutes, seconds = divmod(full_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            self.time_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)

        if not self.stop_loop:
            toast = ToastNotifier()
            toast.show_toast("Countdown Timer", "Time is up!", duration=10)

    def stop(self):
        self.stop_loop = True
        self.time_label.config(text="00:00:00")

