with open("input") as f:
    data = f.read().strip()

def count(group):
    return map(int, group.split("\n"))

groups = data.split("\n\n")
group_sums = [sum(count(group)) for group in groups]

def part1():
    return max(group_sums)

def part2():
    return sum(sorted(group_sums)[-3:])

# Part 1
print(part1())

# Part 2
print(part2())