
def apply(x, map) -> int:
    # dest, src, range
    for m in map:
        dest = m[0]
        src = m[1]
        range = m[2]
        # print(f'{dest}, {src}, {range}, {x}')
        if (x >= src and x < (src + range)):
            # print('true')
            return x + dest - src
    
    return x

        
def getLocation(seed, mSoil, mFert, mWater, mLight, mTemp, mHum, mLoc) -> int:
    soil = apply(seed, mSoil)
    fert = apply(soil, mFert)
    water = apply(fert, mWater)
    light = apply(water, mLight)
    temp = apply(light, mTemp)
    hum = apply(temp, mHum)
    loc = apply(hum, mLoc)
    print(f'{soil}, {fert}, {water}, {light}, {temp}, {temp}, {hum}, {loc}')
    return loc    


def getMap(lines) -> []:
    map = []
    for l in lines:
        map.append([int(elem) for elem in l.split()])
    return map



def part2(input) -> int:
    with open(input) as f:
        data = f.read()
        lines = data.split("\n")

    sr = [int(elem) for elem in lines[0][7:].split()]
    seeds = []
    
    for i,r in zip(sr[0::2], sr[1::2]):
        for j in range(r):
            seeds.append(i+j)
    print(len(seeds))
    print(seeds)
    
    return 0
    
    iSoil = lines.index('seed-to-soil map:')
    iFert = lines.index('soil-to-fertilizer map:')
    iWater = lines.index('fertilizer-to-water map:')
    iLight = lines.index('water-to-light map:')
    iTemp = lines.index('light-to-temperature map:')
    iHum = lines.index('temperature-to-humidity map:')
    iLoc = lines.index('humidity-to-location map:')
    
    mSoil = getMap(lines[iSoil+1:iFert-1])
    mFert = getMap(lines[iFert+1:iWater-1])
    mWater = getMap(lines[iWater+1:iLight-1])
    mLight = getMap(lines[iLight+1:iTemp-1])
    mTemp = getMap(lines[iTemp+1:iHum-1])
    mHum = getMap(lines[iHum+1:iLoc-1])
    mLoc = getMap(lines[iLoc+1:])

    locations = []
    for s in seeds:
        locations.append(getLocation(s, mSoil, mFert, mWater, mLight, mTemp, mHum, mLoc))
    return min(locations)

def part1(input) -> int:
    with open(input) as f:
        data = f.read()
        lines = data.split("\n")

    seeds = [int(elem) for elem in lines[0][7:].split()]
    
    iSoil = lines.index('seed-to-soil map:')
    iFert = lines.index('soil-to-fertilizer map:')
    iWater = lines.index('fertilizer-to-water map:')
    iLight = lines.index('water-to-light map:')
    iTemp = lines.index('light-to-temperature map:')
    iHum = lines.index('temperature-to-humidity map:')
    iLoc = lines.index('humidity-to-location map:')
    
    mSoil = getMap(lines[iSoil+1:iFert-1])
    mFert = getMap(lines[iFert+1:iWater-1])
    mWater = getMap(lines[iWater+1:iLight-1])
    mLight = getMap(lines[iLight+1:iTemp-1])
    mTemp = getMap(lines[iTemp+1:iHum-1])
    mHum = getMap(lines[iHum+1:iLoc-1])
    mLoc = getMap(lines[iLoc+1:])

    locations = []
    for s in seeds:
        locations.append(getLocation(s, mSoil, mFert, mWater, mLight, mTemp, mHum, mLoc))
    return min(locations)