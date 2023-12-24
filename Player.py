import os
import random
import json
from dataclasses import dataclass, field
from typing import List, Optional


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

    def use_skill(self, type_of_skill: str, enemy_player: Optional['Player'] = None) -> None:
        if type_of_skill == "active":
            pass
