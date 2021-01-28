class Yuneec(object):

    def __init__(self):
        print("Yuneec init")

    def printName(self):
        print("Yuneec ", "*" * 30)


class L(object):
    fei = "fei"

    def __init__(self):
        print("L init")

    def printName(self):
        print("L ", "*" * 30)

    def __str__(self):
        print("1234")
        return "123 %s" % self.fei


print("--- Yuneec.py --- " * 5)
y = Yuneec()
# y.printName()
#
# l = L()
# l.printName()
# print(l)

# y = type(Yuneec)
t = type(Yuneec)
print(y)
print(t)
