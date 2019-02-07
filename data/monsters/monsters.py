import json
import os
import codecs

__enabledMonsterRollIds = []
__enabledMonsterRequestIds = []
__monsterDataArray = []

def update_enabled_monster_ids(enabledRollIds, enabledRequestIds):
	if isinstance(enabledRollIds, list):
		__enabledMonsterRollIds = enabledRollIds
	if isinstance(enabledRequestIds, list):
		__enabledMonsterRequestIds = enabledRequestIds
	return

def initialize_monster_data():
	path = os.path.dirname(__file__)
	with codecs.open(os.path.join(path, "monsters.json"), encoding='utf-8-sig', mode='r') as file:
		__monsterDataArray = json.load(file, encoding='utf-8-sig')
	return

def do_get_count():
	return len(__monsterDataArray)