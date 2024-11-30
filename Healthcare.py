import tkinter as tk

def submit():
    print(f"Name: {name_var.get()}, Age: {age_var.get()}, Issue: {issue_var.get()}")

app = tk.Tk()
app.title("Healthcare App")

tk.Label(app, text="Name:").grid(row=0, column=0)
name_var = tk.StringVar()
tk.Entry(app, textvariable=name_var).grid(row=0, column=1)

tk.Label(app, text="Age:").grid(row=1, column=0)
age_var = tk.StringVar()
tk.Entry(app, textvariable=age_var).grid(row=1, column=1)

tk.Label(app, text="Issue:").grid(row=2, column=0)
issue_var = tk.StringVar()
tk.Entry(app, textvariable=issue_var).grid(row=2, column=1)

tk.Button(app, text="Submit", command=submit).grid(row=3, column=0, columnspan=2)

app.mainloop()
