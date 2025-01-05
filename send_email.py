import tkinter as tk  
from tkinter import ttk  
import smtplib  
import os


MY_PASSWORD = "qxesoanabybqmyan"
MY_EMAIL = "nasreldinheshamword@gmail.com"  


class SendEmail:

    def __init__(self):  
        self.root = tk.Tk()  
        self.root.title("Send Email")  

        self.from_label = ttk.Label(master=self.root, text="From")
        self.from_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')  

        self.email_label = ttk.Label(master=self.root, text=MY_EMAIL)  
        self.email_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.to_label = ttk.Label(self.root, text="To: ")  
        self.to_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.to_entry = ttk.Entry(master=self.root)  
        self.to_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')  

        self.subject_label = ttk.Label(master=self.root, text="Subject")  
        self.subject_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')  

        self.subject_entry = ttk.Entry(master=self.root)  
        self.subject_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')  

        self.message_label = ttk.Label(master=self.root, text="Message:")  
        self.message_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')  

        self.frame = tk.Frame(self.root)  
        self.frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')  

        self.text_area = tk.Text(self.frame, height=5)  
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  

        self.scrollbar = tk.Scrollbar(self.frame, command=self.text_area.yview)  
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  

        self.text_area.config(yscrollcommand=self.scrollbar.set)  

        self.send_button = ttk.Button(self.root, text="Send", command=self.send_email)  
        self.send_button.grid(row=5, column=0, columnspan=2, pady=10)  

        self.root.grid_rowconfigure(4, weight=1)
        self.root.columnconfigure(1, weight=1)

        self.root.mainloop()  

    def send_email(self):
        to_email = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.text_area.get("1.0", tk.END)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject:{subject}\n\n{message}")


