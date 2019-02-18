import itertools
sets = {
    "gs" : [
        "https://bit.ly/Meme-GS-1",
        "https://bit.ly/Meme-GS-2",
        "https://bit.ly/Meme-GS-3"
    ],
    "ls" : [
        "https://bit.ly/Meme-LS-1",
        "https://bit.ly/Meme-LS-2",
        "https://bit.ly/Meme-LS-3",
        "https://bit.ly/Meme-LS-4"
    ],
    "db" : [
        "https://bit.ly/Meme-DB-1",
        "https://bit.ly/Meme-DB-2"
    ],
    "sns" : [],
    "h" : [],
    "hh" : [
        "https://bit.ly/Meme-HH-1",
    ],
    "cb" : [
        "https://bit.ly/Meme-CB-1",
    ],
    "sa" : [],
    "l" : [
        "https://bit.ly/Meme-Lance-1",
    ],
    "gl" : [
        "https://bit.ly/Meme-GL-1",
    ],
    "ig" : [
        "https://bit.ly/Meme-IG-1",
        "https://bit.ly/Meme-IG-2",
        "https://bit.ly/Meme-IG-3",
        "https://bit.ly/Meme-IG-4",
        "https://bit.ly/Meme-IG-5",
        "https://bit.ly/Meme-IG-6"
    ],
    "b" : [
        "https://bit.ly/Meme-Bow-1",
        "https://bit.ly/Meme-Bow-2",
        "https://bit.ly/Meme-Bow-3",
        "https://bit.ly/Meme-Bow-4"
    ],
    "lbg" : [
        "https://bit.ly/Meme-LBG-1"
    ],
    "hbg" : [
        "https://bit.ly/Meme-HBG-1",
        "https://bit.ly/Meme-HBG-2",
        "https://bit.ly/Meme-HBG-3",
        "https://bit.ly/Meme-HBG-4",
        "https://bit.ly/Meme-HBG-5",
        "https://bit.ly/Meme-HBG-6"
    ],
}

def getAll():
    all=itertools.chain(sets['gs'],sets['ls'],sets['db'],sets['sns'],sets['h'],sets['hh'],sets['cb'],sets['sa'],sets['l'],sets['gl'],sets['ig'],sets['b'],sets['hbg'],sets['lbg'])
    return list(all)
