from collections import deque

class PairingSocks:

    def __init__(self, pairs, originalPile):
        self.pairs = pairs
        self.originalPile = originalPile
        self.auxiliaryPile = deque()

    
    def pair(self):
        nrOfMoves = 0
        while True:
            if self.auxiliaryPile and self.originalPile:
                if self.originalPile[0] == self.auxiliaryPile[0]:
                    self.originalPile.popleft()
                    self.auxiliaryPile.popleft()
                else:
                    self.auxiliaryPile.appendleft(self.originalPile.popleft())
            elif self.auxiliaryPile:
                return "impossible" 
            elif self.originalPile:
                self.auxiliaryPile.appendleft(self.originalPile.popleft())
            else:
                return nrOfMoves
            nrOfMoves += 1


def main():
    
    pairs = int(input().strip())
    pile = deque(input().strip().split(" "))
    
    pair = PairingSocks(pairs, pile)
    print(pair.pair())


if __name__ == "__main__":
    main()



