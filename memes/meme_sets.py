import random
from . import sets
from settings.settings import weapons_short
def getMemeSet(weapon):
    if weapon.lower() in weapons_short:
        try:
            return random.choice(sets.sets[weapon])
        except:
            return ""
    elif weapon.lower()=="all" or weapon == "":
        try:
            return random.choice(sets.getAll())
        except:
            return ""
    return

def saveSet(hh_url):
    if check_valid_hh_url(url):
        pass
    else:
        pass
