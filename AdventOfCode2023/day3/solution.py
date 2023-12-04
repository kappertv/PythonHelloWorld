def create_empty_matrix(n, m):
    ans = []
    for i in range(n):
        ans.append([0] * m)
    return ans

def sumOfAllPartNumbersPart1() -> int:
    with open("sampleinput") as f:
        data = f.read()
        lines = data.split("\n")
        m = create_empty_matrix(len(lines), len(lines[0]))
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                m[i][j] = lines[i][j]
            
        print("matrix", m)
                
        return 0
