from src.dnddb import DndDB
import pprint

x = DndDB()
pprint.pprint(x.damage_types)
x.reload()
