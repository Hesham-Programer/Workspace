import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FindMatches:

    def __init__(self):

        self.user_text = str
        self.original_text = str

        self.root = tk.Tk()
        self.root.title("Find Matches")
        self.root.geometry("900x500")

        self.text_label = ttk.Label(master=self.root, text="Your Text:\t\t\t\tOriginal Text:", font=("Arial", 14, "bold"))
        self.text_label.pack(pady=10, side=tk.TOP)

        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.user_text_entry = tk.Text(master=self.frame, wrap=tk.WORD, width=50, height=10)
        self.user_text_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(master=self.frame, orient=tk.VERTICAL, command=self.user_text_entry.yview)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.user_text_entry['yscrollcommand'] = self.scrollbar.set

        self.original_text_entry = tk.Text(master=self.frame, wrap=tk.WORD, width=50, height=10)
        self.original_text_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(master=self.frame, orient=tk.VERTICAL, command=self.original_text_entry.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.original_text_entry['yscrollcommand'] = self.scrollbar.set

        self.result_label = ttk.Label(master=self.root, text="Your Text:\t\t\t\tOriginal Text:", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

        self.exit_button = ttk.Button(master=self.root, text="Find matches", width=35, command=self.find_matches)
        self.exit_button.pack(pady=10)

        self.root.mainloop()

    def find_matches(self):
        regex = self.user_text_entry.get("1.0", "end-1c")
        text = self.original_text_entry.get("1.0", "end-1c")
        if regex == "" and text == "":
            messagebox.showwarning(title="Empty Entry", message="Please Fill The Empty Entry")
        if regex and text:
            matches = re.finditer(regex, text)
            for match in matches:
                start_index = f"1.0 + {match.start()} chars"
                end_index = f"1.0 + {match.end()} chars"
                self.user_text_entry.tag_add("match", start_index, end_index)
                self.original_text_entry.tag_add("match", start_index, end_index)
            self.user_text_entry.tag_config("match", foreground="black", background="red", font=("Arial", 10, "bold"))
            self.original_text_entry.tag_config("match", foreground="black", background="green", font=("Arial", 10, "bold"))


    def clear(self):
        self.user_text_entry.delete("1.0", "end-1c")
        self.original_text_entry.delete("1.0", "end-1c")