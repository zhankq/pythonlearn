def make_averager():
    nums = []

    def averager(n):
        nums.append(n)
        return sum(nums)/len(nums)
    return averager

averagers = make_averager()

print(averagers(10))
print(averagers(20))
print(averagers(30))
print(averagers(40))
