import tkinter as tk  
from tkinter import ttk  
from random import choice, shuffle, randint
import pyperclip
from tkinter import messagebox
import json

class PasswordManger:
    
    def __init__(self):

        self.labels_color = "#cdd1ce"

        self.root = tk.Tk()
        self.root.title("MyPass")
        self.root.geometry("450x250")  
        self.root.configure(bg="#ebedeb")

        self.title_label = ttk.Label(self.root, text="MyPass", font=("Helvetica", 24, "bold"), background='#ebedeb', foreground='red')  
        self.title_label.pack(pady=10)

        self.input_frame = tk.Frame(self.root, bg='#ebedeb')  
        self.input_frame.pack(pady=10)  

        self.website_label = ttk.Label(self.input_frame, text="Website:", background=self.labels_color)  
        self.website_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.website_entry = ttk.Entry(self.input_frame, width=30)  
        self.website_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = ttk.Button(self.input_frame, text="Search", command=self.find_password)  
        self.search_button.grid(row=0, column=2, padx=5, pady=5)  

        self.email_label = ttk.Label(self.input_frame, text="Email/Username:", background=self.labels_color)  
        self.email_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')  

        self.email_entry = ttk.Entry(self.input_frame, width=30)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.password_label = ttk.Label(self.input_frame, text="Password:", background=self.labels_color)
        self.password_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')

        self.password_entry = ttk.Entry(self.input_frame, width=30)  
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)  

        self.generate_button = ttk.Button(self.input_frame, text="Generate Password", command=self.generate_password)  
        self.generate_button.grid(row=2, column=2, padx=5, pady=5)  

        self.add_button = ttk.Button(self.root, text="Add", command=self.save)  
        self.add_button.pack(pady=(10, 5))

        self.root.mainloop()

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)
    
    def find_password(self):
        website = self.website_entry.get()
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

    def save(self):

        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            try:
                with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                self.website_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)



