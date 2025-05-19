

import tkinter as tk
from tkinter import messagebox, simpledialog
from src.user import Authenticator
from src.patient import PatientDatabase
from src.notes import NoteDatabase
from src.logger import UsageLogger
from src.stats import StatsGenerator

class ClinicalDataUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clinical Data Warehouse")
        self.root.geometry("550x480")
        self.root.configure(bg="#f9f9f9")
        self.auth = Authenticator()
        self.patients = PatientDatabase()
        self.notes = NoteDatabase()
        self.logger = UsageLogger()
        self.stats = StatsGenerator()
        self.current_user = None

    def run(self):
        self.login_screen()
        self.root.mainloop()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Login to System", font=("Segoe UI", 16, "bold"), bg="#f9f9f9").pack(pady=20)

        frame = tk.Frame(self.root, bg="#f9f9f9")
        frame.pack()

        tk.Label(frame, text="Username", bg="#f9f9f9").grid(row=0, column=0, pady=5, sticky="e")
        username_entry = tk.Entry(frame)
        username_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Password", bg="#f9f9f9").grid(row=1, column=0, pady=5, sticky="e")
        password_entry = tk.Entry(frame, show="*")
        password_entry.grid(row=1, column=1, pady=5)

        tk.Button(self.root, text="Login", width=15, bg="#4CAF50", fg="white",
                  command=lambda: self.login(username_entry.get(), password_entry.get())).pack(pady=20)

    def login(self, username, password):
        user = self.auth.authenticate(username, password)
        if user:
            self.current_user = user
            self.logger.log(username, user.role, 'login_success')
            self.main_menu()
        else:
            self.logger.log(username, 'unknown', 'login_failure')
            messagebox.showerror("Login Failed", "Invalid credentials")

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text=f"Welcome {self.current_user.username} ({self.current_user.role})", font=("Segoe UI", 14), bg="#f9f9f9").pack(pady=15)

        role = self.current_user.role
        if role in ['nurse', 'clinician']:
            actions = [
                ("Retrieve Patient", self.retrieve_patient),
                ("Add Patient", self.add_patient),
                ("Remove Patient", self.remove_patient),
                ("Count Visits", self.count_visits),
                ("View Note", self.view_note),
            ]
        elif role == 'admin':
            actions = [("Count Visits", self.count_visits)]
        elif role == 'management':
            actions = [("Generate Statistics", self.generate_statistics)]
        else:
            actions = []

        for label, action in actions:
            tk.Button(self.root, text=label, width=25, pady=5, bg="#3498db", fg="white", command=action).pack(pady=4)

        tk.Button(self.root, text="Exit", width=25, pady=5, bg="#e74c3c", fg="white", command=self.root.quit).pack(pady=20)

    def retrieve_patient(self):
        pid = simpledialog.askstring("Patient ID", "Enter Patient ID:")
        patient = self.patients.retrieve_latest(pid)
        if patient:
            info = "\n".join(f"{k}: {v}" for k, v in patient.items())
            messagebox.showinfo("Patient Info", info)
            self.logger.log(self.current_user.username, self.current_user.role, f"retrieve_patient {pid}")
        else:
            messagebox.showerror("Error", "Patient not found")

    def add_patient(self):
        fields = [
            ("Patient_ID", str), ("Visit_time", str), ("Visit_department", str),
            ("Gender", str), ("Race", str), ("Age", int),
            ("Ethnicity", str), ("Insurance", str), ("Zip code", str),
            ("Chief complaint", str), ("Note_ID", str), ("Note_type", str)
        ]

        patient_info = {}
        for label, cast in fields:
            val = simpledialog.askstring("Input", f"Enter {label}:")
            if val is None:
                return
            try:
                patient_info[label] = cast(val)
            except:
                messagebox.showerror("Invalid Input", f"{label} must be of type {cast.__name__}")
                return

        self.patients.add_patient(patient_info)
        self.logger.log(self.current_user.username, self.current_user.role, f"add_patient {patient_info['Patient_ID']}")
        messagebox.showinfo("Success", "Patient added successfully.")

    def remove_patient(self):
        pid = simpledialog.askstring("Remove Patient", "Enter Patient ID:")
        self.patients.remove_patient(pid)
        self.logger.log(self.current_user.username, self.current_user.role, f"remove_patient {pid}")
        messagebox.showinfo("Removed", f"Patient {pid} removed successfully.")

    def count_visits(self):
        date = simpledialog.askstring("Visit Date", "Enter Date (YYYY-MM-DD):")
        count = self.patients.count_visits_by_date(date)
        self.logger.log(self.current_user.username, self.current_user.role, f"count_visits {date}")
        messagebox.showinfo("Visit Count", f"Total visits on {date}: {count}")

    def view_note(self):
        pid = simpledialog.askstring("Patient ID", "Enter Patient ID:")
        visit_id = simpledialog.askstring("Visit ID", "Enter Visit ID:")
        if not pid or not visit_id:
            return

        notes = self.notes.get_note_by_patient_and_visit(pid, visit_id)
        if notes:
            note_display = "\n\n".join(f"Note {n['Note_ID']}:\n{n['Note_text']}" for n in notes)
            messagebox.showinfo("Clinical Notes", note_display)
            self.logger.log(self.current_user.username, self.current_user.role, f"view_note {pid} {visit_id}")
        else:
            messagebox.showerror("Not Found", f"No notes found for Patient {pid} and Visit {visit_id}")

    def generate_statistics(self):
        self.stats.generate()
        self.logger.log(self.current_user.username, self.current_user.role, "generate_statistics")
        messagebox.showinfo("Statistics", "Statistics saved as 'age_distribution.png'")
