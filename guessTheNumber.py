import sys


class GuessTheNumber:
    def __init__(self, number):
        self.number = number
        self.guessNr = 500
        self.max = 1000
        self.min = 0


    def guess(self):
        print(self.guessNr, flush = True)
        for _ in range(10):
            answer = sys.stdin.readline().strip()

            if answer == "lower":
                self.max = self.guessNr
                self.guessNr = (self.min + self.max) // 2
            elif answer == "higher":
                self.min = self.guessNr
                self.guessNr = (self.min + self.max + 1) // 2
            elif answer == "correct":
                break

            print(self.guessNr, flush = True)

  
def main():
    rightNr = GuessTheNumber(sys.stdin.readline().strip())
    rightNr.guess()
    

if __name__ == "__main__":
    main()
   