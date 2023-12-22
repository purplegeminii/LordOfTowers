from Player import Player
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("1000x600")  # Width x Height
root.title("LOT")
frame = ttk.Frame(root, padding=10)
frame.grid()


# Create a label widget
tk.Label(frame, text="Welcome to Lord Of Towers!").grid(column=0, row=0)

# Player object
player1 = Player(name="Delali")
print(player1)
print("\n")

def greet() -> None:
    print("Button Clicked!")

# Create a button widget
btn1 = tk.Button(frame, text="Button", command=greet)
btn1.grid(column=0, row=1)

# Quit btn
tk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=1)

def main() -> None:
    print("""game start""")
    root.mainloop()

if __name__ == "__main__":
    main()
