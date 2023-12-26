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

    def use_skill(self, type_of_skill: str, enemy_player: Optional['Player'] = None) -> None:
        if type_of_skill == "active":
            pass
