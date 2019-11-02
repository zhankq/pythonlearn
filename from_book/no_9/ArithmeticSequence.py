def check_index(key):
    if not isinstance(key,int):raise TypeError
    if key < 0: raise IndexError

class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, item):
        check_index(item)

        try:return self.changed[item]
        except KeyError:
            return self.start + self.step*item

    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value

s= ArithmeticSequence(1,2)

print(s[4])
