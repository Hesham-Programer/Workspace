import tkinter as tk
from tkinter import ttk
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class Pomodoro:
    
    def __init__(self):

        self.timer = ""
        self.reps = 0

        self.window = tk.Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)

        self.title_label = ttk.Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 35, "bold"))
        self.title_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        tomato_img = tk.PhotoImage(file="images/tomato.png")
        self.canvas.create_image(100, 112, image=tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        self.start_button = ttk.Button(text="Start", command=self.start_timer)
        self.start_button.grid(column=0, row=2)

        self.reset_button = ttk.Button(text="Reset", command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)

        self.check_marks = ttk.Label(foreground=GREEN, background=YELLOW)
        self.check_marks.grid(column=1, row=3)

        self.window.mainloop()

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="Timer")
        self.check_marks.config(text="")
        self.reps = 0

    def start_timer(self):
        self.reps += 1

        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if self.reps % 8 == 0:
            self.count_down(long_break_sec)
            self.title_label.config(text="Break", foreground=RED)
        elif self.reps % 2 == 0:
            self.count_down(short_break_sec)
            self.title_label.config(text="Break", foreground=PINK)
        else:
            self.count_down(work_sec)
            self.title_label.config(text="Work", foreground=GREEN)

    def count_down(self, count):

        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            marks = ""
            work_sessions = math.floor(self.reps / 2)
            for _ in range(work_sessions):
                marks += "✔"
            self.check_marks.config(text=marks)
    def exit_pomodoro(self):
        self.window.destroy()
