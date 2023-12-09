def getSequence(history) -> []:
    intlist = [int(elem) for elem in history.split()]
    seqdif = [intlist]
    current = intlist
    while (len(set(current)) != 1) or current[0] != 0:
        last = seqdif[-1]
        new = []
        for n in range(len(last) - 1):
            new.append(last[n+1] - last[n])
        current = new
        seqdif.append(new)
    
    return seqdif


def nextValue(history) -> int:
    seqdif = getSequence(history)
    res = 0
    for n in seqdif:
        res += n[-1]
    return res

def previousValue(history) -> int:
    seqdif = getSequence(history)
    print(seqdif)
    prevVal = 0
    for n in reversed(seqdif):
        print(f'{n} + {prevVal} - {n[0]}')
        prevVal = n[0] - prevVal
        print(prevVal)

    return prevVal


def part1(input) -> int:
    with open(input) as f:
        data = f.read().rstrip()
        lines = data.split("\n")

    return sum(map(nextValue, lines))

def part2(input) -> int:
    with open(input) as f:
        data = f.read().rstrip()
        lines = data.split("\n")

    return sum(map(previousValue, lines))
