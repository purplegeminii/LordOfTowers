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
player2 = Player(name="ENEMY PLAYER")
print(player1)
print(player2)

# HP and MP bars frame
player1.create_hp_mp_bars(frame)
hp_mp_bars = player1.hp_mp_bars
hp_mp_bars.place(x=25, y=50)

player2.create_hp_mp_bars(frame)
hp_mp_bars2 = player2.hp_mp_bars
hp_mp_bars2.place(x=530, y=50)

def show_player_status() -> None:
    global frame
    print("Player Status window opened!")
    player_status_canvas = player1.get_player_status(frame)
    player_status_canvas.place(x=280, y=50)
    frame.after(5000, player_status_canvas.destroy)

# button frame to hold the ff btn: [status, quit]
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


# Active skills button frame
active_skill_btns = tk.Frame(frame)
active_skill_btns.rowconfigure(0, weight=1)
active_skill_btns.place(x=50, y=250)

warrior_btn = tk.Button(active_skill_btns, text="slash", command=lambda: player1.use_skill("slash", player2))
warrior_btn.grid(row=0, column=0, sticky=tk.W+tk.E)

assasin_btn = tk.Button(active_skill_btns, text="stab", command=lambda: player1.use_skill("stab", player2))
assasin_btn.grid(row=0, column=1, sticky=tk.W+tk.E)

mage_btn = tk.Button(active_skill_btns, text="fireball", command=lambda: player1.use_skill("fireball", player2))
mage_btn.grid(row=0, column=2, sticky=tk.W+tk.E)


def main() -> None:
    print("""game start""")
    root.mainloop()

if __name__ == "__main__":
    main()
