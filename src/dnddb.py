import json
import os
from collections import namedtuple


class DndDB:
    def __init__(self):
        self.ability_scores = self.importjson("data/5e-SRD-Ability-Scores.json")
        self.classes = self.importjson("data/5e-SRD-Classes.json")
        self.conditions = self.importjson("data/5e-SRD-Conditions.json")
        self.damage_types = self.importjson("data/5e-SRD-Damage-Types.json")
        self.equipment = self.importjson("data/5e-SRD-Equipment.json")
        self.equipment_categories = self.importjson("data/5e-SRD-Equipment-Categories.json")
        self.features = self.importjson("data/5e-SRD-Features.json")
        self.languages = self.importjson("data/5e-SRD-Languages.json")
        self.levels = self.importjson("data/5e-SRD-Levels.json")
        self.magic_schools = self.importjson("data/5e-SRD-Magic-Schools.json")
        self.monsters = self.importjson("data/5e-SRD-Monsters.json")
        self.proficiencies = self.importjson("data/5e-SRD-Proficiencies.json")
        self.races = self.importjson("data/5e-SRD-Races.json")
        self.skills = self.importjson("data/5e-SRD-Skills.json")
        self.spellcasting = self.importjson("data/5e-SRD-Spellcasting.json")
        self.spells = self.importjson("data/5e-SRD-Spells.json")
        self.starting_equipment = self.importjson("data/5e-SRD-Starting-Equipment.json")
        self.subclasses = self.importjson("data/5e-SRD-Subclasses.json")
        self.subraces = self.importjson("data/5e-SRD-Subraces.json")
        self.test = self.importjson("data/5e-SRD-Test.json")
        self.traits = self.importjson("data/5e-SRD-Traits.json")
        self.weapon_properties = self.importjson("data/5e-SRD-Weapon-Properties.json")

    @staticmethod
    def importjson(fname):
        with open(fname) as json_file:
            data = json.load(json_file)
            jsonobj = json.loads(json.dumps(data), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            print("Successfully loaded " + fname)
            return jsonobj
