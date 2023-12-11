def insertColumnAt(x, map):
    for r in map:
        r.insert(x, '.')

def noGalaxiesInColumn(x, map) -> bool:
    for r in map:
        if r[x] == '#':
            return False
    return True

def create_expandeduniverse(lines):
    u = []
    for l in lines:
        u.append(list(l))
        if '#' not in l:
            u.append(list(l)) # expand row
    for x in reversed(range(len(u[0]))):
        if noGalaxiesInColumn(x, u):
            insertColumnAt(x+1, u)
    return u    

def findGalaxies(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'S':
                return (y,x)

def getGalaxies(u):
    res = []
    for r in range(len(u)):
        for c in range(len(u[0])):
            if u[r][c] == '#':
                res.append((r, c))
    return res


def calcDist(s, d):
    return abs(s[0] - d[0]) + abs(s[1] - d[1])

def getDistances(g):
    res = []
    for i in range(len(g)):
        for j in range(i+1, len(g)):
            res.append(calcDist(g[i], g[j]))
    return res

def part1(input) -> int:
    with open(input) as f:
        data = f.read().rstrip()
        lines = data.splitlines()
                
    u = create_expandeduniverse(lines)
    # print(u)
    # print(f'height: {len(u)}, width: {len(u[0])}')
    
    g = getGalaxies(u)
    # print(g)
    d = getDistances(g)
    return sum(d)

def part2(input) -> int:
    # do not add lines to grid, but specify distance in galaxies.
    return 0
    
