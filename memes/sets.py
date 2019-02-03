import itertools
sets = {
    "GS" : [
        "http://honeyhunterworld.com/mhwb/?23,118,107,107,105,100,75,0,0,0,30,0,0,16,68,0,24,0,0,0,26,0,12,0,0,5,68,0,2",
        "http://honeyhunterworld.com/mhwb/?640,95,74,80,76,76,48,0,0,0,25,25,0,25,0,0,25,0,0,25,0,0,5,0,0,5,5,0,3",
        "http://honeyhunterworld.com/mhwb/?680,118,107,107,103,107,72,0,0,0,39,0,0,25,39,0,39,0,0,64,64,0,64,20,20,64,0,0,3"
    ],
    "LS" : [
        "http://honeyhunterworld.com/mhwb/?683,118,103,107,105,107,3,0,0,0,21,0,0,8,5,0,36,36,31,42,0,0,0,0,0,0,0,0,3",
        "http://honeyhunterworld.com/mhwb/?643,95,71,71,69,71,6,0,0,0,53,90,0,53,0,0,96,0,0,0,0,0,96,0,0,96,0,0,3",
        "http://honeyhunterworld.com/mhwb/?43,84,88,78,76,88,83,0,0,0,0,0,0,92,31,0,18,54,0,0,0,0,51,0,0,21,11,0,2",
        "http://honeyhunterworld.com/mhwb/?42,94,87,87,85,87,48,0,0,0,33,51,0,19,0,0,5,0,0,3,0,0,21,0,0,3,0,0,3"
    ],
    "DB" : [
        "http://honeyhunterworld.com/mhwb/?361,110,72,99,70,99,44,0,0,0,80,0,0,34,37,0,37,37,96,34,18,0,18,42,42,34,42,0,3",
        "http://honeyhunterworld.com/mhwb/?354,110,72,99,70,99,44,att,att,0,0,0,0,80,37,0,37,37,96,34,18,0,18,42,42,34,42,0,3"
    ],
    "SnS" : [],
    "Hammer" : [],
    "HH" : [
        "http://honeyhunterworld.com/mhwb/?447,116,103,103,103,105,27,0,0,0,0,0,0,54,0,0,96,96,96,73,42,0,42,42,76,76,76,0,3",
    ],
    "CB" : [
        "http://honeyhunterworld.com/mhwb/?289,17,26,22,88,92,24,0,0,0,42,27,0,0,0,0,27,0,0,73,0,0,0,0,0,37,37,0,3",
    ],
    "SA" : [],
    "Lance" : [
        "http://honeyhunterworld.com/mhwb/?148,95,83,84,82,72,3,slot,0,0,49,0,0,77,0,0,49,0,0,96,96,96,18,18,0,90,0,0,3",
    ],
    "GL" : [
        "http://honeyhunterworld.com/mhwb/?401,95,70,68,66,67,10,0,0,0,0,0,0,12,0,0,42,42,0,19,0,0,19,0,0,4,0,0,3",
    ],
    "IG" : [
        "http://honeyhunterworld.com/mhwb/?680,116,87,80,103,105,64,0,0,0,91,0,0,91,0,0,54,0,0,90,0,0,90,96,96,75,96,0,2",
        "http://honeyhunterworld.com/mhwb/?680,118,107,107,105,107,2,0,0,0,96,0,0,12,5,0,42,0,0,21,20,0,42,0,0,50,0,0,3",
        "http://honeyhunterworld.com/mhwb/?484,95,87,87,105,87,64,0,0,0,33,0,0,67,0,0,96,0,0,96,0,0,51,0,0,86,0,0,2",
        "http://honeyhunterworld.com/mhwb/?680,110,98,99,96,99,3,0,0,0,34,0,0,0,18,0,0,0,0,25,5,0,92,0,0,0,20,0,3",
        "http://honeyhunterworld.com/mhwb/?670,83,78,107,76,107,91,health,0,0,12,5,0,30,0,0,16,30,0,56,56,0,56,0,0,33,0,0,2",
        "http://honeyhunterworld.com/mhwb/?668,99,84,84,82,91,9,0,0,0,0,0,0,33,18,0,18,18,0,18,69,42,5,73,0,0,0,0,3"
    ],
    "Bow" : [
        "http://honeyhunterworld.com/mhwb/?269,94,88,88,86,88,64,0,0,0,0,0,0,28,0,0,0,0,0,0,0,0,33,0,0,0,0,0,2",
        "http://honeyhunterworld.com/mhwb/?280,103,84,84,82,82,3,health,0,0,0,0,0,92,54,54,54,69,0,96,96,96,92,92,0,50,0,0,3",
        "http://honeyhunterworld.com/mhwb/?280,112,62,101,76,101,59,0,0,0,0,0,0,5,0,0,34,0,0,12,0,0,19,0,0,25,0,0,3"
    ],
    "LBG" : [
        "http://honeyhunterworld.com/mhwb/?673,119,104,107,76,107,82,aff,0,0,71,5,0,90,90,0,5,94,0,90,57,0,57,0,0,57,0,0,2,Recoil,Recoil,Recoil"
    ],
    "HBG" : [
        "http://honeyhunterworld.com/mhwb/?676,103,99,84,68,103,72,slot,0,0,65,76,68,37,37,37,42,37,0,37,86,76,42,0,0,42,76,0,3,Reload,Reload,Reload",
        "http://honeyhunterworld.com/mhwb/?267,94,62,87,86,86,21,health,health,0,0,0,0,51,0,0,51,0,0,96,0,0,51,31,0,31,31,0,3,Recoil,Recoil,Shield",
        "http://honeyhunterworld.com/mhwb/?676,84,103,105,85,86,2,0,0,0,71,5,0,31,31,0,31,76,76,0,0,0,16,0,0,96,36,0,3,Recoil,Recoil,Shield",
        "http://honeyhunterworld.com/mhwb/?628,95,98,80,97,86,101,aff,att,0,0,0,0,16,0,0,96,0,0,84,0,0,26,96,0,49,49,0,1,Shield,Shield,Shield",
        "http://honeyhunterworld.com/mhwb/?267,94,88,88,86,88,8,0,0,0,0,0,0,45,0,0,56,56,0,16,0,0,5,56,0,4,4,0,3,Shield,Shield,Shield",
        "http://honeyhunterworld.com/mhwb/?637,95,88,87,96,87,64,0,0,0,25,0,0,0,0,0,5,96,0,36,0,0,37,0,0,0,0,0,2,Shield,Shield,Shield"
    ],
}

def getAll():
    all=itertools.chain(sets['GS'],sets['LS'],sets['DB'],sets['SnS'],sets['Hammer'],sets['HH'],sets['CB'],sets['SA'],sets['Lance'],sets['GL'],sets['IG'],sets['Bow'],sets['HBG'],sets['LBG'])
    return list(all)
