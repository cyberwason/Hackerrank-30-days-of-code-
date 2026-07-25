class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        n = len(self.__elements)
        max_diff = 0
        for i in range(n):
            for j in range(n):
                diff = abs(self.__elements[i] - self.__elements[j])
                if diff > max_diff:
                    max_diff = diff
        self.maximumDifference = max_diff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)