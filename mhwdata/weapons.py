import json
import os
import codecs


__enabledWeaponRollIds = []
__enabledWeaponRequestIds = []
__idToWeaponData = {}
__lowerValidNamesToId = {}


HUNT_TYPE_ROLL = "Roll"
HUNT_TYPE_REQUEST = "Request"


def initialize_weapon_data():
	global __idToWeaponData
	global __lowerValidNamesToId
	global __enabledWeaponRollIds
	global __enabledWeaponRequestIds

	__idToWeaponData.clear()
	__lowerValidNamesToId.clear()
	del __enabledWeaponRequestIds[:]
	del __enabledWeaponRollIds[:]

	__weaponDataArray = []

	path = os.path.dirname(__file__)
	with codecs.open(os.path.join(path, "weapons.json"), encoding='utf-8-sig', mode='r') as file:
		__weaponDataArray = json.load(file, encoding='utf-8-sig')

	for dataSet in __weaponDataArray:
		
		# Populate Weapon Data Dictionary ID to Data Model
		__idToWeaponData[dataSet["id"]] = dataSet

		# Populate Lower Valid Names to ID
		displayNameLower = dataSet["displayName"].lower()
		if displayNameLower in __lowerValidNamesToId.keys():
			# TODO - Throw valid exception of duplicate names being used for multiple weapons.
			raise Exception("Duplicate string name for weapons found! " + displayNameLower)
		else:
			__lowerValidNamesToId[displayNameLower] = dataSet["id"]
		
		if dataSet["validNames"] != None and len(dataSet["validNames"]) > 0:
			# Add additional names to the Lower Valid Names to ID map. Check for duplicates.
			for extraName in dataSet["validNames"]:
				extraNameLower = extraName.lower()
				if extraNameLower in __lowerValidNamesToId.keys():
					raise Exception("Duplicate string name for weapons found! " + displayNameLower)
				else:
					__lowerValidNamesToId[extraNameLower] = dataSet["id"]

	return


# Returns the display name of a valid weapon that is found. Otherwise None is returned.
def validate_name(name, huntType):
	global __lowerValidNamesToId
	global __enabledWeaponRollIds
	global __enabledWeaponRequestIds
	global __idToWeaponData

	lowerName = name.lower()
	
	matchingId = __lowerValidNamesToId.get(lowerName)

	if matchingId is None:
		return None

	isAllowed = False
	if huntType == HUNT_TYPE_ROLL:
		isAllowed = matchingId in __enabledWeaponRollIds
	elif huntType == HUNT_TYPE_REQUEST:
		isAllowed = matchingId in __enabledWeaponRequestIds
	else:
		raise Exception("Invalid HuntType passed! " + huntType)

	if isAllowed:
		return __idToWeaponData[matchingId].get("displayName")
	else:
		return None


def add_weapon_to_enabled_rolls(name):
	global __lowerValidNamesToId
	global __enabledWeaponRollIds
	matchingId = __lowerValidNamesToId.get(name.lower())
	if matchingId is None:
		raise Exception("NO MATCHING ID FOR: " + name)

	__enabledWeaponRollIds.append(matchingId)
	return


def add_weapon_to_enabled_requests(name):
	global __enabledWeaponRequestIds
	global __lowerValidNamesToId
	matchingId = __lowerValidNamesToId.get(name.lower())
	if matchingId is None:
		raise Exception("NO MATCHING ID FOR: " + name)

	__enabledWeaponRequestIds.append(matchingId)
	return


def get_weapon_names_for_roll():
	global __enabledWeaponRollIds
	global __idToWeaponData
	weaponNames = []
	for weaponId in __enabledWeaponRollIds:
		weaponNames.append(__idToWeaponData[weaponId].get("displayName"))

	return weaponNames


def get_weapon_roll_count():
	global __enabledWeaponRollIds
	return len(__enabledWeaponRollIds)