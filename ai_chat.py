import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import google.generativeai as genai

ENTRY_FONT = ("italic", 13, "bold")
AI_NAME = "gemini-1.5-flash"
AI_FONT = ("Arial", 20, "bold")
API_KEY = "AIzaSyB1LreF4vXQVW143o0Cn9LNXGCCaHH01Pw"

class AiChat:

    def __init__(self):

        self.formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Ai Chat")

        self.frame = ttk.Frame(master=self.root)
        self.frame.pack(padx=0, pady=0, fill=tk.BOTH, expand=True)

        self.chat_box = tk.Text(master=self.frame, wrap=tk.WORD, width=30, height=15, state="disabled")
        self.chat_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scroll_bar = ttk.Scrollbar(master=self.frame, orient=tk.VERTICAL, command=self.chat_box.yview)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self.chat_box["yscrollcommand"] = self.scroll_bar.set

        self.user_entry = ttk.Entry(master=self.root, width=55, font=("Arial", 12, "italic"))
        self.user_entry.pack(pady=10, side=tk.LEFT, expand=True)

        self.send_button = ttk.Button(master=self.root, width=20, text="Send", command=self.send_massage)
        self.send_button.pack(pady=10, side=tk.RIGHT, expand=True, padx=5)


        self.root.mainloop()
    
    def send_massage(self):
        if self.user_entry.get().strip() != "":
            self.chat_box.config(state="normal")

            self.chat_box.tag_configure("user", foreground="blue", font=("Arial", 12, "italic"))
            self.chat_box.tag_configure("bot", foreground="green", font=("Courier New", 11))

            self.chat_box.insert(tk.END, f"You: {self.user_entry.get()}\n\n\t(Time: {self.formatted_time})\n\n\n", "user") 
            
            genai.configure(api_key=API_KEY)
            self.chat_box.insert(tk.END, f"Bot: {genai.GenerativeModel('gemini-1.5-flash').generate_content(self.user_entry.get()).text}\n", "bot") 

            self.user_entry.delete(0, tk.END)
            self.chat_box.config(state="disabled")
        else:
            messagebox.showwarning("Empty Input!", "You left the entry empty!")


