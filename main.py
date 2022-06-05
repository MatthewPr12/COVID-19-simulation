"""
main module that holds constants
"""
from society import Society

data = {"young": 1, "old": 0.75, "female": 1,
        "male": 0.8, "T1": 10, "T2": 4, "T3": 4,
        "T4": 7, "T5": 120, "u": 0.2,
        "k": 0.33, 'init_infected': 0.001}

soc = Society(200, 200, 1, data)
