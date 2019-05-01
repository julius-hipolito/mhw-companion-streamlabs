# ---------------------------
# Import Libraries
# ---------------------------
import json
import os
import codecs
import sys


# ---------------------------
# Import any custom modules under the "sys.path.append(os.path.dirname(__file__))" line
# Required for importing modules from the main scripts directory
# StreamLabs Thread: https://ideas.streamlabs.com/ideas/SL-I-3971
# ---------------------------
sys.path.append(os.path.dirname(__file__))
from memes.meme_sets import getMemeSet
from queue.hunt_queue import HuntQueue
from queue.hunt_queue import HuntData
from mhwdata import weapons
from mhwdata import monsters


# ---------------------------
# [Required] Script Information
# ---------------------------
ScriptName = "MHW Companion"
Website = "https://github.com/Vizionz/mhw-companion-streamlabs"
Description = "Monster Hunter World Companion for StreamLabs ChatBot"
Creator = "Level Headed Gamers"
Version = "0.1.0"


# ---------------------------
# Define Global Variables
# ---------------------------
configFile = "config.json"
settings = {}

huntQueue = None


# ---------------------------
# [Required] Initialize Data (Only called on load)
# ---------------------------
def Init():
	global settings
	global huntQueue

	path = os.path.dirname(__file__)
	try:
		with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
			settings = json.load(file, encoding='utf-8-sig')
	except:
		settings = {
			"queueRandomHuntSetupCommand": "!mhw-qhunt-roll",
			"queueRandomHuntSetupCommandPermission": "Everyone",
			"queueGetNextHuntCommand": "!mhw-nhunt",
			"queueGetNextHuntCommandPermission": "Everyone",
			"currentHuntCommand": "!mhw-hunt",
			"currentHuntCommandPermission": "Everyone",
			"huntRollCommand": "!mhw-hunt-random",
			"huntRollCommandPermission": "Everyone",
			"weaponCommand": "!mhw-weapon-roll",
			"weaponCommandPermission": "Everyone",
			"monsterCommand": "!mhw-monster-roll",
			"monsterCommandPermission": "Everyone",
			"memeSetCommand": "!mhw-meme-set-roll",
			"memeSetCommandPermission": "Everyone",
			"whisperCommandsCommand": "!mhw-commands",
			"whisperCommandsCommandPermission": "Everyone",
			"queueCustomHuntCommand": "!mhw-hunt-custom",
			"queueCustomHuntCommandPermission": "Everyone",
			"huntQueueSize": 10,
			"enableWeaponAnyRoll": True,
			"enableWeaponAnyRequest": True,
			"enableWeaponInsectGlaiveRoll": True,
			"enableWeaponInsectGlaiveRequest": True,
			"enableWeaponChargeBladeRoll": True,
			"enableWeaponChargeBladeRequest": True,
			"enableWeaponSwitchAxeRoll": True,
			"enableWeaponSwitchAxeRequest": True,
			"enableWeaponBowRoll": True,
			"enableWeaponBowRequest": True,
			"enableWeaponLightBowgunRoll": True,
			"enableWeaponLightBowgunRequest": True,
			"enableWeaponHeavyBowgunRoll": True,
			"enableWeaponHeavyBowgunRequest": True,
			"enableWeaponHammerRoll": True,
			"enableWeaponHammerRequest": True,
			"enableWeaponHuntingHornRoll": True,
			"enableWeaponHuntingHornRequest": True,
			"enableWeaponLongSwordRoll": True,
			"enableWeaponLongSwordRequest": True,
			"enableWeaponSwordShieldRoll": True,
			"enableWeaponSwordShieldRequest": True,
			"enableWeaponLanceRoll": True,
			"enableWeaponLanceRequest": True,
			"enableWeaponGunlanceRoll": True,
			"enableWeaponGunlanceRequest": True,
			"enableWeaponGreatSwordRoll": True,
			"enableWeaponGreatSwordRequest": True,
			"enableWeaponDualBladesRoll": True,
			"enableWeaponDualBladesRequest": True,
			"enableMonsterAnyRoll": True,
			"enableMonsterAnyRequest": True,
			"enableMonsterTeostraRoll": True,
			"enableMonsterTeostraRequest": True,
			"enableMonsterLunastraRoll": True,
			"enableMonsterLunastraRequest": True,
			"enableMonsterKirinRoll": True,
			"enableMonsterKirinRequest": True,
			"enableMonsterNergiganteRoll": True,
			"enableMonsterNergiganteRequest": True,
			"enableMonsterVaalHazakRoll": True,
			"enableMonsterVaalHazakRequest": True,
			"enableMonsterKushalaDaoraRoll": True,
			"enableMonsterKushalaDaoraRequest": True,
			"enableMonsterKulveTarothRoll": True,
			"enableMonsterKulveTarothRequest": True,
			"enableMonsterXenojiivaRoll": True,
			"enableMonsterXenojiivaRequest": True,
			"enableMonsterBehemothRoll": True,
			"enableMonsterBehemothRequest": True,
			"enableMonsterRathalosRoll": True,
			"enableMonsterRathalosRequest": True,
			"enableMonsterAzureRathalosRoll": True,
			"enableMonsterAzureRathalosRequest": True,
			"enableMonsterRathianRoll": True,
			"enableMonsterRathianRequest": True,
			"enableMonsterPinkRathianRoll": True,
			"enableMonsterPinkRathianRequest": True,
			"enableMonsterDiablosRoll": True,
			"enableMonsterDiablosRequest": True,
			"enableMonsterBlackDiablosRoll": True,
			"enableMonsterBlackDiablosRequest": True,
			"enableMonsterBazelgeuseRoll": True,
			"enableMonsterBazelgeuseRequest": True,
			"enableMonsterUragaanRoll": True,
			"enableMonsterUragaanRequest": True,
			"enableMonsterLavasiothRoll": True,
			"enableMonsterLavasiothRequest": True,
			"enableMonsterLegianaRoll": True,
			"enableMonsterLegianaRequest": True,
			"enableMonsterOdogaronRoll": True,
			"enableMonsterOdogaronRequest": True,
			"enableMonsterDeviljhoRoll": True,
			"enableMonsterDeviljhoRequest": True,
			"enableMonsterZorahMagdarosRoll": True,
			"enableMonsterZorahMagdarosRequest": True,
			"enableMonsterGreatJagrasRoll": True,
			"enableMonsterGreatJagrasRequest": True,
			"enableMonsterKuluYaKuRoll": True,
			"enableMonsterKuluYaKuRequest": True,
			"enableMonsterTzitziYaKuRoll": True,
			"enableMonsterTzitziYaKuRequest": True,
			"enableMonsterGreatGirrosRoll": True,
			"enableMonsterGreatGirrosRequest": True,
			"enableMonsterDodogamaRoll": True,
			"enableMonsterDodogamaRequest": True,
			"enableMonsterPukeiPukeiRoll": True,
			"enableMonsterPukeiPukeiRequest": True,
			"enableMonsterBarrothRoll": True,
			"enableMonsterBarrothRequest": True,
			"enableMonsterJyuratodusRoll": True,
			"enableMonsterJyuratodusRequest": True,
			"enableMonsterTobiKadachiRoll": True,
			"enableMonsterTobiKadachiRequest": True,
			"enableMonsterAnjanathRoll": True,
			"enableMonsterAnjanathRequest": True,
			"enableMonsterPaolumuRoll": True,
			"enableMonsterPaolumuRequest": True,
			"enableMonsterRadobaanRoll": True,
			"enableMonsterRadobaanRequest": True,
		}

	weapons.initialize_weapon_data()
	monsters.initialize_monster_data()

	# Parse Settings
	for setting in settings.keys():

		if isinstance(settings[setting], bool) and settings[setting] == True:
			isRoll = ("Roll" in setting)

			trimmedSettingKey = setting.replace("Roll", "")
			trimmedSettingKey = trimmedSettingKey.replace("Request", "")

			if "enableWeapon" in trimmedSettingKey:
				trimmedSettingKey = trimmedSettingKey.replace("enableWeapon", "")
				if (isRoll):
					weapons.add_weapon_to_enabled_rolls(trimmedSettingKey)
				else:
					weapons.add_weapon_to_enabled_requests(trimmedSettingKey)
				

			if "enableMonster" in trimmedSettingKey:
				trimmedSettingKey = trimmedSettingKey.replace("enableMonster", "")
				if (isRoll):
					monsters.add_monster_to_enabled_rolls(trimmedSettingKey)
				else:
					monsters.add_monster_to_enabled_requests(trimmedSettingKey)

		huntQueue = HuntQueue(settings["huntQueueSize"], weapons.get_weapon_roll_count(), monsters.get_monster_roll_count())


