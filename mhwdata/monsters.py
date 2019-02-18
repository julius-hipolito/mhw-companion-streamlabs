import json
import os
import codecs


__enabledMonsterRollIds = []
__enabledMonsterRequestIds = []
__idToMonsterData = {}
__lowerValidNamesToId = {}


HUNT_TYPE_ROLL = "Roll"
HUNT_TYPE_REQUEST = "Request"


def initialize_monster_data():
	global __idToMonsterData
	global __lowerValidNamesToId
	global __enabledMonsterRollIds
	global __enabledMonsterRequestIds

	__idToMonsterData.clear()
	__lowerValidNamesToId.clear()
	del __enabledMonsterRollIds[:]
	del __enabledMonsterRequestIds[:] 

	__monsterDataArray = []

	path = os.path.dirname(__file__)
	with codecs.open(os.path.join(path, "monsters.json"), encoding='utf-8-sig', mode='r') as file:
		__monsterDataArray = json.load(file, encoding='utf-8-sig')

	for dataSet in __monsterDataArray:
		
		# Populate Monster Data Dictionary ID to Data Model
		__idToMonsterData[dataSet["id"]] = dataSet

		# Populate Lower Valid Names to ID
		displayNameLower = dataSet["displayName"].lower()
		if displayNameLower in __lowerValidNamesToId.keys():
			# TODO - Throw valid exception of duplicate names being used for multiple monsters.
			raise Exception("Duplicate string name for monsters found! " + displayNameLower)
		else:
			__lowerValidNamesToId[displayNameLower] = dataSet["id"]
		
		if dataSet["validNames"] != None and len(dataSet["validNames"]) > 0:
			# Add additional names to the Lower Valid Names to ID map. Check for duplicates.
			for extraName in dataSet["validNames"]:
				extraNameLower = extraName.lower()
				if extraNameLower in __lowerValidNamesToId.keys():
					raise Exception("Duplicate string name for monsters found! " + displayNameLower)
				else:
					__lowerValidNamesToId[extraNameLower] = dataSet["id"]

	return


# Returns the display name of a valid monster that is found. Otherwise None is returned.
def validate_name(name, huntType):
	global __lowerValidNamesToId
	global __enabledMonsterRollIds
	global __enabledMonsterRequestIds
	global __idToMonsterData

	lowerName = name.lower()
	
	matchingId = __lowerValidNamesToId.get(lowerName)

	if matchingId is None:
		return None

	isAllowed = False
	if huntType == HUNT_TYPE_ROLL:
		isAllowed = matchingId in __enabledMonsterRollIds
	elif huntType == HUNT_TYPE_REQUEST:
		isAllowed = matchingId in __enabledMonsterRequestIds
	else:
		raise Exception("Invalid HuntType passed! " + huntType)

	if isAllowed:
		return __idToMonsterData[matchingId].get("displayName")
	else:
		return None


def add_monster_to_enabled_rolls(name):
	global __lowerValidNamesToId
	global __enabledMonsterRollIds
	matchingId = __lowerValidNamesToId.get(name.lower())
	if matchingId is None:
		raise Exception("NO MATCHING ID FOR: " + name)

	__enabledMonsterRollIds.append(matchingId)
	return


def add_monster_to_enabled_requests(name):
	global __lowerValidNamesToId
	global __enabledMonsterRequestIds
	matchingId = __lowerValidNamesToId.get(name.lower())
	if matchingId is None:
		raise Exception("NO MATCHING ID FOR: " + name)

	__enabledMonsterRequestIds.append(matchingId)
	return


def get_monster_names_for_roll():
	global __enabledMonsterRollIds
	global __idToMonsterData
	monsterNames = []
	for monsterId in __enabledMonsterRollIds:
		monsterNames.append(__idToMonsterData[monsterId].get("displayName"))

	return monsterNames


def get_monster_roll_count():
	global __enabledMonsterRollIds
	return len(__enabledMonsterRollIds)