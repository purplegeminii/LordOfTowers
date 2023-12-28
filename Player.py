import os
import random
import json
from dataclasses import dataclass, field
from typing import List, Optional
import tkinter as tk


data = open(os.path.join("Asserts/Data", "job_class.json"))
loaded_data = json.load(data)
jobs: List[str] = [job['job_name'] for job in loaded_data]

def assign_job() -> str:
    return "".join(random.choice(jobs))


@dataclass
class Player:
    
    name: str
    level: int = 1
    job_class: str = field(init=False, default_factory=assign_job)
    health_bar: float = field(init=False)
    mana_bar: float = field(init=False)
    base_hp: float = field(init=False)
    base_mp: float = field(init=False)
    combat_power: float = field(init=False)

    hp_mp_bars: tk.Frame = field(init=False, repr=False)
    hp_canvas: tk.Canvas = field(init=False, repr=False)
    health_value: float = field(init=False, repr=False)
    health_bar_gui: int = field(init=False, repr=False)
    mp_canvas: tk.Canvas = field(init=False, repr=False)
    mana_value: float = field(init=False, repr=False)
    mana_bar_gui: int = field(init=False, repr=False)

    def __post_init__(self):
        self.health_bar = [x['init_health'] for x in loaded_data if x['job_name']==self.job_class][0]
        self.base_hp = self.health_bar
        self.mana_bar = [x['init_mana'] for x in loaded_data if x['job_name']==self.job_class][0]
        self.base_mp = self.mana_bar
        health_multiplier = 2/3
        mana_multiplier = 3
        self.combat_power = round(((health_multiplier)*(self.health_bar))+((mana_multiplier)*(self.mana_bar)), 2)

    def get_player_status(self, frame: tk.Frame) -> tk.Canvas:
        player_status = tk.Canvas(frame, width=200, height=300, bg="red")
        player_status.create_text(100, 30, text="Player Status", fill="blue", font=('Arial', 18))

        player_status.create_text(60, 60, text="Name:", fill="blue", font=('Arial', 16))
        player_status.create_text(140, 60, text=self.name.split(" ")[0], fill="blue", font=('Arial', 16))

        player_status.create_text(60, 80, text="Level:", fill="blue", font=('Arial', 16))
        player_status.create_text(140, 80, text=str(self.level), fill="blue", font=('Arial', 16))

        player_status.create_text(60, 100, text="Job:", fill="blue", font=('Arial', 16))
        player_status.create_text(140, 100, text=self.job_class, fill="blue", font=('Arial', 16))

        hp = str(self.health_bar)+"/"+str(self.base_hp)
        player_status.create_text(60, 120, text="HP:", fill="blue", font=('Arial', 16))
        player_status.create_text(140, 120, text=hp, fill="blue", font=('Arial', 16))

        mp = str(self.mana_bar)+"/"+str(self.base_mp)
        player_status.create_text(60, 140, text="MP:", fill="blue", font=('Arial', 16))
        player_status.create_text(140, 140, text=mp, fill="blue", font=('Arial', 16))

        return player_status
    
    def create_hp_mp_bars(self, frame: tk.Frame) -> None:
        self.hp_mp_bars = tk.Frame(frame)
        self.hp_mp_bars.rowconfigure(0, weight=1)
        self.hp_mp_bars.rowconfigure(1, weight=1)

        self.hp_canvas = tk.Canvas(self.hp_mp_bars, width=200, height=30, bg="red")
        self.hp_canvas.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.health_value = self.health_bar/self.base_hp * 100
        self.health_bar_gui = self.hp_canvas.create_rectangle(0, 0, self.health_value * 2, 30, fill="green")

        self.mp_canvas = tk.Canvas(self.hp_mp_bars, width=200, height=30, bg="white")
        self.mp_canvas.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.mana_value = self.mana_bar/self.base_mp * 100
        self.mana_bar_gui = self.mp_canvas.create_rectangle(0, 0, self.mana_value * 2, 30, fill="blue")

    
    def update_health_bar(self) -> None:
        self.health_bar -= 40
        self.health_value = self.health_bar/self.base_hp * 100
        self.hp_canvas.delete(self.health_bar_gui)
        self.health_bar_gui = self.hp_canvas.create_rectangle(0, 0, (self.health_value) * 2, 30, fill="green")
        print("player class method: update HP")

    def update_mana_bar(self) -> None:
        self.mana_bar -= 40
        self.mana_value = self.mana_bar/self.base_mp * 100
        self.mp_canvas.delete(self.mana_bar_gui)
        self.mana_bar_gui = self.mp_canvas.create_rectangle(0, 0, (self.mana_value) * 2, 30, fill="blue")
        print("player class method: update MP")

    def use_skill(self, type_of_skill: str, enemy_player: Optional['Player'] = None) -> None:
        if type_of_skill == "active":
            pass
