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
player1.create_hp_mp_bars(frame)
hp_mp_bars = player1.hp_mp_bars
hp_mp_bars.place(x=25, y=50)

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
update_hp_btn = tk.Button(buttonframe, text="Update HP", command=player1.update_health_bar)
update_hp_btn.grid(row=1, column=0, sticky=tk.W+tk.E)

# Update mana button
update_mp_btn = tk.Button(buttonframe, text="Update MP", command=player1.update_mana_bar)
update_mp_btn.grid(row=1, column=1, sticky=tk.W+tk.E)


def main() -> None:
    print("""game start""")
    root.mainloop()

if __name__ == "__main__":
    main()
