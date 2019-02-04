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


# ---------------------------
# [Required] Script Information
# ---------------------------
ScriptName = "MHW Companion"
Website = "NA"
Description = "Monster Hunter World Companion for StreamLabs ChatBot"
Creator = "VizionzEvo"
Version = "0.1.0"


# ---------------------------
# Define Global Variables
# ---------------------------
configFile = "config.json"
settings = {}

huntCurrent = None
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
			"huntRollCommand": "!mhw-hunt-roll",
			"huntRollCommandPermission": "Everyone",
			"weaponCommand": "!mhw-weapon-roll",
			"weaponCommandPermission": "Everyone",
			"monsterCommand": "!mhw-monster-roll",
			"monsterCommandPermission": "Everyone",
			"memeSetCommand": "!mhw-meme-set-roll",
			"memeSetCommandPermission": "Everyone",
			"huntQueueSize": 10,
			"permission": "Everyone",
			"useCooldown": True,
			"useCooldownMessages": True,
			"cooldown": 1,
			"onCooldown": "$user, $command is still on cooldown for adfasdfasdf minutes!",
			"userCooldown": 10,
			"onUserCooldown": "$user, $command is still on user cooldown for adsfasdfasdf minutes!"
		}

	huntQueue = HuntQueue(maxsize=settings["huntQueueSize"])


# ---------------------------
# [Required] Execute Data / Process messages
# ---------------------------
def Execute(data):

	if data.IsChatMessage:

		global huntQueue
		global huntCurrent
		
		firstParam = data.GetParam(0).lower()

		if firstParam == settings["queueGetNextHuntCommand"] and Parent.HasPermission(data.User, settings["queueGetNextHuntCommandPermission"], ""):
			# TODO - Move to function.
			if huntQueue.empty():
				Parent.SendStreamMessage("Sorry, the hunt queue is empty.")
				huntCurrent = None
				return

			huntCurrent = huntQueue.get()
			Parent.SendStreamMessage("Next hunt is " + huntCurrent.weapon + " vs " + huntCurrent.monster + " from @" + huntCurrent.userName + "!")
			return

		if firstParam == settings["currentHuntCommand"] and Parent.HasPermission(data.User, settings["currentHuntCommandPermission"], ""):
			# TODO - Move to function
			if huntCurrent is None:
				Parent.SendStreamMessage("There is no current hunt.")
				return

			Parent.SendStreamMessage("Current hunt is " + huntCurrent.weapon + " vs " + huntCurrent.monster + " from @" + huntCurrent.userName + ".")
			return

		if firstParam == settings["queueRandomHuntSetupCommand"] and Parent.HasPermission(data.User, settings["queueRandomHuntSetupCommandPermission"], ""):
			# TODO - Move to function
			if huntQueue.full():
				Parent.SendStreamMessage("@" + data.UserName + " - Sorry, the queue is full. Please try again later.")
				return

			weapon, monster = huntQueue.add_hunt(data.UserName, data.User)
			Parent.SendStreamMessage("@" + data.UserName + " - Added " + weapon + " vs " + monster + " to the queue!")
			return

		if firstParam == settings["huntRollCommand"] and Parent.HasPermission(data.User, settings["huntRollCommandPermission"], ""):
			# TODO - Move to function
			weapon, monster = huntQueue.add_hunt(data.UserName, data.User)
			Parent.SendStreamMessage("@" + data.UserName + " - Hunt Roll: " + weapon + " vs " + monster)
			return

		if firstParam == settings["weaponCommand"] and Parent.HasPermission(data.User, settings["weaponCommandPermission"], ""):
			# TODO - Move to function
			weapon = random.choice(weapons)
			Parent.SendStreamMessage("@" + data.UserName + " - Weapon Roll: " + weapon)
			return

		if firstParam == settings["monsterCommand"] and Parent.HasPermission(data.User, settings["monsterCommandPermission"], ""):
			# TODO - Move to function
			monster = random.choice(monsters)
			Parent.SendStreamMessage("@" + data.UserName + " - Monster Roll: " + monster)
			return

		if firstParam == settings["memeSetCommand"] and Parent.HasPermission(data.User, settings["memeSetCommandPermission"], ""):
			# TODO - Move to function
			memeSet = getMemeSet(data.GetParam(1))
			if memeSet == "":
				Parent.SendStreamMessage(
					"@" + data.UserName + " - Sorry, we don't have any meme sets for " + data.GetParam(1) + " yet")
			elif not memeSet:
				Parent.SendStreamMessage("@" + data.UserName + " - Invalid Command. Please try \"!mhw-meme-set-roll weapon_type\" \weapon_types: Any, GS, LS, SnS, DB, Hammer, HH, CB, SA, Lance, GL, IG, Bow, LBG, HBG")
			else:
				Parent.SendStreamMessage("@" + data.UserName + " - Meme Set Roll: " + memeSet)
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
