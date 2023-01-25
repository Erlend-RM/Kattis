class Backspace:

    def __init__(self, string):
        self.string = string
        self.newString = []

    def fix(self):
        for i in self.string:
            if i == "<":
                self.newString.pop()
            else:
                self.newString.append(i)
        
        return "".join(self.newString)



def main():
    string =  input().strip()
    intendedString = Backspace(string)
    print(intendedString.fix())


if __name__ == "__main__":
    main()
