
def getValueOfCard(w,p) -> int:
    n = len(list(set(w).intersection(p)))
    
    if n == 0:
        return 0
    
    res = 1
    
    for i in range(n-1):
        res = res * 2
    
    print(res)
    return res

def sumOfAllCardValuesPart1() -> int:
    with open("sampleinput") as f:
        data = f.read()
        cards = data.split("\n")
    res = 0
    for card in cards:
        c = card.split(": ")[1].split("|")
        winningcards = c[0].split()
        playcards = c[1].split()
        
        res += getValueOfCard(winningcards, playcards)

    return res

def countTotalScratchCardsPart2() -> int:
    with open("sampleinput") as f:
        data = f.read()
        cards = data.split("\n")
    res = 0
    instancesOfCards = []
    for card in cards:
        s = card.split(": ")[0]
        cid = int(s[5:])
        instancesOfCards.append(cid)
        c = card.split(": ")[1].split("|")
        
        winningcards = c[0].split()
        playcards = c[1].split()
        
        dublicatecardsincludeorig = list(filter(lambda x: x == cid, instancesOfCards))
        
        # print(dublicatecardsincludeorig)
        
        matchingnumbers = len(list(set(winningcards).intersection(playcards)))
        
        for i in range(len(dublicatecardsincludeorig)):
            for j in (range(matchingnumbers)):
                instancesOfCards.append(cid + j + 1)
        
        # print(instancesOfCards)
    
    return len(instancesOfCards)