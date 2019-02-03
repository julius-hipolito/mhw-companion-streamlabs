import clr
import sys
import json
import os
import ctypes
import codecs
import random
import Queue

ScriptName = "MHW Companion"
Website = "NA"
Description = "Monster Hunter World Companion for StreamLabs ChatBot"
Creator = "VizionzEvo"
Version = "0.1.0"

configFile = "config.json"
settings = {}

huntCurrent = None
huntQueue = None

#TODO - Move to settings.
weapons = [
	"Insect Glaive",
	"Charge Blade",
	"Switch Axe",
	"Bow",
	"Light Bow Gun",
	"Heavy Bow Gun",
	"Hammer",
	"Hunting Horn",
	"Long Sword",
	"Sword & Shield",
	"Lance",
	"Gun Lance"
]

#TODO - Move to settings.
monsters = [
	"Teostra",
	"Lunastra",
	"Kirin",
	"Nergigante",
	"Vaal Hazak",
	"Rathalos",
	"Azure Rathalos",
	"Pink Rathian",
	"Diablos",
	"Black Diablos",
	"Bazelgeuse",
	"Uragaan",
	"Lavasioth", 
	"Legiana", 
	"Odogaron",
	"Devil Jho",
	"Xeno'jiva",
	"Zorah Magdaros",
	"Great Jagras",
	"Kulu-Ya-Ku",
	"Tzitzi-Ya-Ku",
	"Great Girros",
	"Dodogama"
]

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