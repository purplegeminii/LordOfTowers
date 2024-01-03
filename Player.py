import os
import random
import json
from dataclasses import dataclass, field
from typing import List, Optional, Dict
import tkinter as tk


data = open(os.path.join("Asserts/Data", "job_class.json"))
loaded_data: List[Dict] = json.load(data)
jobs: List[str] = [job['job_name'] for job in loaded_data]

def assign_job() -> str:
    return "".join(random.choice(jobs))

def assign_random_multiplier() -> float:
    multipliers = [1.0, 1.1, 1.2, 1.3, 2.0]
    weights = [20, 31, 23, 25, 1]  # Adjust these weights based on the desired probability

    # Ensure the sum of weights is equal to 100 or use total sum as the reference
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]

    chosen_multiplier = random.choices(multipliers, weights=normalized_weights, k=1)
    return chosen_multiplier[0]


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
        self.health_bar = round([x['init_health'] for x in loaded_data if x['job_name']==self.job_class][0] * assign_random_multiplier())
        self.base_hp = self.health_bar
        self.mana_bar = round([x['init_mana'] for x in loaded_data if x['job_name']==self.job_class][0] * assign_random_multiplier())
        self.base_mp = self.mana_bar

        health_growth_rate = 8
        mana_growth_rate = 12

        health_multiplier = 1 + (self.level * health_growth_rate / 100)
        mana_multiplier = 1 + (self.level * mana_growth_rate / 100)

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

        player_status.create_text(90, 180, text="Combat Power:", fill="blue", font=('Arial', 16))
        player_status.create_text(100, 200, text=str(self.combat_power), fill="blue", font=('Arial', 16))

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

        self.auto_regen_mp()

    
    def update_health_bar(self) -> None:
        self.health_value = self.health_bar/self.base_hp * 100
        self.hp_canvas.delete(self.health_bar_gui)
        self.health_bar_gui = self.hp_canvas.create_rectangle(0, 0, (self.health_value) * 2, 30, fill="green")
        print(f"{self.__class__.__name__} class method: update HP")

    def update_mana_bar(self) -> None:
        self.mana_value = self.mana_bar/self.base_mp * 100
        self.mp_canvas.delete(self.mana_bar_gui)
        self.mana_bar_gui = self.mp_canvas.create_rectangle(0, 0, (self.mana_value) * 2, 30, fill="blue")
        print(f"{self.__class__.__name__} class method: update MP")

    def auto_regen_mp(self, mana_regen_rate: int = 50) -> None:
        # Assuming a mana regeneration rate of 50 units per 10 seconds
        regen_interval_ms = 10000  # Milliseconds (10 sec)

        if self.mana_bar < self.base_mp:
            print(f"{self.__class__.__name__} class method: auto_regen_mp")
            self.mana_bar = min(self.mana_bar + mana_regen_rate, self.base_mp)
            self.update_mana_bar()  # Update the mana bar GUI here
        
        # Schedule the next regeneration
        self.hp_mp_bars.after(regen_interval_ms, lambda: self.auto_regen_mp(mana_regen_rate))

    def receive_damage(self, damage: float) -> None:
        self.health_bar -= damage
        self.update_health_bar()
        print(f"{self.name} received {damage} damage!")

    def use_skill(self, name_of_skill: str, enemy_player: Optional['Player'] = None) -> None:
        # Check if the skill exists in the loaded_data
        skill_exists = any(
            job.get('job_name') == self.job_class and any(skill['skill_name'] == name_of_skill for skill in job['active_skill'] + job['passive_skill'])
            for job in loaded_data
        )

        if skill_exists:
            # Find the skill within the loaded_data for the player's job class
            job_skills = next(job for job in loaded_data if job['job_name'] == self.job_class)
            skill = next((s for s in job_skills['active_skill'] + job_skills['passive_skill'] if s['skill_name'] == name_of_skill), None)

            if skill:
                print(f"{self.__class__.__name__} class method: use_skill")
                # Determine if the skill is active or passive
                is_active = skill['skill_type'] == 'active'

                # Perform actions based on whether the skill is active or passive
                if is_active:
                    # Placeholder logic for an active skill
                    if enemy_player:
                        # Placeholder damage calculation for demonstration purposes
                        damage = int(eval(skill['skill_damage'].format(skill_level=skill['skill_level'])))
                        mana_cost = int(eval(skill['skill_mana_cost'].format(skill_level=skill['skill_level'])))
                        # Check if the player has enough mana to use the skill
                        if self.mana_bar >= mana_cost:
                            self.mana_bar -= mana_cost
                            print(f"{mana_cost} mana used to activate {name_of_skill} skill")
                            self.update_mana_bar()
                            enemy_player.receive_damage(damage)
                            print(f"{self.name} used {name_of_skill} on {enemy_player.name}!")

                        else:
                            print(f"{self.name} doesn't have enough mana to use {name_of_skill}!")

                else:
                    # Placeholder logic for a passive skill (if any)
                    print(f"{self.name} used {name_of_skill} (passive skill)!")
