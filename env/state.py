from dataclasses import dataclass
from typing import List, Dict
import random

@dataclass
class UserState:
    user_embedding: List[float]
    history: List[int]
    interest: float
    fatigue: float
    value_pref: Dict[str, float]

def init_user():
    return UserState(
        user_embedding=[random.random() for _ in range(8)],
        history=[],
        interest=random.uniform(0.4, 0.8),
        fatigue=0.1,
        value_pref={"caring": 0.7, "toxicity_tolerance": 0.2}
    )