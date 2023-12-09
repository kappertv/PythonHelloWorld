class Node:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node({self.node},{self.left},{self.right})'

def simultaniousStepsA2Z(instructions, nodes) -> int:
    steps = 0
    startKeys = list(filter(lambda k: k.endswith('A'), nodes.keys()))
    count = len(startKeys)
    allNodesEndWithZ = len(list(filter(lambda k: k.endswith('Z'), startKeys))) == count
   #  print(allNodesEndWithZ)
    while not allNodesEndWithZ and steps < 10:
        print(len(startKeys))
        for n in startKeys:
            print(f'{n}: {nodes[n]}')
        newKeys = []
        if instructions[steps % len(instructions)] == 'L': #left
            print('left')
            for n in startKeys:
                newKeys.append(nodes[n][0])
        else:
            print('right')
            for n in startKeys:
                newKeys.append(nodes[n][1])
        startKeys = newKeys
        endz = len(list(filter(lambda k: k.endswith('Z'), startKeys))) 
        allNodesEndWithZ = endz == count
        steps = steps + 1

    
    return steps

def stepsFromAAA2ZZZ(instructions, nodes) -> int:
    steps = 0
    currentNode = next(x for x in nodes if x.node == 'AAA')
    # print(instructions)
    # print(currentNode)
    
    while (currentNode.node != 'ZZZ'):
    #for step in range(10):
        s = instructions[steps % len(instructions)] == 'L'
        # print(s)
        if instructions[steps % len(instructions)] == 'L':
            currentNode = next(x for x in nodes if x.node == currentNode.left)
        else:
            currentNode = next(x for x in nodes if x.node == currentNode.right)
        # print(currentNode)
        steps = steps + 1
            
    return steps

def part1(input) -> int:
    nodes = []
    with open(input) as f:
        data = f.read().strip()
        lines = data.split("\n")
        instructions = lines[0]
        for line in lines[2:]:
            s = line.split(" = ")
            lr = s[1].translate(dict.fromkeys(map(ord, '()'), None)).split(",")
            nodes.append(Node(s[0], lr[0], lr[1].strip()))
    
    # print(instructions)
    # for node in nodes:
    #     print(node)
    
    return stepsFromAAA2ZZZ(instructions, nodes)

def part2(input) -> int:
    with open(input) as f:
        data = f.read().strip()
        lines = data.split("\n")
        instructions = lines[0]
        
        nodes = {}
        
        for line in lines[2:]:
            s = line.split(" = ")
            lr = s[1].translate(dict.fromkeys(map(ord, '()'), None)).split(",")
            nodes[s[0]] = (lr[0], lr[1].strip())
           # nodes.append(Node(s[0], lr[0], lr[1].strip()))
    # print(nodes.keys())
    # print(nodes.values())
    return simultaniousStepsA2Z(instructions, nodes)