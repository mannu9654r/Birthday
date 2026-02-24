import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')  # Format: Hour:Minute:Second AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every 1000ms (1 second)

# Create the window
root = tk.Tk()
root.title("Digital Clock")

# Configure the window size and background
root.geometry("350x150")
root.configure(bg="black")

# Create the time display label
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Start the clock
time()

# Run the app
root.mainloop()