# ---------------------------
# [Required] Execute Data / Process messages
# ---------------------------
def Execute(data):

	if data.IsChatMessage:

		global huntQueue

		firstParam = data.GetParam(0).lower()

		if firstParam == settings["queueGetNextHuntCommand"] and Parent.HasPermission(data.User, settings["queueGetNextHuntCommandPermission"], ""):
			# TODO - Move to function.
			nextHunt = huntQueue.next_hunt()

			if huntQueue.is_empty():
				Parent.SendStreamMessage("Sorry, the hunt queue is empty.")
				return

			Parent.SendStreamMessage("Next hunt is " + nextHunt.weapon + " vs " + nextHunt.monster + " from @" + nextHunt.username + "!")
			return

		if firstParam == settings["currentHuntCommand"] and Parent.HasPermission(data.User, settings["currentHuntCommandPermission"], ""):
			# TODO - Move to function
			currentHunt = huntQueue.current_hunt()
			if currentHunt is None:
				Parent.SendStreamMessage("There is no current hunt.")
				return

			Parent.SendStreamMessage("Current hunt is " + currentHunt.weapon + " vs " + currentHunt.monster + " from @" + currentHunt.username + ".")
			return

		if firstParam == settings["queueRandomHuntSetupCommand"] and Parent.HasPermission(data.User, settings["queueRandomHuntSetupCommandPermission"], ""):
			# TODO - Move to function
			if huntQueue.is_full():
				Parent.SendStreamMessage("@" + data.UserName + " - Sorry, the queue is full. Please try again later.")
				return

			weapon, monster = huntQueue.add_hunt(data.UserName, data.User)
			Parent.SendStreamMessage("@" + data.UserName + " - Added " + weapon + " vs " + monster + " to the queue!")
			return

		if firstParam == settings["huntRollCommand"] and Parent.HasPermission(data.User, settings["huntRollCommandPermission"], ""):
			# TODO - Move to function
			weapon = huntQueue.roll_weapon()
			monster = huntQueue.roll_monster()
			Parent.SendStreamMessage("@" + data.UserName + " - Hunt Roll: " + weapon + " vs " + monster)
			return

		if firstParam == settings["weaponCommand"] and Parent.HasPermission(data.User, settings["weaponCommandPermission"], ""):
			# TODO - Move to function
			weapon = huntQueue.roll_weapon()
			Parent.SendStreamMessage("@" + data.UserName + " - Weapon Roll: " + weapon)
			return

		if firstParam == settings["monsterCommand"] and Parent.HasPermission(data.User, settings["monsterCommandPermission"], ""):
			# TODO - Move to function
			monster = huntQueue.roll_monster()
			Parent.SendStreamMessage("@" + data.UserName + " - Monster Roll: " + monster)
			return

		if firstParam == settings["memeSetCommand"] and Parent.HasPermission(data.User, settings["memeSetCommandPermission"], ""):
			#TODO - Move to function
			memeSet = getMemeSet(data.GetParam(1))
			if memeSet == "":
				Parent.SendStreamMessage(
					"@" + data.UserName + " - Sorry, we don't have any meme sets for " + data.GetParam(1) + " yet")
			elif not memeSet:
				Parent.SendStreamMessage("@" + data.UserName + " - Invalid Command. Please try \"!mhw-meme-set-roll weapon_type\" | weapon_types: Any, GS, LS, SnS, DB, H, HH, CB, SA, L, GL, IG, Bow, LBG, HBG")
			else:
				Parent.SendStreamMessage("@" + data.UserName + " - Meme Set Roll: " + memeSet)
			return

		if firstParam == settings["whisperCommandsCommand"] and Parent.HasPermission(data.User, settings["whisperCommandsCommandPermission"], ""):
			# TODO - Move to function
			commandList = []

			for attribute, value in settings.iteritems():
				attributeStr = str(attribute)
				commandPermissionString = attributeStr + "Permission"

				if commandPermissionString not in settings:
					continue

				if Parent.HasPermission(data.User, settings[commandPermissionString], ""):
					commandList.append(str(value))

			if commandList:
				Parent.SendStreamWhisper(data.UserName, "Your available MHW commands are: " + ", ".join(commandList))

		if firstParam == settings["queueCustomHuntCommand"] and Parent.HasPermission(data.User, settings["queueCustomHuntCommandPermission"], ""):
			# TODO - Move to function
			if huntQueue.is_full():
				Parent.SendStreamMessage("@" + data.UserName + " - Sorry, the queue is full. Please try again later.")
				return
			commandStr = settings["queueCustomHuntCommand"]
			message = data.Message.replace(commandStr + "", "").split(",")

			if len(message) != 2:
				Parent.SendStreamMessage(
					"@" + data.UserName + " - Invalid command. Please try \" "+ commandStr + " weapon, monster\"."
					"E.g.: " + commandStr + " Bow, Kushala Daora")
				return

			# Check both weapon lists to see if it's valid
			weapon = weapons.validate_name(message[0].strip(), weapons.HUNT_TYPE_REQUEST)
			if weapon == None:
				Parent.SendStreamMessage(
					"@" + data.UserName + " - Invalid weapon. Check your spelling and try again. "
					"E.g.: " + commandStr + " Bow, Kushala Daora")
				return

			monster = monsters.validate_name(message[1].strip(), monsters.HUNT_TYPE_REQUEST)
			if monster == None:
				Parent.SendStreamMessage("you entered: " + message[1].strip() + 
					"@" + data.UserName + " - Invalid monster. Check your spelling and try again. "
					"E.g.: " + commandStr + " Bow, Kushala Daora")
				return

			huntQueue.add_hunt(data.UserName, data.User, weapon, monster)
			Parent.SendStreamMessage("@" + data.UserName + " - Added " + weapon + " vs " + monster + " to the queue!")
			return

	return


# ---------------------------
# [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
# ---------------------------
def ScriptToggled(state):
	return


# ---------------------------
# [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
# ---------------------------
def ReloadSettings(jsonData):
	Init()
	return


# ---------------------------
# [Required] Tick method (Gets called during every iteration even when there is no incoming data)
# ---------------------------
def Tick():
	return


# ---------------------------
# Helper method used by UI_Config.json to open the README.md file from script settings ui.
# ---------------------------
def OpenReadMe():
	location = os.path.join(os.path.dirname(__file__), "README.md")
	os.startfile(location)
	return
