import tkinter as tk
from pomodoro import Pomodoro
from tkinter import ttk
from ai_chat import AiChat
from timer import CountDownTimer
from find_matches import FindMatches
from send_email import SendEmail
from Password_manger import PasswordManger


NAME = "Hesham"
WELCOME_FONT = ("italic", 15, "bold")

class Main:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("400x350")
        self.root.title("My workspace")

        self.workspace_label = ttk.Label(master=self.root, text=f"Welcome {NAME} To Your workspace!", font=WELCOME_FONT)
        self.workspace_label.pack(pady=10, expand=True)

        self.pomodoro_button = ttk.Button(text="Pomodoro", width=50, command=self.pomodoro)
        self.pomodoro_button.pack(pady=5, expand=True)

        self.chat_button = ttk.Button(text="AI Chat", width=50, command=AiChat)
        self.chat_button.pack(pady=5, expand=True)

        self.send_email_button = ttk.Button(text="Send Email", width=50, command=self.send_email)
        self.send_email_button.pack(pady=5, expand=True)

        self.password_manager_button = ttk.Button(text="Password Manger", width=50, command=self.password)
        self.password_manager_button.pack(pady=5, expand=True)

        self.timer_button = ttk.Button(text="Timer", width=50, command=self.timer)
        self.timer_button.pack(pady=5, expand=True)

        self.find_difference_button = ttk.Button(text="Compare a piece of text", width=50, command=self.compare)
        self.find_difference_button.pack(pady=5, expand=True)

        self.exit_button = ttk.Button(text="Exit", width=10, command=self.exit_function)
        self.exit_button.pack(pady=5, expand=True)

        self.root.mainloop()

    def exit_function(self):
        self.root.destroy()

    def pomodoro(self):
        self.root.destroy()
        Pomodoro()

    def timer(self):
        self.root.destroy()
        CountDownTimer()

    def compare(self):
        FindMatches()

    def send_email(self):
        self.root.destroy()
        SendEmail()
    def password(self):
        PasswordManger()

if __name__ == "__main__":
    Main()
