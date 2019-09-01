class C:
    print("class C being defined...")

class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members+=1

m1 = MemberCounter()
m1.init()
print(MemberCounter.members)

m2 = MemberCounter()
m2.init()
print(MemberCounter.members)

class SonClass(MemberCounter):
    def init(self):
        return "nothing"

print(issubclass(SonClass,MemberCounter))

