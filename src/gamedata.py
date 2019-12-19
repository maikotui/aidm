import json

class gamedata:
    def __init__(self):
        self.value = -1

x = gamedata()
with open("data/games/gamedata.json", "w") as write_file:
    json.dump(x.__dict__, write_file)
