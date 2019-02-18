import Queue
import random
import uuid


from collections import deque
from mhwdata import weapons
from mhwdata import monsters


class HuntQueue:
	def __init__(self, maxsize, weaponsRollCount, monstersRollCount):
		weaponCount = max(min(weaponsRollCount-2, 100), 1)
		monsterCount = max(min(monstersRollCount-2, 100), 1)

		self.__huntQueue = Queue.Queue(maxsize=maxsize)
		self.__recentWeapons = deque(maxlen=weaponCount)
		self.__recentMonsters = deque(maxlen=monsterCount)
		self.__currentHunt = None
		self.__random = random.Random(uuid.uuid1().int)

	def is_empty(self):
		return self.__huntQueue.empty()

	def next_hunt(self):
		try:
			self.__currentHunt = self.__huntQueue.get()
		except Empty:
			# Catch Empty exception if attempting .get() on an empty queue.
			self.__currentHunt = None
		return self.__currentHunt

	def current_hunt(self):
		return self.__currentHunt

	def is_full(self):
		return self.__huntQueue.full()

	def add_hunt(self, username, user, weapon=None, monster=None):
		if monster is None:
			monster = self.roll_monster()

		if weapon is None:
			weapon = self.roll_weapon()

		self.__huntQueue.put(HuntData(username, user, weapon, monster))
		self.__recentMonsters.append(monster)
		self.__recentWeapons.append(weapon)

		return weapon, monster

	def roll_monster(self):
		rollableMonsters = monsters.get_monster_names_for_roll()
		monster = "Any"
		if len(rollableMonsters) == 0:
			return monster
		elif len(rollableMonsters) == 1:
			monster = rollableMonsters[0]
		else:
			monster = monster if monster else \
				self.__random.choice([monster for monster in rollableMonsters if monster not in self.__recentMonsters])
		return monster

	def roll_weapon(self):
		rollableWeapons = weapons.get_weapon_names_for_roll()
		weapon = "Any"
		if len(rollableWeapons) == 0:
			return weapon
		elif len(rollableWeapons) == 1:
			weapon = rollableWeapons[0]
		else:
			weapon = weapon if weapon else \
				self.__random.choice([weapon for weapon in rollableWeapons if weapon not in self.__recentWeapons])
		return weapon				


# ---------------------------
# Hunt Data Model
# ---------------------------
class HuntData:
	def __init__(self, username, user, weapon, monster):
		self.username = username
		self.user = user
		self.weapon = weapon
		self.monster = monster
