import tkinter as tk


class UserProfile(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Profile")
        self.geometry("400x400")

        # Create widgets
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(self, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.age_label = tk.Label(self, text="Age:")
        self.age_label.grid(row=1, column=0, padx=5, pady=5)
        self.age_var = tk.StringVar()
        self.age_entry = tk.Entry(self, textvariable=self.age_var)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        self.gender_label = tk.Label(self, text="Gender:")
        self.gender_label.grid(row=2, column=0, padx=5, pady=5)
        self.gender_var = tk.StringVar()
        self.gender_entry = tk.Entry(self, textvariable=self.gender_var)
        self.gender_entry.grid(row=2, column=1, padx=5, pady=5)

        self.save_button = tk.Button(self, text="Save", command=self.save_profile)
        self.save_button.grid(row=3, column=1, padx=5, pady=5, columnspan=2)

    def save_profile(self):
        name = self.name_var.get()
        age = self.age_var.get()
        gender = self.gender_var.get()
        print(f"Name: {name}, Age: {age}, Gender: {gender}")


app = UserProfile()
app.mainloop()