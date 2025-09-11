import numpy
import random

from pygame.math import clamp

names = ["Snoop Dogg", "Snoop Frog", "Python"]

moves = [
    { #0
        "Name": "B*tch Slap",
        "Power": 15,
        "Accuracy": 100
    },
    { #1
        "Name": "Hard Punch",
        "Power": 25,
        "Accuracy": 90
    },
    { #2
        "Name": "Right Cross",
        "Power": 20,
        "Accuracy": 95
    },
    { #3
        "Name": "Iron Fist",
        "Power": 50,
        "Accuracy": 60
    },
    { #4
        "Name": "Body Slam",
        "Power": 70,
        "Accuracy": 30
    },
    { #5
        "Name": "Snakebite",
        "Power": 30,
        "Accuracy": 85
    },
    { #6
        "Name": "Draconic Roar",
        "Power": 25,
        "Accuracy": 100
    },
]
movesets = {
    "Snoop Dogg": [moves[0], moves[1], moves[2], moves[3], moves[4]],
    "Snoop Frog": [moves[0], moves[1], moves[2], moves[3], moves[4]],
    "Python": [moves[0], moves[2], moves[5], moves[6], moves[4]],
}

healthRanges = {
    "Snoop Dogg": [100, 120],
    "Snoop Frog": [90, 150],
    "Python": [75, 100],
}

class Entity:
    def __init__(self, name):
        self.Name = name
        permutation = numpy.random.permutation(movesets[name])
        self.Moves = [permutation[0], permutation[1], permutation[2], permutation[3]]
        self.MaxHealth = random.randint(healthRanges[name][0], healthRanges[name][1])
        self.Health = self.MaxHealth
    def __str__(self):
        return f'Name: {self.Name}, MaxHealth: {self.MaxHealth}, Health: {self.Health}\nMoves: {self.Moves}'
    def takeDamage(self, move):
        if random.random() < (move["Accuracy"]/100):
            print("Accuracy check complete")
            self.Health -= move["Power"]
            self.Health = clamp(self.Health, 0, self.MaxHealth)
            print(self.Health)
            print("Health taken")
            return True
            #Add Pythonmon type checks soon?
        else:
            return False