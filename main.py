from Player import Player
import tkinter as tk
from tkinter import ttk
import timeit


root = tk.Tk()
root.geometry("1000x600")  # Width x Height
root.title("LOT")
frame = tk.Frame(root, padx=10, pady=10)
frame.grid()


# Create a label widget
tk.Label(frame, text="Welcome to Lord Of Towers!").grid(column=0, row=0)

# Player object
player1 = Player(name="Delali Nsiah-Asare")
print(player1)
print("\n")

# Create a canvas to draw the health bar
hp_canvas = tk.Canvas(frame, width=200, height=30, bg="red")
hp_canvas.grid(column=0, row=1)

# Draw the health bar
health_value = player1.health_bar/player1.base_hp * 100
health_bar = hp_canvas.create_rectangle(0, 0, health_value * 2, 30, fill="green")

def update_health_bar() -> None:
    global health_value, hp_canvas, health_bar
    player1.health_bar = player1.health_bar - 40
    health_value = player1.health_bar/player1.base_hp * 100
    hp_canvas.delete(health_bar)
    health_bar = hp_canvas.create_rectangle(0, 0, (health_value) * 2, 30, fill="green")

# Create a canvas to draw the health bar
mp_canvas = tk.Canvas(frame, width=200, height=30, bg="white")
mp_canvas.grid(column=0, row=2)

# Draw the health bar
mana_value = player1.mana_bar/player1.base_mp * 100
mana_bar = mp_canvas.create_rectangle(0, 0, mana_value * 2, 30, fill="blue")

def update_mana_bar() -> None:
    global mana_value, mp_canvas, mana_bar
    player1.mana_bar = player1.mana_bar - 40
    mana_value = player1.mana_bar/player1.base_mp * 100
    mp_canvas.delete(mana_bar)
    mana_bar = mp_canvas.create_rectangle(0, 0, (mana_value) * 2, 30, fill="blue")

def greet() -> None:
    print("Button Clicked!")

# Create a button widget
btn1 = tk.Button(frame, text="Button", command=greet)
btn1.grid(column=0, row=3)

# Quit btn
quitbtn = tk.Button(frame, text="Quit", command=root.destroy)
quitbtn.grid(column=1, row=3)

# Update health button
update_hp_btn = tk.Button(frame, text="Update HP", command=update_health_bar)
update_hp_btn.grid(column=0, row=4)

# Update mana button
update_mp_btn = tk.Button(frame, text="Update MP", command=update_mana_bar)
update_mp_btn.grid(column=1, row=4)

def main() -> None:
    print("""game start""")
    root.mainloop()

if __name__ == "__main__":
    main()
