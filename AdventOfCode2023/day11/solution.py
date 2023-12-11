def expandColumnAt(x, map):
    for r in map:
        r[x] = 1000000

def noGalaxiesInColumn(x, map) -> bool:
    for r in map:
        if r[x] == '#':
            return False
    return True

def create_expandeduniverse(lines):
    u = []
    for l in lines:
        if '#' not in l:
            u.append([1000000]*(len(l))) # expand row        
        else:    
            u.append(list(l))
    for x in range(len(u[0])):
        if noGalaxiesInColumn(x, u):
            expandColumnAt(x, u)
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


def calcDist(s, d, u):
#    print(f'{s}, {d}')
    minr = min(s[0], d[0])
    maxr = max(s[0], d[0])
    minc = min(s[1], d[1])
    maxc = max(s[1], d[1])
    res = 0
    for r in range(minr, maxr):
        dig = u[r][minc]
 #       print(f'dig:{dig}')
        if dig == '.' or dig == '#':
            res += 1
        else:
            res += int(dig)

    for c in range(minc, maxc):
        dig = u[s[0]][c]
  #      print(f'dig:{dig}')
        if dig == '.' or dig == '#':
            res += 1
        else:
            res += int(dig)
    
   # print(f'return {res}')
    return res

def getDistances(g, u):
    res = []
    for i in range(len(g)):
        for j in range(i+1, len(g)):
            res.append(calcDist(g[i], g[j], u))
    return res

def part1(input) -> int:
    with open(input) as f:
        data = f.read().rstrip()
        lines = data.splitlines()
                
    u = create_expandeduniverse(lines)
    #print(u)
    #print(f'height: {len(u)}, width: {len(u[0])}')
    
    g = getGalaxies(u)
    #print(g)
    d = getDistances(g, u)
    #print(d)
    return sum(d)

def part2(input) -> int:
    # do not add lines to grid, but specify distance in galaxies.
    return 0
    
