import tkinter as tk

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.inser(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + event.widget.cget("text"))

def clear_input():
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Simple Calculator")

entry = tk.Entry(window, font=('Arial', 18), borderwidth=2, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    'C','0','=','+'
]

row,col = 1,0

for button in buttons:
    btn = tk.Button(window, text=button, font=('Arial', 18), width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)

    if button =='=':
        btn.bind("<Button-1>", lambda event: evaluate_expression())
    elif button == 'C':
        btn.bind("<Button-1>", lambda event: clear_input())
    else:
        btn.bind("<Button-1>", button_click)

    col += 1
    if col>3:
        col=0
        row += 1

window.mainloop()