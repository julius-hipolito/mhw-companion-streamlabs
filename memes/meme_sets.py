import random
from . import sets
from mhwdata import weapons


def getMemeSet(weapon):
    if weapon.lower() == "any" or weapon == "":
        try:
            return random.choice(sets.getAll())
        except:
            return ""
    else:
        try:
            return random.choice(sets.sets[weapon.lower()])
        except:
            return ""
    return