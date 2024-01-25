import tkinter as tk
from tkinter import font

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def change_theme(theme_colors):
    global button_bg, button_fg
    root.configure(bg=theme_colors["bg"])
    button_bg = theme_colors["button_bg"]
    button_fg = theme_colors["button_fg"]
    for button in buttons:
        button.config(bg=button_bg, fg=button_fg)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

# Entry widget to display the input and result
entry = tk.Entry(root, font=("Helvetica", 36, "bold"), bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Define button style
button_font = font.Font(family="Helvetica", size=18, weight="bold")
button_bg = "#f9f9f9"
button_fg = "#333333"

# Color themes
themes = [
    {
        "name": "HazleWood",
        "bg": "#c9bb8e",
        "button_bg": "#f9f9f9",
        "button_fg": "#333333",
    },
    {
        "name": "Dark",
        "bg": "#222222",
        "button_bg": "#333333",
        "button_fg": "#f9f9f9",
    },
    {
        "name": "Fawn",
        "bg": "#c8a951",
        "button_bg": "#36d536",
        "button_fg": "#f9f9f9",
    },
]

# Buttons
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
    ("=",)
]

for row_idx, row in enumerate(buttons):
    for col_idx, label in enumerate(row):
        button = tk.Button(
            root,
            text=label,
            font=button_font,
            bg=button_bg,
            fg=button_fg,
            padx=20,
            pady=20,
            relief="flat",
            borderwidth=0,
            highlightthickness=4,
            highlightbackground="#dcdcdc",
            activebackground="#ebebeb",
        )
        button.grid(row=row_idx + 1, column=col_idx, padx=5, pady=5, sticky="nsew")
        button.bind("<Button-1>", on_click)

# Make all buttons in each row and column the same size
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Create theme buttons
theme_frame = tk.Frame(root, bg="#f0f0f0")
theme_frame.grid(row=6, column=0, columnspan=4, pady=10)

for idx, theme in enumerate(themes):
    theme_btn = tk.Button(
        theme_frame,
        text=theme["name"],
        font=("Helvetica", 14),
        bg=theme["bg"],
        fg="#333333",
        padx=10,
        pady=5,
        relief="flat",
        command=lambda t=theme: change_theme(t),
    )
    theme_btn.grid(row=0, column=idx, padx=5)

# Run the main event loop
root.mainloop()
