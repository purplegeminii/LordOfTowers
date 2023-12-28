from Player import Player
import tkinter as tk
from tkinter import ttk
import timeit
import time
from typing import Optional


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

def show_player_status(player: Player) -> None:
    global frame
    print("Player Status window opened!")
    player_status_canvas = player.get_player_status(frame)
    player_status_canvas.place(x=280, y=50)
    frame.after(5000, player_status_canvas.destroy)

def create_general_btns(player: Player) -> tk.Frame:
    global frame
    # general button frame to hold the ff btn: [status, quit]
    buttonframe = tk.Frame(frame)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    # Create a button widget
    pl_status = tk.Button(buttonframe, text="Status", command=lambda: show_player_status(player))
    pl_status.grid(row=0, column=0, sticky=tk.W+tk.E)
    return buttonframe

# general button frame
generalbuttonframe1 = create_general_btns(player1)
generalbuttonframe1.place(x=50, y=200)

generalbuttonframe2 = create_general_btns(player2)
generalbuttonframe2.place(x=530, y=200)


def create_skills_btns(current_player: Player, enemy_player: Player) -> tk.Frame:
    global frame
    # Active skills button frame
    active_skill_btns = tk.Frame(frame)
    active_skill_btns.rowconfigure(0, weight=1)
    # warrior
    warrior_btn = tk.Button(active_skill_btns, text="slash", command=lambda: current_player.use_skill("slash", enemy_player))
    warrior_btn.grid(row=0, column=0, sticky=tk.W+tk.E)
    # assasin
    assasin_btn = tk.Button(active_skill_btns, text="stab", command=lambda: current_player.use_skill("stab", enemy_player))
    assasin_btn.grid(row=0, column=1, sticky=tk.W+tk.E)
    # mage
    mage_btn = tk.Button(active_skill_btns, text="fireball", command=lambda: current_player.use_skill("fireball", enemy_player))
    mage_btn.grid(row=0, column=2, sticky=tk.W+tk.E)
    return active_skill_btns

active_skills_1 = create_skills_btns(player1, player2)
active_skills_1.place(x=50, y=250)

active_skills_2 = create_skills_btns(player2, player1)
active_skills_2.place(x=530, y=250)


def main() -> None:
    print("""game start""")
    root.mainloop()

if __name__ == "__main__":
    main()
