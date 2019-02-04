import itertools
sets = {
    "GS" : [
        "https://bit.ly/Meme-GS-1",
        "https://bit.ly/Meme-GS-2",
        "https://bit.ly/Meme-GS-3"
    ],
    "LS" : [
        "https://bit.ly/Meme-LS-1",
        "https://bit.ly/Meme-LS-2",
        "https://bit.ly/Meme-LS-3",
        "https://bit.ly/Meme-LS-4"
    ],
    "DB" : [
        "https://bit.ly/Meme-DB-1",
        "https://bit.ly/Meme-DB-2"
    ],
    "SnS" : [],
    "Hammer" : [],
    "HH" : [
        "https://bit.ly/Meme-HH-1",
    ],
    "CB" : [
        "https://bit.ly/Meme-CB-1",
    ],
    "SA" : [],
    "Lance" : [
        "https://bit.ly/Meme-Lance-1",
    ],
    "GL" : [
        "https://bit.ly/Meme-GL-1",
    ],
    "IG" : [
        "https://bit.ly/Meme-IG-1",
        "https://bit.ly/Meme-IG-2",
        "https://bit.ly/Meme-IG-3",
        "https://bit.ly/Meme-IG-4",
        "https://bit.ly/Meme-IG-5",
        "https://bit.ly/Meme-IG-6"
    ],
    "Bow" : [
        "https://bit.ly/Meme-Bow-1",
        "https://bit.ly/Meme-Bow-2",
        "https://bit.ly/Meme-Bow-3",
        "https://bit.ly/Meme-Bow-4"
    ],
    "LBG" : [
        "https://bit.ly/Meme-LBG-1"
    ],
    "HBG" : [
        "https://bit.ly/Meme-HBG-1",
        "https://bit.ly/Meme-HBG-2",
        "https://bit.ly/Meme-HBG-3",
        "https://bit.ly/Meme-HBG-4",
        "https://bit.ly/Meme-HBG-5",
        "https://bit.ly/Meme-HBG-6"
    ],
}

def getAll():
    all=itertools.chain(sets['GS'],sets['LS'],sets['DB'],sets['SnS'],sets['Hammer'],sets['HH'],sets['CB'],sets['SA'],sets['Lance'],sets['GL'],sets['IG'],sets['Bow'],sets['HBG'],sets['LBG'])
    return list(all)
