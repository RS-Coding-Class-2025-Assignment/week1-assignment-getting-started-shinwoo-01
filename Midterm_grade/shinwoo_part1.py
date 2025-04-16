
import tkinter as tk

root = tk.Tk()
root.title("Celsius to Fahrenheit")
root.geometry("400x200")


def CtoF():
    try:
        celsius = float(entry.get())
        fahrenheit = celsius * 9/5 + 32
        result_label.config(text=f"Result: {fahrenheit:.1f} F")
    except ValueError:
        result_label.config(text="Error")


label_name = tk.Label(root, text="Enter Celsius:")
label_name.grid(row=0, column=0, padx=5, pady=5)


entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)


convert_btn = tk.Button(root, text="Convert", command=CtoF)
convert_btn.grid(row=1, column=0, padx=2, pady=10)


result_label = tk.Label(root, text="Result: _ F")
result_label.grid(row=2, column=0, padx=2, pady=10)


root.mainloop()
