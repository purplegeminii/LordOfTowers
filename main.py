from Player import Player
import tkinter as tk
from tkinter import ttk
import timeit
import time


root = tk.Tk()
root.geometry("800x600")  # Width x Height
root.title("LOT")
frame = tk.Frame(root, padx=10, pady=10, bg="black")
frame.grid(row=0, column=0, sticky="nsew")
frame_width, frame_height = frame.winfo_width(), frame.winfo_height()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


# Create a label widget
welcome_lbl = tk.Label(frame, text="Welcome to Lord Of Towers!")
welcome_lbl.grid(column=0, row=0)

# Player object
player1 = Player(name="Delali Nsiah-Asare")
print(player1)

# HP and MP bars frame
hp_mp_bars = tk.Frame(frame)
hp_mp_bars.rowconfigure(0, weight=1)
hp_mp_bars.rowconfigure(1, weight=1)
hp_mp_bars.place(x=25, y=50)

# Create a canvas to draw the health bar
hp_canvas = tk.Canvas(hp_mp_bars, width=200, height=30, bg="red")
hp_canvas.grid(row=0, column=0, sticky=tk.W+tk.E)

# Draw the health bar
health_value = player1.health_bar/player1.base_hp * 100
health_bar = hp_canvas.create_rectangle(0, 0, health_value * 2, 30, fill="green")

def update_health_bar() -> None:
    global health_value, hp_canvas, health_bar
    player1.health_bar = player1.health_bar - 40
    health_value = player1.health_bar/player1.base_hp * 100
    hp_canvas.delete(health_bar)
    health_bar = hp_canvas.create_rectangle(0, 0, (health_value) * 2, 30, fill="green")

# Create a canvas to draw the mana bar
mp_canvas = tk.Canvas(hp_mp_bars, width=200, height=30, bg="white")
mp_canvas.grid(row=1, column=0, sticky=tk.W+tk.E)

# Draw the mana bar
mana_value = player1.mana_bar/player1.base_mp * 100
mana_bar = mp_canvas.create_rectangle(0, 0, mana_value * 2, 30, fill="blue")

def update_mana_bar() -> None:
    global mana_value, mp_canvas, mana_bar
    player1.mana_bar = player1.mana_bar - 40
    mana_value = player1.mana_bar/player1.base_mp * 100
    mp_canvas.delete(mana_bar)
    mana_bar = mp_canvas.create_rectangle(0, 0, (mana_value) * 2, 30, fill="blue")

def show_player_status() -> None:
    global frame
    print("Player Status window opened!")
    player_status_canvas = player1.get_player_status(frame)
    player_status_canvas.place(x=300, y=50)
    frame.after(5000, player_status_canvas.destroy)

# button frame to hold the ff btn: [status, quit, update hp, update mp]
buttonframe = tk.Frame(frame)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.place(x=50, y=200)

# Create a button widget
btn1 = tk.Button(buttonframe, text="Status", command=show_player_status)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

# Quit btn
quitbtn = tk.Button(buttonframe, text="Quit", command=root.destroy)
quitbtn.grid(row=0, column=1, sticky=tk.W+tk.E)

# Update health button
update_hp_btn = tk.Button(buttonframe, text="Update HP", command=update_health_bar)
update_hp_btn.grid(row=1, column=0, sticky=tk.W+tk.E)

# Update mana button
update_mp_btn = tk.Button(buttonframe, text="Update MP", command=update_mana_bar)
update_mp_btn.grid(row=1, column=1, sticky=tk.W+tk.E)


def main() -> None:
    print("""game start""")
    root.mainloop()

if __name__ == "__main__":
    main()
