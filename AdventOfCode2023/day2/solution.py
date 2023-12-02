
def create_game(game):
    g = game.split(":")
    rounddata = g[1].split(";")
    rounds = []
    for i in range(len(rounddata)):
        round = [0,0,0]
        dice = rounddata[i].split(",")
        print("dice", dice)
        for j in range(len(dice)):
            d = dice[j].strip().split(" ")
            if d[1] == "red":
                round[0] = int(d[0])
            if d[1] == "green":
                round[1] = int(d[0])
            if d[1] == "blue":
                round[2] = int(d[0]) 
        rounds.append(round)
    
    return rounds

def create_empty_matrix(n, m):
    ans = []
    for i in range(n):
        ans.append([0] * m)
    return ans

def isPossibleRound(round) -> bool:        
    return round[0] <= 12 and round[1] <= 13 and round[2] <= 14

def isPossibleGame(game) -> bool:
    for i in range(len(game)):
        if not isPossibleRound(game[i]):
            return False
    
    return True

def powerOfCubes(game) -> int:
    maxred = max(f[0] for f in game)
    maxgreen = max(f[1] for f in game)
    maxblue = max(f[2] for f in game)
    
    return maxred * maxgreen * maxblue

            

def sumOfAllValidGamesPart1() -> int:
    with open("sampleinput") as f:
        data = f.read().strip()
        gameData = data.split("\n")
        
        games = []
        for i in range(len(gameData)):
            games.append(create_game(gameData[i]))
        
        print("games", games)
        res = 0
        for i in range(len(games)):
            if (isPossibleGame(games[i])):
                res += (i + 1)
        
        return res

def sumOfAllPowerGamesPart2() -> int:
    with open("input") as f:
        data = f.read().strip()
        gameData = data.split("\n")
        
        games = []
        for i in range(len(gameData)):
            games.append(create_game(gameData[i]))
        
        print("games", games)
        res = 0
        for i in range(len(games)):
            res += powerOfCubes(games[i])
        
        return res
