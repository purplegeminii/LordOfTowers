from Player import Player
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("1000x600")  # Width x Height
root.title("LOT")
frame = ttk.Frame(root, padding=10)
frame.grid()


# Create a label widget
ttk.Label(frame, text="Welcome to Lord Of Towers!").grid(column=0, row=0)

# Player object
player1 = Player(name="Delali")
print(player1)
print("\n")

def greet() -> None:
    print("Button Clicked!")

# Create a style
btn1_style = ttk.Style()
# Configure the foreground color for the button using the style
btn1_style.configure("Custom.TButton", foreground="red", background="blue", relief="raised")

# Create a button widget
btn1 = ttk.Button(frame, text="Button", style="Custom.TButton", command=greet)
btn1.grid(column=0, row=1)

# Quit btn
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=1)

def main() -> None:
    print("""game start""")
    root.mainloop()

if __name__ == "__main__":
    main()
