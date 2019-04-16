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
		self.__maxCount = maxsize
		self.__huntQueue = deque(maxlen=maxsize)
		self.__recentWeapons = deque(maxlen=weaponCount)
		self.__recentMonsters = deque(maxlen=monsterCount)
		self.__currentHunt = None
		self.__random = random.Random()

	def is_empty(self):
		if self.__huntQueue:
			return False
		else:
			return True

	def next_hunt(self):
		try:
			self.__currentHunt = self.__huntQueue.popleft()
		except Empty:
			# Catch Empty exception if attempting .get() on an empty queue.
			self.__currentHunt = None
		return self.__currentHunt

	def current_hunt(self):
		return self.__currentHunt

	def is_full(self):
		return len(self.__huntQueue) == self.__maxCount

	def add_hunt(self, username, user, weapon=None, monster=None):
		if monster is None:
			monster = self.roll_monster()

		if weapon is None:
			weapon = self.roll_weapon()

		self.__huntQueue.append(HuntData(username, user, weapon, monster))
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
			monster = self.__random.choice([monster for monster in rollableMonsters if monster not in self.__recentMonsters])
		return monster

	def roll_weapon(self):
		rollableWeapons = weapons.get_weapon_names_for_roll()
		weapon = "Any" + str(len(rollableWeapons))
		if len(rollableWeapons) == 0:
			return weapon
		elif len(rollableWeapons) == 1:
			weapon = rollableWeapons[0]
		else:
			weapon = self.__random.choice([weapon for weapon in rollableWeapons if weapon not in self.__recentWeapons])
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
