import clr
import json
import os
import ctypes
import codecs
import random
import Queue
import sys

# import any custom modules under the "sys.path.append(os.path.dirname(__file__))" line
# Required for importing modules from the main scripts directory
# StreamLabs thread: https://ideas.streamlabs.com/ideas/SL-I-3971
sys.path.append(os.path.dirname(__file__))
from memes.meme_sets import getMemeSet
from settings.settings import weapons, monsters

ScriptName = "MHW Companion"
Website = "NA"
Description = "Monster Hunter World Companion for StreamLabs ChatBot"
Creator = "VizionzEvo"
Version = "0.1.0"

configFile = "config.json"
settings = {}

huntCurrent = None
huntQueue = None


def ScriptToggled(state):
	return

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
			"queueGetNextHuntCommand": "!mhw-nhunt",
			"currentHuntCommand": "!mhw-chunt",
			"huntSetupCommand": "!mhw-hunt-roll",
			"weaponCommand": "!mhw-weapon-roll",
			"monsterCommand": "!mhw-monster-roll",
			"memeSetCommand": "!mhw-meme-set-roll",
			"huntQueueSize": 10,
			"permission": "Everyone",
			"useCooldown": True,
			"useCooldownMessages": True,
			"cooldown": 1,
			"onCooldown": "$user, $command is still on cooldown for adfasdfasdf minutes!",
			"userCooldown": 10,
			"onUserCooldown": "$user, $command is still on user cooldown for adsfasdfasdf minutes!"
		}

	huntQueue = Queue.Queue(maxsize=settings["huntQueueSize"])

def Execute(data):

	if data.IsChatMessage:

		global huntQueue
		global huntCurrent

		if data.GetParam(0).lower() == settings["queueGetNextHuntCommand"] and Parent.HasPermission(data.User, settings["permission"], ""):
			#TODO - Move to function.
			#TODO - Setup permission variable.
			if huntQueue.empty() == True:
				Parent.SendStreamMessage("Sorry, the hunt queue is empty.")
				huntCurrent = None
				return

			huntCurrent = huntQueue.get()
			Parent.SendStreamMessage("Next hunt is " + huntCurrent.weapon + " vs " + huntCurrent.monster + " from @" + huntCurrent.userName + "!")
			return

		if data.GetParam(0).lower() == settings["currentHuntCommand"] and Parent.HasPermission(data.User, settings["permission"], ""):
			#TODO - Move to function
			#TODO - Setup permission variable.
			if huntCurrent is None:
				Parent.SendStreamMessage("There is no current hunt.")
				return

			Parent.SendStreamMessage("Current hunt is " + huntCurrent.weapon + " vs " + huntCurrent.monster + " from @" + huntCurrent.userName + ".")
			return

		if data.GetParam(0).lower() == settings["queueRandomHuntSetupCommand"] and Parent.HasPermission(data.User, settings["permission"], ""):
			#TODO - Move to function
			#TODO - Setup permission variable.
			weapon = random.choice(weapons)
			monster = random.choice(monsters)

			if huntQueue.full() == True:
				Parent.SendStreamMessage("@" + data.UserName + " - Sorry, the queue is full. Please try again later.")
				return

			huntQueue.put(HuntData(data.UserName, data.User, weapon, monster))
			Parent.SendStreamMessage("@" + data.UserName + " - Added " + weapon + " vs " + monster + " to the queue!")
			return

		if data.GetParam(0).lower() == settings["huntSetupCommand"] and Parent.HasPermission(data.User, settings["permission"], ""):
			#TODO - Move to function
			#TODO - Setup permission variable.
			weapon = random.choice(weapons)
			monster = random.choice(monsters)
			Parent.SendStreamMessage("@" + data.UserName + " - Hunt Roll: " + weapon + " vs " + monster)
			return

		if data.GetParam(0).lower() == settings["weaponCommand"] and Parent.HasPermission(data.User, settings["permission"], ""):
			#TODO - Move to function
			#TODO - Setup permission variable.
			weapon = random.choice(weapons)
			Parent.SendStreamMessage("@" + data.UserName + " - Weapon Roll: " + weapon)
			return

		if data.GetParam(0).lower() == settings["monsterCommand"] and Parent.HasPermission(data.User, settings["permission"], ""):
			#TODO - Move to function
			#TODO - Setup permission variable.
			monster = random.choice(monsters)
			Parent.SendStreamMessage("@" + data.UserName + " - Monster Roll: " + monster)
			return

		if data.GetParam(0).lower() == settings["memeSetCommand"] and Parent.HasPermission(data.User, settings["permission"], ""):
			#TODO - Move to function
			#TODO - Setup permission variable.
			set = getMemeSet(data.GetParam(1))
			if set=="":
				Parent.SendStreamMessage("@" + data.UserName + " - Sorry, we don't have any meme sets for "+data.GetParam(1)+" yet")
			elif not set:
				Parent.SendStreamMessage("@" + data.UserName + " - Invalid Command. Please try \"!mhw-meme-set-roll weapon_type\" \
										  weapon_types: All, GS, LS, SnS, DB, Hammer, HH, CB, SA, Lance, GL, IG, Bow, LBG, HBG")
			else:
				Parent.SendStreamMessage("@" + data.UserName + " - Meme Set Roll: " + set)
			return
	return

def ReloadSettings(jsonData):
	Init()
	return

def OpenReadMe():
	location = os.path.join(os.path.dirname(__file__), "README.md")
	os.startfile(location)
	return

def Tick():
	return


class HuntData():
	def __init__(self, userName, user, weapon, monster):
		self.userName = userName
		self.user = user
		self.weapon = weapon
		self.monster = monster
