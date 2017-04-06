class BinarySearch(list):
    """docstring for BinarySearch"""

    def __init__(self, a, b):
        self .extend([x for x in range(b, (a * b) + 1, b)])
        self.length = len(self)
        self.count = 0
        self.results = {"count": 0, "index": 0}

    def search(self, Phrase):
        Low = 0
        High = len(self) - 1
        found = False
        while Low <= High and not found:
            self.count = self.count + 1
            Mid = (High + Low) / 2
            if self[Mid] == Phrase:
                self.results["count"] = self.count
                self.results["index"] = Mid
                found = True
                return self.results
            elif self[Mid] > Phrase:
                High = Mid - 1
            else:
                Low = Mid + 1
        return found


two_to_forty = BinarySearch(20, 2)
print two_to_forty
search1 = two_to_forty.search(40)
print search1
