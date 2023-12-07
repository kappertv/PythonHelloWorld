cards = 'AKQT98765432J'        
reversedcards = "".join(reversed(cards))

class HandAndBid:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
    
    def cardvalue(self) -> str:
        values = ""
        
        for c in self.hand:
            a = reversedcards.index(c)
            values += f"{a:02}"

        return values
            
    
    def cardcount(self) -> []:
        counts = []
        for c in cards:
            counts.append(self.hand.count(c))
        return counts
    
    def handtype(self):
        c = self.cardcount()
        j = c[-1:]
        nj = c[:12]
     #   print("jokers" + f"{j}")
     #   print("notjokers" + f"{nj}")
        jokers = max(j)
        highest = max(nj)
        if highest + jokers == 1:
            return '1 High card'
        elif highest + jokers == 4:
            return '6 Four of a kind'
        elif highest + jokers == 5:
            return '7 Five of a kind'
        elif highest == 3 and 2 in nj:
            return '5 Full house'
        elif nj.count(2) == 2 and jokers == 1:
            return '5 Full house'
        elif highest + jokers == 3:
            return '4 Three of a kind'
        elif nj.count(2) == 2:
            return '3 Two pair'
        elif nj.count(2) == 1 and jokers == 1:
            return '3 Two pair'
        elif highest + jokers == 2:
            return '2 One Pair'
        
    
    def __str__(self):
        return f'Hand({self.hand},{self.bid}, {self.handtype()}, {self.cardvalue()})'

hands = []
        
with open("input") as f:
    data = f.read().strip()
    lines = data.split("\n")
    for line in lines:
        s = line.split()
        hands.append(HandAndBid(s[0], int(s[1])))

def totalWinnings() -> int:
    
    sortedHands = sorted(hands, key=lambda hand: (hand.handtype(), hand.cardvalue()))
    
    total = 0
    rank = 1
    for hand in sortedHands:
        print(hand)
#        print(rank * hand.bid)
        total += (rank * hand.bid)
        rank += 1
        
    return total

def part1() -> int:
    return totalWinnings()