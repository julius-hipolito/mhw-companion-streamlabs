import Queue
import random

from collections import deque
from settings.settings import weapons, monsters


class HuntQueue:
    def __init__(self, maxsize):
        self.huntQueue = Queue.Queue(maxsize=maxsize)
        self.recentMonsters = deque(maxlen=10)
        self.recentWeapons = deque(maxlen=5)

    def empty(self):
        return self.huntQueue.empty()

    def get(self):
        return self.huntQueue.get()

    def full(self):
        return self.huntQueue.full()

    def add_hunt(self, username, user, weapon=None, monster=None):
        monster = monster if monster else \
            random.choice([monster for monster in monsters if monster not in self.recentMonsters])
        weapon = weapon if weapon else \
            random.choice([weapon for weapon in weapons if weapon not in self.recentWeapons])

        self.huntQueue.put(HuntData(username, user, weapon, monster))
        self.recentMonsters.append(monster)
        self.recentWeapons.append(weapon)

        return weapon, monster


# ---------------------------
# Hunt Data Model
# ---------------------------
class HuntData:
    def __init__(self, username, user, weapon, monster):
        self.username = username
        self.user = user
        self.weapon = weapon
        self.monster = monster
