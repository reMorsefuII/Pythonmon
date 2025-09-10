import numpy
import random

names = ["TestMon1"]

moves = [
    {
        "Name": "TestMove1",
        "Power": 15,
        "Accuracy": 100
    },
    {
        "Name": "TestMove2",
        "Power": 25,
        "Accuracy": 90
    },
    {
        "Name": "TestMove3",
        "Power": 20,
        "Accuracy": 95
    },
    {
        "Name": "TestMove4",
        "Power": 50,
        "Accuracy": 60
    },
    {
        "Name": "TestMove5",
        "Power": 70,
        "Accuracy": 30
    }
]
movesets = {
    "TestMon1": [moves[0], moves[1], moves[2], moves[3], moves[4]],
}

healthRanges = {
    "TestMon1": [100, 120]
}

class Entity:
    def __init__(self, name):
        self.Name = name
        permutation = numpy.random.permutation(movesets[name])
        self.Moves = [permutation[0], permutation[1], permutation[2], permutation[3]]
        self.MaxHealth = random.randint(healthRanges["TestMon1"][0], healthRanges["TestMon1"][1])
        self.Health = self.MaxHealth
    def __str__(self):
        return f'Name: {self.Name}, MaxHealth: {self.MaxHealth}, Health: {self.Health}\nMoves: {self.Moves}'
    def takeDamage(self, move):
        if random.random() < (move["Accuracy"]/100):
            print("Accuracy check complete")
            self.Health -= move["Power"]
            return True
            #Add Pythonmon type checks soon?
        else:
            return False