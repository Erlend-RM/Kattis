class NumbersOnATree:
    def __init__(self, height, path):
        self.height = height
        self.path = path
        self.nodeHeight = len(path)
        self.node = 0

    def root(self):
        root = 2 ** (self.height + 1) - 1
        return root

    def resultNode(self):
        low = 0
        for i in range(self.height - self.nodeHeight):
            low += 2 ** (self.height - i)
        high = low + 2**self.nodeHeight
        self.node = (low + high) // 2
        for i in self.path:
            if i == "L":
                low = self.node
                self.node = (low + high) // 2
            elif i == "R":
                high = self.node
                self.node = (low + high) // 2
        return self.node + 1


def main():
    line = input().strip().split()
    height = int(line[0])
    if len(line) > 1:
        path = line[1]
        node = NumbersOnATree(height, path)
    else:
        node = NumbersOnATree(height, "")
    print(node.resultNode())


if __name__ == '__main__':
    main()