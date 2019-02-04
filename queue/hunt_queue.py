import Queue
import random


from collections import deque
from settings.settings import weapons, monsters


class HuntQueue:
	def __init__(self, maxsize):
		self.__huntQueue = Queue.Queue(maxsize=maxsize)
		self.__recentMonsters = deque(maxlen=10)
		self.__recentWeapons = deque(maxlen=5)
		self.__currentHunt = None

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
		monster = monster if monster else \
			random.choice([monster for monster in monsters if monster not in self.__recentMonsters])
		weapon = weapon if weapon else \
			random.choice([weapon for weapon in weapons if weapon not in self.__recentWeapons])

		self.__huntQueue.put(HuntData(username, user, weapon, monster))
		self.__recentMonsters.append(monster)
		self.__recentWeapons.append(weapon)

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
