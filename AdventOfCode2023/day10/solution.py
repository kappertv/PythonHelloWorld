def create_map(lines):
    ans = []
    for l in lines:
        ans.append(list(l))
    return ans

def findStart(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'S':
                return (y,x)

def part1(input) -> int:
    with open(input) as f:
        data = f.read().rstrip()
        lines = data.splitlines()
        
    m = create_map(lines)
    
    print(m)
    print(findStart(m))
    # from starttile
    # needed steps = 0
    # find possible directions
    # for each possible direction increase needed steps
    # find possible directions not going back (check of needed steps is known)
    return None