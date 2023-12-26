from Player import Player
import tkinter as tk
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
    health_value = player1.health_bar/player1.base_hp * 100
    hp_canvas.delete(health_bar)
    # to-do: remove the "-40"
    health_bar = hp_canvas.create_rectangle(0, 0, (health_value-40) * 2, 30, fill="green")

def greet() -> None:
    print("Button Clicked!")

# Create a button widget
btn1 = tk.Button(frame, text="Button", command=greet)
btn1.grid(column=0, row=2)

# Quit btn
quitbtn = tk.Button(frame, text="Quit", command=root.destroy)
quitbtn.grid(column=1, row=2)

# Update health button
update_hp_btn = tk.Button(frame, text="Update HP", command=update_health_bar)
update_hp_btn.grid(column=0, row=3)

def main() -> None:
    print("""game start""")
    root.mainloop()

if __name__ == "__main__":
    main()
