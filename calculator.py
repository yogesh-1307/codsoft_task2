import tkinter as tk

def button_click(event):
    current = result_var.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif text == "C":
        result_var.set("")
    else:
        result_var.set(current + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")

result_var = tk.StringVar()
result_var.set("")

result_display = tk.Entry(root, textvar=result_var, font="Helvetica 20", justify="right")
result_display.pack(fill=tk.BOTH, padx=10, pady=10, ipadx=10, ipady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", ".", "+"),
    ("=")
]

for button_row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack()

    for button_text in button_row:
        button = tk.Button(row_frame, text=button_text, font="Helvetica 16", padx=20, pady=20)
        button.pack(side=tk.LEFT)
        button.bind("<Button-1>", button_click)

root.mainloop()
