with open("input") as f:
    data = f.read().strip()
    lines = data.split("\n")
    racedurations = lines[0][5::].split()
    recordracedistances = lines[1][9::].split()

def getPossibleRaceOutcomes(duration) -> []:
    res = []
    for speed in range(1, duration):
        res.append((duration - speed) * speed)
         
    return res

def numberOfWaysToBeatTheRecord(duration, recorddistance) -> int:
    res = list(filter(lambda x: x > recorddistance, getPossibleRaceOutcomes(duration)))

    # print(res)
    return len(res)

def errorMarginPart1() -> int:
    # print(racedurations)
    # print(recordracedistances)
    res = []
    for i in range(len(racedurations)):
        res.append(numberOfWaysToBeatTheRecord(int(racedurations[i]), int(recordracedistances[i])))
    
    print(res)
    r = 1
    for s in res:
        r = r * s
    
    return r

def part2() -> int:
    oneduration = ''.join(racedurations)
    onerecorddistance = ''.join(recordracedistances)
    print(oneduration)
    print(onerecorddistance)
    
    return numberOfWaysToBeatTheRecord(int(oneduration), int(onerecorddistance))
    