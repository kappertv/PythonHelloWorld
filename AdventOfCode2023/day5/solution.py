class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic
        
with open("sampleinput") as f:
    data = f.read()
    lines = data.split("\n")


def lowestLocationNumber() -> int:
    print(lines)
    return 0

def part1() -> int:
    return lowestLocationNumber()