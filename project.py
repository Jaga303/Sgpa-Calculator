import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook, load_workbook
import os

# Grade to point mapping
grade_points = {
    'O': 10,
    'A+': 9,
    'A': 8,
    'B+': 7,
    'B': 6,
    'C': 5,
    'F': 0
}

# Subject and their credits
subject_credits = {
    'Math': 4,
    'Physics': 3,
    'Chemistry': 3,
    'English': 2,
    'Computer': 4
}

def calculate_sgpa(grades):
    total_points = 0
    total_credits = 0
    for subject, grade in grades.items():
        gp = grade_points.get(grade, None)
        if gp is None:
            return None
        credit = subject_credits[subject]
        total_points += gp * credit
        total_credits += credit
    return round(total_points / total_credits, 2)

def save_to_excel(data, sgpa):
    file = "students_sgpa.xlsx"
    if os.path.exists(file):
        wb = load_workbook(file)
        ws = wb.active
    else:
        wb = Workbook()
        ws = wb.active
        ws.append(["Name", "Reg No", "Branch"] + list(subject_credits.keys()) + ["SGPA"])

    row = [data["name"], data["reg_no"], data["branch"]] + [data["grades"][subj] for subj in subject_credits] + [sgpa]
    ws.append(row)
    wb.save(file)

def submit():
    name = name_entry.get()
    reg_no = reg_no_entry.get()
    branch = branch_entry.get()

    grades = {}
    for subj, entry in grade_entries.items():
        grade = entry.get().strip().upper()
        if grade not in grade_points:
            messagebox.showerror("Error", f"Invalid grade '{grade}' for {subj}")
            return
        grades[subj] = grade

    sgpa = calculate_sgpa(grades)
    if sgpa is None:
        messagebox.showerror("Error", "Error calculating SGPA")
        return

    data = {"name": name, "reg_no": reg_no, "branch": branch, "grades": grades}
    save_to_excel(data, sgpa)
    messagebox.showinfo("Success", f"SGPA calculated: {sgpa}\nData saved to Excel.")

# GUI Setup
root = tk.Tk()
root.title("SGPA Calculator")
root.geometry("400x600")

tk.Label(root, text="Student SGPA Calculator", font=('Arial', 16)).pack(pady=10)

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Registration No:").pack()
reg_no_entry = tk.Entry(root)
reg_no_entry.pack()

tk.Label(root, text="Branch:").pack()
branch_entry = tk.Entry(root)
branch_entry.pack()

tk.Label(root, text="Enter Grades (O, A+, A, B+, B, C, F)").pack(pady=10)

grade_entries = {}
for subj in subject_credits:
    tk.Label(root, text=f"{subj}:").pack()
    entry = tk.Entry(root)
    entry.pack()
    grade_entries[subj] = entry

tk.Button(root, text="Submit", command=submit, bg="green", fg="white").pack(pady=20)

root.mainloop()